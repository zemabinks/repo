# Zema's Repo

Add this source to Sileo: `https://zemabinks.github.io/repo/`

This is a general source for Zema's iOS tweaks, apps and ports. The first package is
RelayRace RootHide `1.2` for compatible RootHide devices. This package updates metadata and Sileo depiction while preserving the confirmed 20.1 runtime payload and installer scripts.
Original RelayRace by shalamand3r; RootHide support and port by ZEMA.

Current package size: 12,092 bytes. SHA-256: `c2d14fea1cb4919fc6b40a57c58b084a4e2703fdedebec8ad2e4d2926120b914`.

## App downloads

### ZGTA V — Build91 archive-access candidate

[Download the TrollStore IPA](https://github.com/zemabinks/repo/releases/download/zgta-v-build-91/ZGTA-V-Build91-Archive-Access-TrollStore.ipa) · [Release notes and Sileo installers](https://github.com/zemabinks/repo/releases/tag/zgta-v-build-91)

By **zema**. Build90's supplied phone logs confirm installation and folder scanning work, but a Files-provider archive fails to open with **Operation not permitted**. Build91 keeps each discovered archive with its original folder grant, coordinates the actual content reads and improves read-error messages. Keep the existing app, game files, archives and saves.

Refresh this source in Sileo and update **ZGTA V (TrollStore installer) to0.91-1** with your existing compatible TrollStore or TrollStore Lite setup. No AppSync dependency is needed. The native helper interface is unchanged; exact IPA size and SHA-256 are checked. Earlier indexed wrapper versions remain available to cached Sileo selections.

Local ARM64 Release/package/signature/CRC and resource checks pass. Actual macOS coordinated ZIP/split-ZIP reads, writer exclusion/release, cancellation and archive/unrelated-save preservation pass. **Three current Simulator UI cases pass**, including the original parent-grant handoff. Preview engine/download/install adapters are inert; screenshots use temporary fixtures. **Actual Build91 phone/provider/RAR testing is pending.** No new gameplay, app-data upgrade/save retention, multiplayer, performance or reboot-persistence claim is made. The theme, icons, English-only interface, game/artwork/shader resources and existing save compatibility are retained.

The separate AppSync0.91-1 wrapper remains experimental for compatible ARM64 rootful jailbreaks, iOS15.0–18.2, using official dependencies from https://cydia.akemi.ai/. It is not a RootHide/rootless conversion. Fresh dependency availability and actual device results remain unverified.

[Installation guide](docs/zgta-v-installation.md). Removing either small wrapper leaves the app/data in place. Your own matching game files are required. The clean public2.0/platform audit remains in progress.

IPA size: **90,975,818 bytes**. SHA-256: `f54b0172e6d9d348295af4ecf117c71817284eaca09cbf9e09aa130edb6f9802`.

Machine-readable download: [`downloads/zgta-v.json`](downloads/zgta-v.json). [Historical Build88 installation evidence](downloads/zgta-v-device-install.json); Build90 upgrade/scan observations and limitations are described in the current release verification.

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

