#!/usr/bin/env python3
"""Render a maintainer-only installer; build it with the existing Linux dpkg-deb."""
import argparse,json,re,shlex,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def stage(destination:Path, flavor="trollstore"):
    assert flavor in ("trollstore", "appsync")
    assert not destination.exists(),destination
    catalog=json.loads((ROOT/'downloads/zgta-v.json').read_text())
    assert re.fullmatch(r'[a-f0-9]{64}',catalog['sha256'])
    assert catalog['download_url']=='https://github.com/zemabinks/repo/releases/download/zgta-v-build-88/'+catalog['file']
    assert catalog['bytes']==90997632 and catalog['build']==88
    destination.mkdir(parents=True);destination.chmod(0o755);control=destination/'DEBIAN';control.mkdir();control.chmod(0o755)
    shutil.copy2(ROOT/f'package-sources/{flavor}-installer/control',control/'control')
    text=(ROOT/f'package-sources/{flavor}-installer/postinst.in').read_text()
    values={'APP_NAME':catalog['name'],'IPA_URL':catalog['download_url'],'SHA256':catalog['sha256'],'BYTES':str(catalog['bytes'])}
    for key,value in values.items():text=text.replace('@'+key+'@',shlex.quote(value))
    assert not re.search(r'@[A-Z_]+@',text)
    (control/'postinst').write_text(text);(control/'postinst').chmod(0o755)
    (control/'control').chmod(0o644)
    return catalog
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('destination',type=Path);parser.add_argument('--flavor',choices=['trollstore','appsync'],default='trollstore');args=parser.parse_args();stage(args.destination,args.flavor)
