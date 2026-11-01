# ZGTA 5 historical installer changelogs

These are the original pre-1.x installer/build identifiers, preserved for recovery and provenance. They are not current product-version labels. Verification status describes each entry at the time it was written; later results may supersede it.

Current iOS product: **ZGTA 5 — 1.1 beta 1** (`1.1~beta1`, unchanged app Build 109). Browser/Mac **1.2** is a separate update, without a new iOS app.

## TrollStore

### Installer 0.109-2 / App Build 109
ZGTA V 2.0 beta 4 / Build 109 adds proximity voice between iPhone and browser players using the existing microphone and speaker controls. Voices get progressively quieter with distance and are silent beyond 35 metres, with smooth changes while moving. The owner confirmed installation/data, speech both ways, distance reduction/range silence/return and microphone mute on iPhone and Mac. Stable installer 0.109-2 delivers that unchanged tested IPA from the public release; its public metadata wrapper was not separately phone-tested. AppSync remains experimental and not device-tested. Bluetooth/interruption routes, Windows/Android/Linux and Apple Silicon execution remain untested.

Earlier entries retain their historical meaning.

### TrollStore installer0.107-3 / App107
TrollStore installer0.107-3 shows concise progress on successful installation and retains full helper output on failure. The owner confirmed clean installation, GTA relaunch and existing data on the RootHide setup. It installs the same Build107 app. AppSync remains0.107-2 and experimental.

### Installer0.107-2 / App Build107
ZGTA V 2.0 beta 3 / Build107 preserves the corrected building rendering and separates Automatic, Standard and Reduced memory management from graphics presets, resolution and FPS. The owner confirmed Build107 graphics, launched Mac DMG107.1, connected Mac/iPhone, and confirmed automatic empty-room discovery on both after the relay1.1 update. The iPhone performance report is a hot driving run, not a measured speedup. Physical3GB/A13 gains remain unmeasured; Windows/Android/Linux and AppleSilicon execution remain untested. Installer0.107-2 changes release metadata only and pins the exact same Build107 IPA as0.107-1. AppSync remains experimental.

Earlier changelog entries retain their original verification status.

### Installer 0.107-1 / App Build 107
Build 107 audits low-memory behavior while preserving the working Build106 rendering fix. Reduced memory bounds optional prefetch to four jobs/one speculative job and trims only completed idle GPU storage earlier; Standard and higher-memory settings are unchanged. Memory management stays independent of graphics presets, resolution and FPS. iOS Find Lobby icons and preset descriptions are corrected; simulator layouts were inspected on SE2020 and iPhone15Pro sizes. Performance reports distinguish the applied memory mode from a pending saved choice. Focused source, native, signature, icon and portable checks pass. The owner confirmed the Build106 parking/highway scene stable; exact Build107 iPhone/Mac performance and graphical tests remain pending. No measured FPS, heat or physical SE2020 improvement is claimed.

### Installer 0.106-1 / App Build 106
Build 106 corrects a fade-mask cleanup leak in native and browser rendering. Nine engine paths inline EndDraw and previously bypassed the fallback-mask reset; the next ordinary draw could inherit partial coverage. Native and actual original WASM regression fixtures reproduce the old leak and pass with the correction. The Build 105 capture had no sampled shadow/upload mismatches, cache evictions or memory clamps; it does not establish a cache shortage. Memory profiles, cache limits, saves and multiplayer protocol are unchanged. Exact iPhone/Mac visual acceptance remains pending; no complete scene fix or FPS gain is claimed.

### Installer 0.105-1 / App Build 105
Build 105 corrects native CPU constant-buffer shadow copies and adds an explicit bounded rendering capture. Build 104 still flickers in owner testing; scene causality is not established. Capture rendering issue is available in Performance check; save that report after rotating the camera. Normal play/FPS tests keep capture off. Memory profiles, cache budgets, saves, networking and browser rendering bytes are unchanged. Exact phone scene verification remains pending; no FPS gain or complete scene fix is claimed.

### Installer 0.104-1 / App Build 104
Build 104 corrects stale fade state after original game resets. All 12 authenticated engine-state sequences pass; retained Build 103 fails seven expected cases. Shader code, memory settings, cooling, saves and networking are unchanged. Owner testing rejected Build 103 for the flickering-building scene. Exact Build 104 iPhone/Mac visual acceptance remains pending; no complete scene fix or FPS gain is claimed.

### Installer 0.103-1 / App Build 103
Build103 corrects the missing-technique fade fallback on Metal and WebGPU: it preserves inversion and the original complementary 2x2 pixel masks. Automated source, shader and package checks pass. Exact Build103 iPhone/Mac visual gameplay acceptance remains pending; no measured FPS gain or complete missing-building fix is claimed. Memory settings, thermal protection, saves and multiplayer protocol are unchanged.

### Installer 0.102-1 / App Build 102
Build102 is a system-audit candidate: safer save restore and individual recovery, dirty multiplayer profile checkpoints, lower nested-archive parsing copies, directory descriptor leak and Metal allocation failure handling. Browser LAN local mod snapshots and exact running-host identity are included in matching browser packages. Local checks pass; physical iPhone/Mac gameplay, sustained heat and paired mod visibility remain pending. No FPS gain or SE missing-world fix is claimed.

### Installer 0.101-1 / App Build 101
- Separate memory management from presets and display controls.
- Improve packed texture decoding, asset wakeups and completed-buffer cleanup.
- Correct pipeline wait and depth-proxy diagnostics.
- Group iOS settings into presets, display and memory.
- Retain previous packages, game files, saves and installer templates.
- Physical Build 101 gameplay and heat testing remain pending.

### Installer 0.100-1 / App Build 100
- Isolate low-memory native protection below 3400 MiB RAM.
- Preserve modern-device settings and memory policy.
- Add buffer occupancy and texture-failure diagnostics.
- Retain previous packages, game files, saves and installer behavior.
- Physical Build100 phone/SE gameplay testing remains pending.

### Installer 0.99-1 / App Build 99
- Apply current thermal protection before engine loading.
- Trim completed idle GPU caches under memory pressure.
- Add local one-second renderer and streaming diagnostics to explicit performance checks.
- Preserve saved preferences, game files and existing installation behavior.
- Physical phone gameplay and thermal results pending.

### Installer 0.98-1 / App Build 98
- Share duplicate shader constant storage.
- Correct night-light upload hints and missing ped fade coverage.
- Compile first-use native fade variants in the background.
- Install the verified Build98 IPA; gameplay and thermal results pending.

### Installer 0.97-1 / App Build 97
- Improve nearby LAN lobby discovery, retries and refresh.
- Install the verified Build97 IPA.
- Phone installation, discovery and gameplay testing pending.

### Installer 0.96-1 / App Build 96
- Apply the revised bounded host-broadcast capacity fix.
- Pin the exact Build96 IPA by size and SHA-256.
- Keep existing installer/helper behavior and previous package versions.
- Physical phone and paired gameplay retest pending.

### Installer 0.91-1 / App Build 91
- Fix opening archives found by a folder scan.

### Installer 0.90-1 / App Build 90
- Improve game-folder scanning and use English throughout the menus.

### Installer 0.88-2
- Fix TrollStore detection on RootHide.

### Installer 0.88-1
- Initial Sileo installer.

## AppSync

### Installer 0.109-2 / App Build 109
ZGTA V 2.0 beta 4 / Build 109 adds proximity voice between iPhone and browser players using the existing microphone and speaker controls. Voices get progressively quieter with distance and are silent beyond 35 metres, with smooth changes while moving. The owner confirmed installation/data, speech both ways, distance reduction/range silence/return and microphone mute on iPhone and Mac. Stable installer 0.109-2 delivers that unchanged tested IPA from the public release; its public metadata wrapper was not separately phone-tested. AppSync remains experimental and not device-tested. Bluetooth/interruption routes, Windows/Android/Linux and Apple Silicon execution remain untested.

Earlier entries retain their historical meaning.

### Installer0.107-2 / App Build107
ZGTA V 2.0 beta 3 / Build107 preserves the corrected building rendering and separates Automatic, Standard and Reduced memory management from graphics presets, resolution and FPS. The owner confirmed Build107 graphics, launched Mac DMG107.1, connected Mac/iPhone, and confirmed automatic empty-room discovery on both after the relay1.1 update. The iPhone performance report is a hot driving run, not a measured speedup. Physical3GB/A13 gains remain unmeasured; Windows/Android/Linux and AppleSilicon execution remain untested. Installer0.107-2 changes release metadata only and pins the exact same Build107 IPA as0.107-1. AppSync remains experimental.

Earlier changelog entries retain their original verification status.

### Installer 0.107-1 / App Build 107
Build 107 audits low-memory behavior while preserving the working Build106 rendering fix. Reduced memory bounds optional prefetch to four jobs/one speculative job and trims only completed idle GPU storage earlier; Standard and higher-memory settings are unchanged. Memory management stays independent of graphics presets, resolution and FPS. iOS Find Lobby icons and preset descriptions are corrected; simulator layouts were inspected on SE2020 and iPhone15Pro sizes. Performance reports distinguish the applied memory mode from a pending saved choice. Focused source, native, signature, icon and portable checks pass. The owner confirmed the Build106 parking/highway scene stable; exact Build107 iPhone/Mac performance and graphical tests remain pending. No measured FPS, heat or physical SE2020 improvement is claimed.

### Installer 0.106-1 / App Build 106
Build 106 corrects a fade-mask cleanup leak in native and browser rendering. Nine engine paths inline EndDraw and previously bypassed the fallback-mask reset; the next ordinary draw could inherit partial coverage. Native and actual original WASM regression fixtures reproduce the old leak and pass with the correction. The Build 105 capture had no sampled shadow/upload mismatches, cache evictions or memory clamps; it does not establish a cache shortage. Memory profiles, cache limits, saves and multiplayer protocol are unchanged. Exact iPhone/Mac visual acceptance remains pending; no complete scene fix or FPS gain is claimed.

### Installer 0.105-1 / App Build 105
Build 105 corrects native CPU constant-buffer shadow copies and adds an explicit bounded rendering capture. Build 104 still flickers in owner testing; scene causality is not established. Capture rendering issue is available in Performance check; save that report after rotating the camera. Normal play/FPS tests keep capture off. Memory profiles, cache budgets, saves, networking and browser rendering bytes are unchanged. Exact phone scene verification remains pending; no FPS gain or complete scene fix is claimed.

### Installer 0.104-1 / App Build 104
Build 104 corrects stale fade state after original game resets. All 12 authenticated engine-state sequences pass; retained Build 103 fails seven expected cases. Shader code, memory settings, cooling, saves and networking are unchanged. Owner testing rejected Build 103 for the flickering-building scene. Exact Build 104 iPhone/Mac visual acceptance remains pending; no complete scene fix or FPS gain is claimed.

### Installer 0.103-1 / App Build 103
Build103 corrects the missing-technique fade fallback on Metal and WebGPU: it preserves inversion and the original complementary 2x2 pixel masks. Automated source, shader and package checks pass. Exact Build103 iPhone/Mac visual gameplay acceptance remains pending; no measured FPS gain or complete missing-building fix is claimed. Memory settings, thermal protection, saves and multiplayer protocol are unchanged.

### Installer 0.102-1 / App Build 102
Build102 is a system-audit candidate: safer save restore and individual recovery, dirty multiplayer profile checkpoints, lower nested-archive parsing copies, directory descriptor leak and Metal allocation failure handling. Browser LAN local mod snapshots and exact running-host identity are included in matching browser packages. Local checks pass; physical iPhone/Mac gameplay, sustained heat and paired mod visibility remain pending. No FPS gain or SE missing-world fix is claimed.

### Installer 0.101-1 / App Build 101
- Separate memory management from presets and display controls.
- Improve packed texture decoding, asset wakeups and completed-buffer cleanup.
- Correct pipeline wait and depth-proxy diagnostics.
- Group iOS settings into presets, display and memory.
- Retain previous packages, game files, saves and installer templates.
- Physical Build 101 gameplay and heat testing remain pending.

### Installer 0.100-1 / App Build 100
- Isolate low-memory native protection below 3400 MiB RAM.
- Preserve modern-device settings and memory policy.
- Add buffer occupancy and texture-failure diagnostics.
- Retain previous packages, game files, saves and installer behavior.
- Physical Build100 phone/SE gameplay testing remains pending.

### Installer 0.99-1 / App Build 99
- Apply current thermal protection before engine loading.
- Trim completed idle GPU caches under memory pressure.
- Add local one-second renderer and streaming diagnostics to explicit performance checks.
- Preserve saved preferences, game files and existing installation behavior.
- Physical phone gameplay and thermal results pending.

### Installer 0.98-1 / App Build 98
- Share duplicate shader constant storage.
- Correct night-light upload hints and missing ped fade coverage.
- Compile first-use native fade variants in the background.
- Install the verified Build98 IPA; gameplay and thermal results pending.

### Installer 0.97-1 / App Build 97
- Improve nearby LAN lobby discovery, retries and refresh.
- Install the verified Build97 IPA.
- Phone installation, discovery and gameplay testing pending.

### Installer 0.96-1 / App Build 96
- Apply the revised bounded host-broadcast capacity fix.
- Pin the exact Build96 IPA by size and SHA-256.
- Keep existing installer/helper behavior and previous package versions.
- Physical phone and paired gameplay retest pending.

### Installer 0.91-1 / App Build 91
- Fix opening archives found by a folder scan.

### Installer 0.90-1 / App Build 90
- Improve game-folder scanning and use English throughout the menus.

### Installer 0.88-1
- Initial experimental rootful AppSync installer.
