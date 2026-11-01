# ZGTA 5 beta 4 / Build 109 in Sileo

Add `https://zemabinks.github.io/repo/`, refresh, and install **ZGTA 5 (TrollStore installer) 1.1~beta1** through your existing compatible TrollStore. Keep the existing app and game data. The package verifies the exact IPA size and SHA-256 and updates the same application identity. It does not install TrollStore.

ZGTA 5 1.1 beta 1 / Build 109 adds proximity voice between iPhone and browser players using the existing microphone and speaker controls. Voices get progressively quieter with distance and are silent beyond 35 metres, with smooth changes while moving. The owner confirmed installation/data, speech both ways, distance reduction/range silence/return and microphone mute on iPhone and Mac. Stable installer 1.1~beta1 delivers that unchanged tested IPA from the public release; its public metadata wrapper was not separately phone-tested. AppSync remains experimental and not device-tested. Bluetooth/interruption routes, Windows/Android/Linux and Apple Silicon execution remain untested.

[Current installation guide](https://github.com/zemabinks/ZGTA-V/blob/main/docs/START-HERE.md) · [All platform downloads](https://github.com/zemabinks/ZGTA-V/releases/tag/v1.1-beta.1)

## Historical installer notes

# Install ZGTA 5 with Sileo

**Requires iOS / iPadOS 15.0 or later**, a compatible installation method and your own matching prepared game files.

[Full installation guide](https://github.com/zemabinks/ZGTA-V/blob/main/docs/START-HERE.md) · [Other iOS sideloaders](https://github.com/zemabinks/ZGTA-V/blob/main/docs/IOS-SIDELOADING.md) · [Mods, graphics & multiplayer](https://github.com/zemabinks/ZGTA-V/blob/main/docs/PLAY-GUIDE.md)

## TrollStore / TrollStore Lite

1. Make sure compatible TrollStore / TrollStore Lite is already installed. The app's iOS minimum does not mean TrollStore supports every later iOS version.
2. In Sileo → Sources, add `https://zemabinks.github.io/repo/` and refresh.
3. Install **ZGTA 5 (TrollStore installer)**, version **1.1~beta1**.
4. Open **ZGTA 5 → Game files** and choose your prepared folder or archive. Follow the [game-file instructions](https://github.com/zemabinks/ZGTA-V/blob/main/docs/START-HERE.md#required-game-folder).

To update, install over the existing app. Do not delete the app or its data first. Removing the small Sileo package leaves ZGTA 5 installed.

If Sileo shows Reinstall, cannot find the package or reports **Install Identifier Mismatch**, clear the queued attempt, refresh Sources and reopen the package. If the helper cannot be found, check TrollStore or install the [same IPA](https://github.com/zemabinks/repo/releases/download/zgta-v-build-107/ZGTA-V-Build107-Memory-UI-Audit-TrollStore.ipa) manually through it.

## AppSync — experimental

For compatible **ARM64 rootful jailbreaks on iOS 15.0–18.2** without TrollStore. This installer is **not for RootHide or rootless**. Actual installation and gameplay have not been tested.

1. Add the official AppSync source, `https://cydia.akemi.ai/`, and Zema's Repo in Sileo.
2. Select **ZGTA 5 (AppSync installer - experimental)**.
3. Check the dependencies: **AppSync Unified 116.0+**, **appinst 2.1.1+**, curl and coreutils. Let Sileo resolve and configure them.
4. Install, then try opening ZGTA 5 with the compatible jailbreak active. Report the exact error if it fails.

Do not install both ZGTA 5 installer packages. The AppSync installer will not replace a detected TrollStore-managed copy. Removing either installer package leaves the app/data in place.

Fresh downloads from the official dependency server could not be verified during the last check. If Sileo cannot fetch the dependencies, installation cannot proceed. AppSync does not guarantee this game's memory needs or TrollStore-style persistence. Do not remove a working app to test it.

## Sideloadly / AltStore Classic

The same `.ipa` is the input for these signing tools; use the [sideloading guide](https://github.com/zemabinks/ZGTA-V/blob/main/docs/IOS-SIDELOADING.md) for steps and limits. These ZGTA 5 routes remain experimental. Use `.ipa`, not a Sileo `.deb` or TrollStore `.tipa`.

## Remote multiplayer

Follow [Remote play with Tailscale](https://github.com/zemabinks/ZGTA-V/blob/main/docs/REMOTE-PLAY.md) for phone/PC downloads, access invitations and step-by-step hosting/joining.

## Downloads and support

[Build 107](https://github.com/zemabinks/repo/releases/tag/zgta-v-build-107) contains a historical owner-approved beta 3 IPA, installers and checksums. ZGTA 5 2.0 beta 3 / Build107 preserves the corrected building rendering and separates Automatic, Standard and Reduced memory management from graphics presets, resolution and FPS. The owner confirmed Build107 graphics, launched Mac DMG107.1, connected Mac/iPhone, and confirmed automatic empty-room discovery on both after the relay1.1 update. The iPhone performance report is a hot driving run, not a measured speedup. Physical3GB/A13 gains remain unmeasured; Windows/Android/Linux and AppleSilicon execution remain untested. TrollStore installer 0.107-3 summarizes successful helper output and retains full failure diagnostics while installing the same Build 107 IPA. AppSync remains experimental. Updating through either installer preserves existing app data.

If installation fails, share the exact Sileo error. For an in-app problem, use **Settings → Saves & support → Share log**. Review personal paths and addresses before posting; do not upload game files or private saves.

## Installer0.107-3

TrollStore installer0.107-3 shows concise progress on successful installation and retains full helper output on failure. The owner confirmed clean installation, GTA relaunch and existing data on the RootHide setup. It installs the same Build107 app. AppSync remains0.107-2 and experimental. Unrelated package warnings are unaffected.
