# ZGTA V Build 89 — candidate update

This is a **candidate**, by **zema**. It is not the audited public 2.0 release yet. Your own game files are required. These small `.deb` packages install the same pinned IPA; they do not contain the game files. Keep your existing game app, files and saves when updating.

## What changed in Build89

The app is English only, including upgrades previously set to Vietnamese. Folder scans find archives beside incomplete data, rescan remembered locations, retain parent-folder access during extraction and validate readiness. Default unpacking keeps the source archive; the optional space-saving mode explicitly removes it. Existing saves, settings, backups, artwork and game resources are preserved. Old backup formats remain importable.

Build89 passes local ARM64 build/package checks, actual Mac ZIP/split-ZIP extraction, discovery/English/save/control regressions and two Simulator UI cases. **Its physical phone installation and actual iOS Files-provider access have not been tested yet.** Build88 installation and launcher opening were confirmed separately. Keep the current app and data when updating.

After updating: open Game files, choose the folder containing your archive, then try Look again and Check every file again. Archive candidates should remain available even beside an incomplete game. Report the exact status if access fails; a missing-file list alone does not prove storage exhaustion or archive corruption.

## Previous RootHide installation correction (Build88)

Installer **0.88-1** was tested on an iOS 17.0 phone with **TrollStore 2.1.1 already installed**, but failed to find its helper before downloading the IPA. The game was not installed. That error did not prove TrollStore was missing.

The corrected **0.88-2** installer was released for Build88. Keep TrollStore installed. The new script uses RootHide's documented `/rootfs` view, accepts helper ownership UID 0 or 33 as used by upstream, and translates the IPA path whenever running in RootHide. It does not change helper ownership or filesystem permissions. Twenty local mocked tests pass. The physical retest now passes: Sileo installed Build88 through TrollStore on an iPhone15Pro with iOS17.0 and TrollStore2.1.1, Xcode confirms version2.0/build88, and the user confirms that the launcher opens.

The curl, libc-ares2, libcurl4, libnghttp2-14, librtmp1 and libssh2-1 packages shown by Sileo are the download tool and its networking dependencies. The 0.88-2 correction adds no dependencies. Leave those libraries installed; other software may use them. The yellow warning about a missing Maintainer field in an unrelated package was not the reported ZGTA V failure.

## Your iPhone already has TrollStore or TrollStore Lite

1. Add `https://zemabinks.github.io/repo/` to Sileo, or refresh that source.
2. Search for **ZGTA V (TrollStore installer)** and install/update to **0.89-1**.
3. Let the download and native installation finish. Open **ZGTA V** afterward.

No AppSync package is needed for this route. It uses the helper from your installed TrollStore, verifies the exact IPA size and SHA-256, and waits for its result. It does not force a same-identifier app installed by another method to be overwritten. If the helper cannot execute from your bootstrap, installation stops with a Sileo error. Send that log; do not delete your game or reset data.

Removing the small Sileo installer leaves the TrollStore-managed game and its data installed. Use TrollStore for actual app removal.

## No supported TrollStore setup: AppSync candidate

This optional route is **experimental**. It is restricted to ARM64 **rootful** jailbreaks, iOS **15.0–18.2**, with compatible official AppSync packages. It is **not** a RootHide or rootless AppSync conversion and is not a general solution for every jailbroken phone.

1. Add the official AppSync source, `https://cydia.akemi.ai/`, in Sileo.
2. In Zema's Repo, select **ZGTA V (AppSync installer - experimental)**.
3. Review Sileo's dependency list. It requires `ai.akemi.appsyncunified` **116.0+** and `ai.akemi.appinst` **2.1.1+**, plus firmware, curl and coreutils. Let Sileo resolve/configure them; our script never launches a nested APT installation.
4. Install the candidate, then test launching the app while the compatible jailbreak is active. Report the Sileo error if installation fails, or the app's actual launch result.

The official dependency server timed out from the build Mac on **2026-10-26**. Fresh dependency downloads could not be verified. If Sileo cannot fetch them, installation remains blocked; this repository does not mirror third-party AppSync binaries or substitute unverified forks.

The installer refuses an incompatible architecture/firmware, unconfigured or outdated dependencies, a bad download, and a detected TrollStore-managed copy. It calls the official `appinst <IPA>` interface and reports failure if appinst fails. Removing the wrapper leaves the app and its data in place. It does not remove apps, reset data, force a registration change or fall through to another installer.

**Actual AppSync installation, launch, gameplay, upgrades and reboot behavior have not been tested.** The engine source has a smaller virtual-memory reservation fallback, but that does not prove the app has sufficient memory or works on a given AppSync setup. This route needs an active compatible jailbreak; no TrollStore-style reboot persistence is promised.

## Manual download

The [Build 89 release](https://github.com/zemabinks/repo/releases/tag/zgta-v-build-89) also contains the IPA and checksum files. Download the IPA and open it in your compatible TrollStore. Installing either Sileo wrapper downloads exactly those same bytes.

IPA size: **90,970,017 bytes**

SHA-256: `24ef0268fee776b42302cdfec45c189ca30095c3b7d837ae356b7cd582ffcdcb`

## Verification and limits

- Local ARM64 build/package, English/save/control checks, folder discovery, real Mac ZIP/split-ZIP extraction and two Simulator UI cases pass for Build89.
- Installer shell tests use isolated mock helpers; they do **not** prove device installation.
- Debian archives contain only control metadata and a post-install script, with no app payload, uninstall scripts, game data or bundled native helpers.
- The 0.88-1 phone installation failed at helper discovery; 0.88-2 Sileo → TrollStore installation and launcher opening pass on the tested iPhone. Live two-device gameplay, real updates and reboot behavior remain pending.
- Installation method does not establish complete jailbreak/iOS/device compatibility.

## Upstream interfaces checked

- [RootHide filesystem view](https://github.com/roothide/Developer/blob/c53cc199f1bab7d7ea2fd70f0a14e215b1f3461b/roothide.md) and [path-conversion interfaces](https://github.com/roothide/Developer/blob/c53cc199f1bab7d7ea2fd70f0a14e215b1f3461b/interface.md).

- [TrollStore helper source](https://github.com/opa334/TrollStore/blob/88424f683b2a08f34a3f88985f790f97d84ce1df/RootHelper/main.m): `install custom <IPA>`; no force argument.
- [Official appinst usage](https://github.com/akemin-dayo/AppSync/blob/235aca6cddfbdc9fa87fcb5b2aec2df37ed6d65a/appinst/README.md) and [dependency identifiers](https://github.com/akemin-dayo/AppSync/blob/235aca6cddfbdc9fa87fcb5b2aec2df37ed6d65a/appinst/control).
- [AppSync firmware and architecture metadata](https://github.com/akemin-dayo/AppSync/blob/235aca6cddfbdc9fa87fcb5b2aec2df37ed6d65a/control). These upstream ranges do not constitute a ZGTA V device test.

Installer source and local test cases are in `package-sources/` and `tools/`. Source for the eventual public 2.0 release is being audited separately; older private application history is not being exposed.
