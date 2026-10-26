# ZGTA V Build91 — archive-access candidate

By **zema**. Keep your existing app, game files, archives and saves. This guide describes the unchanged native91 component of [public2.0 beta](https://github.com/zemabinks/ZGTA-V/releases/tag/v2.0.0-beta.1); broader device testing remains open.

## Update using compatible TrollStore
1. In Sileo, refresh `https://zemabinks.github.io/repo/`.
2. Open **ZGTA V (TrollStore installer)** and update to **0.91-1**. The wrapper downloads the pinned IPA and uses your existing TrollStore helper; AppSync is not required for this route.
3. Open ZGTA V → Game files, choose the folder containing your archive again, then tap its discovered **Unpack** row.

If Sileo still shows Reinstall or “Install Identifier Mismatch,” clear the queued attempt, refresh Sources and reopen the package. Sileo compares wrapper versions; it does not inspect the installed IPA. Refreshing resolved the owner's earlier mismatch. Both0.90-1 and0.91-1 remain indexed so an earlier selected version can still resolve.

## Why Build91 exists
The owner's Build90 log identifies2.0(90) on iOS17.0: folder scanning works, but reading mirror.rar from a Files-provider folder fails with **Operation not permitted** before extraction. This is a source access failure; the log does not establish archive corruption or insufficient storage. Existing game files did not trigger this particular error.

Build91 pairs the archive and original folder grant, removes an unscoped fallback, coordinates actual file content reads and uses the provider-returned URL. Access is held across multipart extraction and released on success/failure/cancellation. Provider archives are retained; app-owned consumption remains a separately labelled explicit option. No engine resources, saves, settings, theme or signing entitlements change.

## Actual verification and remaining checks
- Local ARM64 Release/package/signature/CRC and unchanged-resource checks pass.
- Actual macOS ZIP/split-ZIP extraction, a separate coordinated writer, cancellation, pre-existing game replacement and source/unrelated save retention pass.
- Three current Simulator UI cases pass, including an external archive's original-grant handoff. Preview engine/download/install adapters are inert and do not prove physical provider access.
-23 local Sileo test methods pass; native installation interfaces are mocked.
- The supplied phone log confirms the earlier Sileo0.88-2 →0.90-1/TrollStore app replacement succeeded. Folder scans are confirmed; archive extraction failed with EPERM.

**The owner confirms the archive workflow now works on the physical phone after the Build91 update.** This is an owner report; no new independent device inventory/log was collected. Do not delete the archive or installed game to troubleshoot. If access is still refused, use **Choose an archive…** for a fresh file grant and share the current log. Gameplay, real save retention during an app update, performance and reboot persistence remain unverified on91. Own matching prepared game files are required; none are bundled.

## Manual download
[Build91 release](https://github.com/zemabinks/repo/releases/tag/zgta-v-build-91) contains the same IPA and checksum. Open it in compatible TrollStore to update the existing app.

Bytes: **90,975,818**
SHA-256: `f54b0172e6d9d348295af4ecf117c71817284eaca09cbf9e09aa130edb6f9802`

Removing the small Sileo wrapper leaves the TrollStore app and its data installed. The wrapper never forces an existing app installed by another method to be overwritten.

## No supported TrollStore setup: AppSync candidate

This optional route is **experimental**. It is restricted to ARM64 **rootful** jailbreaks, iOS **15.0–18.2**, with compatible official AppSync packages. It is **not** a RootHide or rootless AppSync conversion and is not a general solution for every jailbroken phone.

1. Add the official AppSync source, `https://cydia.akemi.ai/`, in Sileo.
2. In Zema's Repo, select **ZGTA V (AppSync installer - experimental)**.
3. Review Sileo's dependency list. It requires `ai.akemi.appsyncunified` **116.0+** and `ai.akemi.appinst` **2.1.1+**, plus firmware, curl and coreutils. Let Sileo resolve/configure them; our script never launches a nested APT installation.
4. Install the candidate, then test launching the app while the compatible jailbreak is active. Report the Sileo error if installation fails, or the app's actual launch result.

The official dependency server timed out from the build Mac on **2026-10-26**. Fresh dependency downloads could not be verified. If Sileo cannot fetch them, installation remains blocked; this repository does not mirror third-party AppSync binaries or substitute unverified forks.

The installer refuses an incompatible architecture/firmware, unconfigured or outdated dependencies, a bad download, and a detected TrollStore-managed copy. It calls the official `appinst <IPA>` interface and reports failure if appinst fails. Removing the wrapper leaves the app and its data in place. It does not remove apps, reset data, force a registration change or fall through to another installer.

**Actual AppSync installation, launch, gameplay, upgrades and reboot behavior have not been tested.** The engine source has a smaller virtual-memory reservation fallback, but that does not prove the app has sufficient memory or works on a given AppSync setup. This route needs an active compatible jailbreak; no TrollStore-style reboot persistence is promised.


## Upstream interfaces checked

- [RootHide filesystem view](https://github.com/roothide/Developer/blob/c53cc199f1bab7d7ea2fd70f0a14e215b1f3461b/roothide.md) and [path-conversion interfaces](https://github.com/roothide/Developer/blob/c53cc199f1bab7d7ea2fd70f0a14e215b1f3461b/interface.md).

- [TrollStore helper source](https://github.com/opa334/TrollStore/blob/88424f683b2a08f34a3f88985f790f97d84ce1df/RootHelper/main.m): `install custom <IPA>`; no force argument.
- [Official appinst usage](https://github.com/akemin-dayo/AppSync/blob/235aca6cddfbdc9fa87fcb5b2aec2df37ed6d65a/appinst/README.md) and [dependency identifiers](https://github.com/akemin-dayo/AppSync/blob/235aca6cddfbdc9fa87fcb5b2aec2df37ed6d65a/appinst/control).
- [AppSync firmware and architecture metadata](https://github.com/akemin-dayo/AppSync/blob/235aca6cddfbdc9fa87fcb5b2aec2df37ed6d65a/control). These upstream ranges do not constitute a ZGTA V device test.

Installer source and local test cases are in `package-sources/` and `tools/`. The clean [public2.0 beta source and platform guide](https://github.com/zemabinks/ZGTA-V/blob/main/docs/START-HERE.md) are available; older private application history remains private. The browser packages use revision92; native91 is unchanged.

[Previous Build90 guide](zgta-v-installation-build90.md) retains its historical verification record.
