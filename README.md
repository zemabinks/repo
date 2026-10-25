# Zema's Repo

Add this source to Sileo: `https://zemabinks.github.io/repo/`

This is a general source for Zema's iOS tweaks, apps and ports. The first package is
RelayRace RootHide `1.2` for compatible RootHide devices. This package updates metadata and Sileo depiction while preserving the confirmed 20.1 runtime payload and installer scripts.
Original RelayRace by shalamand3r; RootHide support and port by ZEMA.

Current package size: 12,092 bytes. SHA-256: `c2d14fea1cb4919fc6b40a57c58b084a4e2703fdedebec8ad2e4d2926120b914`.

## App downloads

### ZGTA V — Build 88 candidate

[Download the TrollStore IPA](https://github.com/zemabinks/repo/releases/download/zgta-v-build-88/ZGTA-V-Build88-LobbyFavorites-TrollStore.ipa) · [Release notes](https://github.com/zemabinks/repo/releases/tag/zgta-v-build-88)

By **zema**. Pure Black launcher, fully clickable Home cards and separate Online / ♥ Favorites lobby views. Install with a compatible TrollStore setup and your own game files. This is an IPA download, not a Sileo `.deb` package. Install updates over the existing app and keep its data.

Simulator UI, 38 logic regressions and local ARM64 package checks pass. Physical iPhone acceptance and live two-device gameplay remain pending. This is a candidate prerelease, not a claim of compatibility with every jailbroken device.

Size: **90,997,632 bytes**. SHA-256: `4dd7a1135c490747b3089f332c6f7573b1a70c8f87ccf4a4430123d8b0488d9d`.

Machine-readable download: [`downloads/zgta-v.json`](downloads/zgta-v.json).

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
