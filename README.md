# Zema's Repo

Add this source to Sileo: `https://zemabinks.github.io/repo/`

This is a general source for Zema's iOS tweaks, apps and ports. The first package is
RelayRace RootHide `1.2` for compatible RootHide devices. This package updates metadata and Sileo depiction while preserving the confirmed 20.1 runtime payload and installer scripts.
Original RelayRace by shalamand3r; RootHide support and port by ZEMA.

Current package size: 12,092 bytes. SHA-256: `c2d14fea1cb4919fc6b40a57c58b084a4e2703fdedebec8ad2e4d2926120b914`.

## App downloads

### ZGTA V — Build 90 candidate

[Download the TrollStore IPA](https://github.com/zemabinks/repo/releases/download/zgta-v-build-90/ZGTA-V-Build90-GameFiles-English-TrollStore.ipa) · [Release notes and Sileo installers](https://github.com/zemabinks/repo/releases/tag/zgta-v-build-90)

By **zema**. English-only UI, repaired Game Files folder discovery/rechecks, retained folder access for extraction, and archive-preserving unpacking by default. Build90 additionally clears stale Ready for an unavailable external folder. Its UI is byte-identical to89; that Simulator evidence is reused alongside the new folder regression. The approved Pure Black layout, V+Z icon, saved settings, saves and game resources are retained. Your own game files are required. Update the existing app without deleting its data.

Refresh this source in Sileo and install/update **ZGTA V (TrollStore installer) 0.90-1** for an existing compatible TrollStore or TrollStore Lite setup. No AppSync dependency is needed. This retains the successful0.88-2 helper interface and pins the new89 IPA. **Build90 phone installation and actual Files-provider access are pending.** Build88 installation and launcher opening were confirmed separately on iPhone15Pro/iOS17.0/TrollStore2.1.1/RootHide.

The separate **AppSync installer0.90-1** remains experimental: compatible ARM64 rootful jailbreaks on iOS15.0–18.2 only, with official AppSync Unified116.0+ and appinst2.1.1+ from https://cydia.akemi.ai/. It is not a RootHide/rootless conversion. Its dependency server timed out during earlier checks; fresh dependency downloads and device results remain unverified.

[Installation guide](docs/zgta-v-installation.md). Both wrappers verify the exact IPA size/SHA-256 and wait for the native installer. Removing a wrapper leaves the game/data installed; no force migration or game uninstall is used.

Local native build/signature/entitlements/identity/resources/CRC, discovery and English/save/control regressions, real Mac ZIP/split-ZIP extraction and two actual Simulator UI cases pass. Phone Files-provider grants, real app-data upgrades, gameplay, two-device multiplayer, performance and reboot persistence remain pending for89. This candidate does not complete the separate public2.0/platform audit.

Size: **90,970,670 bytes**. SHA-256: `e40926d2f5b2fa6964b8400eba76ed782b39c48e0800ed7bfc56c0f6cdc06edd`.

Machine-readable download: [`downloads/zgta-v.json`](downloads/zgta-v.json). [Previous confirmed installation evidence — Build88](downloads/zgta-v-device-install.json).

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
