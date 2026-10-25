import hashlib,json,os,subprocess,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
PAYLOAD=b'known IPA fixture\n'
class Installer(unittest.TestCase):
 def run_installer(self,case='good',system='normal',helpers=1):
  with tempfile.TemporaryDirectory(prefix='zema-ts-test-') as tmp:
   root=Path(tmp);commands=root/'bin';commands.mkdir();apps=root/'apps';apps.mkdir();sysroot=root/'sysroot';sysroot.mkdir();log=root/'called.json'
   template=(ROOT/'package-sources/trollstore-installer/postinst.in').read_text()
   values={'APP_NAME':'Fixture','IPA_URL':'https://github.com/zemabinks/repo/releases/download/zgta-v-build-88/fixture.ipa','SHA256':hashlib.sha256(PAYLOAD).hexdigest(),'BYTES':str(len(PAYLOAD))}
   import shlex
   for k,v in values.items():template=template.replace('@'+k+'@',shlex.quote(v))
   template=template.replace('PATH=/usr/sbin:/usr/bin:/sbin:/bin:/var/jb/usr/sbin:/var/jb/usr/bin:/var/jb/sbin:/var/jb/bin','PATH='+str(commands)+':/usr/bin:/bin')
   paths={'/.sysroot/var/containers/Bundle/Application':str(sysroot/'apps'),'/private/var/containers/Bundle/Application':str(root/'private-apps'),'/var/containers/Bundle/Application':str(apps),'/.sysroot/var/jb/Applications/TrollStoreLite.app':str(sysroot/'lite'),'/.sysroot/Applications/TrollStoreLite.app':str(sysroot/'lite-root'),'/var/jb/Applications/TrollStoreLite.app':str(root/'lite'),'/Applications/TrollStoreLite.app':str(root/'lite-root')}
   for a,b in paths.items():template=template.replace(a,b)
   template=template.replace('/.sysroot/*',str(sysroot)+'/*').replace('/var/tmp/zema-trollstore.',str(root/'download.'))
   def executable(path,text):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text);path.chmod(0o755)
   helper='''#!/usr/bin/env python3
import json,os,sys
from pathlib import Path
if sys.argv[1:]==['install']:sys.exit(255 if os.environ['MOCK_CASE']=='probe-fails' else 253)
p=Path(sys.argv[-1]);Path(os.environ['MOCK_LOG']).write_text(json.dumps({'args':sys.argv[1:],'payload':p.read_bytes().hex()}))
sys.exit(171 if os.environ['MOCK_CASE']=='helper-fails' else 0)
'''
   for i in range(helpers):
    app=(sysroot/'apps' if system=='roothide' else apps)/str(i)/'TrollStore.app' if system!='lite' else root/'lite'
    app.mkdir(parents=True,exist_ok=True);(app/'Info.plist').write_text('fixture');executable(app/'trollstorehelper',helper)
   executable(commands/'id','#!/bin/sh\nprintf "%s\\n" "${MOCK_UID:-0}"\n')
   executable(commands/'stat','#!/bin/sh\nprintf "0\\n"\n')
   executable(commands/'curl','''#!/usr/bin/env python3
import os,sys
from pathlib import Path
if os.environ['MOCK_CASE']=='download-fails':sys.exit(22)
a=sys.argv[1:];p=Path(a[a.index('--output')+1]);data=bytes.fromhex(os.environ['MOCK_PAYLOAD'])
if os.environ['MOCK_CASE']=='wrong-size':data+=b'x'
if os.environ['MOCK_CASE']=='wrong-hash':data=bytes([data[0]^1])+data[1:]
p.write_bytes(data)
''')
   executable(commands/'sha256sum','''#!/usr/bin/env python3
import hashlib,sys
from pathlib import Path
print(hashlib.sha256(Path(sys.argv[1]).read_bytes()).hexdigest()+'  '+sys.argv[1])
''')
   executable(commands/'jbroot','''#!/usr/bin/env python3
import os,sys,shutil
from pathlib import Path
p=Path(os.environ['MOCK_NATIVE']);shutil.copyfile(sys.argv[1],p);print(p)
''')
   script=root/'postinst';script.write_text(template)
   env=dict(os.environ,MOCK_CASE=case,MOCK_LOG=str(log),MOCK_UID='501' if case=='nonroot' else '0',MOCK_PAYLOAD=PAYLOAD.hex(),MOCK_NATIVE=str(root/'native-payload.ipa'))
   result=subprocess.run(['/bin/sh',str(script),'configure'],env=env,capture_output=True,text=True,timeout=10)
   record=json.loads(log.read_text()) if log.exists() else None
   leftovers=list(root.glob('download.*'))
   return result,record,leftovers
 def test_success_only_invokes_official_install_custom(self):
  r,call,left=self.run_installer();self.assertEqual(r.returncode,0,r.stderr);self.assertEqual(call['args'][:2],['install','custom']);self.assertEqual(call['payload'],PAYLOAD.hex());self.assertEqual(left,[])
 def test_roothide_uses_native_ipa_path(self):
  r,call,left=self.run_installer(system='roothide');self.assertEqual(r.returncode,0,r.stderr);self.assertTrue(call['args'][2].endswith('native-payload.ipa'));self.assertEqual(left,[])
 def test_lite_helper(self):
  r,call,_=self.run_installer(system='lite');self.assertEqual(r.returncode,0,r.stderr);self.assertIsNotNone(call)
 def test_missing_trollstore_is_failure(self):
  r,call,_=self.run_installer(helpers=0);self.assertNotEqual(r.returncode,0);self.assertIsNone(call);self.assertIn('not found',r.stderr)
 def test_ambiguous_helpers_fail_closed(self):
  r,call,_=self.run_installer(helpers=2);self.assertNotEqual(r.returncode,0);self.assertIsNone(call)
 def test_nonroot_cannot_install(self):
  r,call,_=self.run_installer(case='nonroot');self.assertNotEqual(r.returncode,0);self.assertIsNone(call)
 def test_failed_download_does_not_install(self):
  r,call,left=self.run_installer(case='download-fails');self.assertNotEqual(r.returncode,0);self.assertIsNone(call);self.assertEqual(left,[])
 def test_wrong_size_does_not_install(self):
  r,call,left=self.run_installer(case='wrong-size');self.assertNotEqual(r.returncode,0);self.assertIsNone(call);self.assertEqual(left,[])
 def test_wrong_hash_does_not_install(self):
  r,call,left=self.run_installer(case='wrong-hash');self.assertNotEqual(r.returncode,0);self.assertIsNone(call);self.assertEqual(left,[])
 def test_failed_root_helper_preflight_does_not_install(self):
  r,call,left=self.run_installer(case='probe-fails');self.assertNotEqual(r.returncode,0);self.assertIsNone(call);self.assertIn('no-install preflight',r.stderr);self.assertEqual(left,[])
 def test_trollstore_failure_not_reported_successful(self):
  r,call,left=self.run_installer(case='helper-fails');self.assertNotEqual(r.returncode,0);self.assertIsNotNone(call);self.assertIn('returned 171',r.stderr);self.assertNotIn('installation complete',r.stdout);self.assertEqual(left,[])
if __name__=='__main__':unittest.main()
