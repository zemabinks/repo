# ZGTA 5 — 1.1 beta 1 in Sileo

Requires iOS / iPadOS 15.0 or later, your own matching prepared game files and a compatible installation method. Sileo package version is `1.1~beta1`; the app remains Build 109. Browser/Mac 1.2 is a separate update, without a replacement iOS app.

## TrollStore / TrollStore Lite

1. Close GTA and keep your existing app and data installed.
2. Add `https://zemabinks.github.io/repo/` in Sileo → Sources and refresh.
3. Install **ZGTA 5 (TrollStore installer) 1.1~beta1** using your existing compatible TrollStore / TrollStore Lite setup.
4. Open the app. For a new installation, select your matching prepared game folder or archive.

The installer verifies the exact IPA size and SHA-256 before updating the existing app. It does not install TrollStore. Removing the small installer package leaves GTA and its data installed.

If the helper is not found, check your TrollStore setup or open the [same IPA](https://github.com/zemabinks/repo/releases/download/zgta-v-build-109/ZGTA-V-Build109-VoiceDistance-TrollStore.ipa) manually through TrollStore. If Sileo has an old queued attempt, clear that attempt, refresh Sources and reopen the package. Do not delete GTA to fix a repository metadata problem.

## AppSync — experimental

For compatible **ARM64 rootful jailbreaks on iOS 15.0–18.2**, using AppSync Unified 116.0+ and appinst 2.1.1+. Not for RootHide or rootless. Installation has not been phone-tested. Use the official dependency source and let Sileo resolve dependencies. Do not install both variants or replace a TrollStore-managed app with AppSync.

[Installation and signing options](https://github.com/zemabinks/ZGTA-V/blob/main/docs/IOS-SIDELOADING.md) · [Game files, updates and troubleshooting](https://github.com/zemabinks/ZGTA-V/blob/main/docs/START-HERE.md)

## Changelog and other platforms

[iOS 1.1 beta 1 notes](https://github.com/zemabinks/ZGTA-V/releases/tag/v1.1-beta.1) · [Browser/Mac 1.2 downloads](https://github.com/zemabinks/ZGTA-V/releases/tag/v1.2) · [Historical installer/build changelogs](zgta-v-changelog-archive.md)

No new FPS, thermal or physical 3 GB-device improvement is claimed. AppSync and Bluetooth/interruption handling remain unverified. [Full verification and remaining limits](https://github.com/zemabinks/ZGTA-V/blob/main/docs/VERIFICATION.md).

For an installation problem, share the exact Sileo error. For an in-app problem, use Settings → Saves & support → Share log. Review personal information before sharing; never upload game files or private saves.
