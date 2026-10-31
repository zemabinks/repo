# Zema's Repo

Add this source to Sileo: `https://zemabinks.github.io/repo/`

This is a general source for Zema's iOS tweaks, apps and ports. The first package is
RelayRace RootHide `1.2` for compatible RootHide devices. This package updates metadata and Sileo depiction while preserving the confirmed 20.1 runtime payload and installer scripts.
Original RelayRace by shalamand3r; RootHide support and port by ZEMA.

Current package size: 12,092 bytes. SHA-256: `c2d14fea1cb4919fc6b40a57c58b084a4e2703fdedebec8ad2e4d2926120b914`.

## App downloads

### ZGTA V — 2.0 beta 3 · Build 107

By **zema**. Solo Story, Free Roam and Private Multiplayer.

**Requires iOS / iPadOS 15.0 or later** and your own matching prepared game files. TrollStore / TrollStore Lite must support your exact device and iOS version.

[Download IPA](https://github.com/zemabinks/repo/releases/download/zgta-v-build-107/ZGTA-V-Build107-Memory-UI-Audit-TrollStore.ipa) · [Other platform downloads](https://github.com/zemabinks/ZGTA-V/releases/tag/v2.0.0-beta.3) · [Installation guide](https://github.com/zemabinks/ZGTA-V/blob/main/docs/START-HERE.md) · [Mods, graphics & multiplayer](https://github.com/zemabinks/ZGTA-V/blob/main/docs/PLAY-GUIDE.md) · [Remote play with Tailscale](https://github.com/zemabinks/ZGTA-V/blob/main/docs/REMOTE-PLAY.md)

In Sileo, refresh this source and install **ZGTA V (TrollStore installer)**, version **0.107-2**, with existing compatible TrollStore. Keep the app installed when updating. Removing the installer package leaves the app and data in place.

[Sideloadly and AltStore Classic](https://github.com/zemabinks/ZGTA-V/blob/main/docs/IOS-SIDELOADING.md) can be tried with the same IPA; ZGTA V has not been tested through them. The separate AppSync package is an untested option for compatible ARM64 rootful jailbreaks on iOS 15.0–18.2, not RootHide/rootless. See [Sileo installation](docs/zgta-v-installation.md).

[Download metadata](downloads/zgta-v.json) · [Checksums and verification](https://github.com/zemabinks/repo/releases/tag/zgta-v-build-107)

ZGTA V 2.0 beta 3 / Build107 preserves the corrected building rendering and separates Automatic, Standard and Reduced memory management from graphics presets, resolution and FPS. The owner confirmed Build107 graphics, launched Mac DMG107.1, connected Mac/iPhone, and confirmed automatic empty-room discovery on both after the relay1.1 update. The iPhone performance report is a hot driving run, not a measured speedup. Physical3GB/A13 gains remain unmeasured; Windows/Android/Linux and AppleSilicon execution remain untested. Installer0.107-2 changes release metadata only and pins the exact same Build107 IPA as0.107-2. AppSync remains experimental.

## GitHub Releases

The [Releases page](https://github.com/zemabinks/repo/releases) provides a
downloadable `.deb` and `SHA256SUMS.txt` for the latest published tweak. The
current tweak release is [RelayRace 1.2](https://github.com/zemabinks/repo/releases/tag/relayrace-1.2).
Future tweaks can have their own package-specific release tags.

The previous `1.1+roothide.20.1` package remains downloadable from `pool/com.shalamand3r.relayrace_1.1+roothide.20.1_iphoneos-arm64e.deb` (12,108 bytes; SHA-256 `efbec56da598293491ae7ff07d81ecf0596108c30176a11182d122772117d965`).

The Release metadata is signed with an Ed25519 OpenPGP key. Public key:
[`repo-signing-key.asc`](repo-signing-key.asc). Fingerprint:
`369B 9D41 D3BC EA25 20B2 2C2B D9AD 1897 295C 6D05`.

This is the canonical Sileo source. Older v19/v18 packages remain in the
private recovery archive. Installation or upgrade of version 1.2 on a phone
and reboot persistence still need device testing.
