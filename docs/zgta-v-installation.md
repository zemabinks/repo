# Install ZGTA V with Sileo

**Requires iOS / iPadOS 15.0 or later**, a compatible installation method and your own matching prepared game files.

[Full installation guide](https://github.com/zemabinks/ZGTA-V/blob/main/docs/START-HERE.md) · [Other iOS sideloaders](https://github.com/zemabinks/ZGTA-V/blob/main/docs/IOS-SIDELOADING.md) · [Mods, graphics & multiplayer](https://github.com/zemabinks/ZGTA-V/blob/main/docs/PLAY-GUIDE.md)

## TrollStore / TrollStore Lite

1. Make sure compatible TrollStore / TrollStore Lite is already installed. The app's iOS minimum does not mean TrollStore supports every later iOS version.
2. In Sileo → Sources, add `https://zemabinks.github.io/repo/` and refresh.
3. Install **ZGTA V (TrollStore installer)**, version **0.96-1**.
4. Open **ZGTA V → Game files** and choose your prepared folder or archive. Follow the [game-file instructions](https://github.com/zemabinks/ZGTA-V/blob/main/docs/START-HERE.md#required-game-folder).

To update, install over the existing app. Do not delete the app or its data first. Removing the small Sileo package leaves ZGTA V installed.

If Sileo shows Reinstall, cannot find the package or reports **Install Identifier Mismatch**, clear the queued attempt, refresh Sources and reopen the package. If the helper cannot be found, check TrollStore or install the [same IPA](https://github.com/zemabinks/repo/releases/download/zgta-v-build-96/ZGTA-V-Build96-HostCapacity-TrollStore.ipa) manually through it.

## AppSync — experimental

For compatible **ARM64 rootful jailbreaks on iOS 15.0–18.2** without TrollStore. This installer is **not for RootHide or rootless**. Actual installation and gameplay have not been tested.

1. Add the official AppSync source, `https://cydia.akemi.ai/`, and Zema's Repo in Sileo.
2. Select **ZGTA V (AppSync installer - experimental)**.
3. Check the dependencies: **AppSync Unified 116.0+**, **appinst 2.1.1+**, curl and coreutils. Let Sileo resolve and configure them.
4. Install, then try opening ZGTA V with the compatible jailbreak active. Report the exact error if it fails.

Do not install both ZGTA V installer packages. The AppSync installer will not replace a detected TrollStore-managed copy. Removing either installer package leaves the app/data in place.

Fresh downloads from the official dependency server could not be verified during the last check. If Sileo cannot fetch the dependencies, installation cannot proceed. AppSync does not guarantee this game's memory needs or TrollStore-style persistence. Do not remove a working app to test it.

## Sideloadly / AltStore Classic

The same `.ipa` is the input for these signing tools; use the [sideloading guide](https://github.com/zemabinks/ZGTA-V/blob/main/docs/IOS-SIDELOADING.md) for steps and limits. These ZGTA V routes remain experimental. Use `.ipa`, not a Sileo `.deb` or TrollStore `.tipa`.

## Remote multiplayer

Follow [Remote play with Tailscale](https://github.com/zemabinks/ZGTA-V/blob/main/docs/REMOTE-PLAY.md) for phone/PC downloads, access invitations and step-by-step hosting/joining.

## Downloads and support

[ZGTA V 2.0 beta](https://github.com/zemabinks/ZGTA-V/releases/tag/host-capacity-candidate-96) has the IPA, browser packages and source. [Native Build 96](https://github.com/zemabinks/repo/releases/tag/zgta-v-build-96) contains Sileo installers, checksums and technical verification. Native version **2.0 / Build 96** includes the revised bounded host-broadcast capacity fix. Local build/package checks and Chrome world entry/reconnect pass; physical iPhone96, paired iPhone/browser and small-job tests remain pending. Existing icons, archive access, game files and saves are preserved.

If installation fails, share the exact Sileo error. For an in-app problem, use **Settings → Saves & support → Share log**. Review personal paths and addresses before posting; do not upload game files or private saves.
