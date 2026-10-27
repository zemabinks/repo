# ZGTA V development and release workflow

**Current Sileo delivery rule:** the later owner clarification below authorizes updated candidate IPAs in this Sileo source. The earlier public-release gate continues to apply to the official ZGTA V project release.

## Development and public-release rule — owner instruction, 27 October 2026

This rule supersedes any earlier wording that automatically publishes every native build or treats keeping GitHub updated as permission to promote a development candidate.

- Continue authorized implementation, automated checks, builds, private candidate packages, private source pushes and progress records without routine approval questions. Use `zemabinks/ZGTA-V-Private-Development` for unfinished work.
- Keep untested application code and packages out of `zemabinks/ZGTA-V` and the public Sileo repository `zemabinks/repo`, including public branches, pull requests, draft releases and prereleases. A prerelease label is not a substitute for this rule.
- Identify when a candidate is almost ready and tell the owner what changed, which checks pass and what still needs their testing. Prepare the concrete candidate privately before requesting a test.
- Before offering public promotion, complete the applicable local checks and obtain the owner's test result for the exact candidate on every relevant platform/device they own: iPhone/iOS and Mac/browser. Verify affected startup, saves, mods and paired multiplayer behavior as appropriate to the change; do not equate packaging or mocked tests with physical gameplay. A materially changed binary/source invalidates affected prior test evidence.
- Windows and Android are explicit exceptions to owner hardware testing because the owner does not own those devices. Still perform available package/static/shared-code checks, disclose untested platform execution and do not claim universal compatibility. This exception does not waive iPhone or Mac testing.
- When the candidate is ready, present one yes/no choice identifying the exact build and test summary: **Publish this build to the public ZGTA V repo and matching Sileo source?** Offer **Yes — publish** and **No — keep in development**. Wait for an actual answer. Generic requests to continue, fix, build, update GitHub or keep repositories current do not authorize public promotion.
- A yes authorizes the complete matching release transaction: approved source/packages, public README/download guides and the Sileo packages/catalogs/depictions/signed indexes. Complete and read back that transaction without asking again for each routine step. A no keeps the candidate private while development continues. Material changes after a yes require renewed affected testing and a new publication choice.
- Public channels stay on the last explicitly approved build. Keep development indexes current privately; never advertise an unapproved candidate as the public current build. Record candidate identity, owner results, outstanding gaps and the publication answer in the private release receipt and UPM evidence.
- Correcting release policy text alone does not approve or promote application changes. This clarification does not retroactively approve already published Build96, authorize a rollback, or establish any missing device test result.

## Standing Sileo update instruction — owner clarification, 27 October 2026

The owner requested “always upload the IPA when updated to my repo” and explicitly clarified “My Sileo source.” This later instruction authorizes distributing each successfully packaged iOS update through `zemabinks/repo`, including test candidates, without a separate routine publication question. It supersedes the Sileo restriction in the earlier rule above. The official public `zemabinks/ZGTA-V` release gate remains in place. Sileo delivery does not establish phone acceptance or stable status.

1. Mirror the exact verified IPA and checksum in this repository's release. Preserve its build number, byte count, SHA-256 and source revision.
2. Increment both existing installer versions and pin that same IPA URL, size and hash. Preserve installation methods, app data and all previous package versions.
3. Update catalogs, depictions, README, landing page and installation guide together. Clearly label candidates and outstanding device tests; keep historical confirmations tied to their actual build.
4. Regenerate package indexes and sign Release/InRelease using the existing key. Verify signatures, archive pins, index hashes and retained old stanzas.
5. Read back the live catalogs, signed indexes, packages and actual IPA bytes. Report the advertised installer version and remaining device checks.

Use existing keys and credentials. Never export private keys or infer physical installation/gameplay from fixtures. No paid hosted runner, billing change or new service is required.
