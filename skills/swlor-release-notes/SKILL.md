---
name: swlor-release-notes
description: Create, update, or publish SWLOR Wiki release notes from merged game and asset changes, using player-facing wording and established disclosure rules. Use for release-note work, not general Wiki documentation.
---

# SWLOR release notes

Use this skill with either GPT or Claude. It uses ordinary Git, GitHub, file, and browser capabilities; no agent-specific API, scripts, symlinks, or installation step is required. `AGENTS.md` routes GPT to this shared file, and `CLAUDE.md` imports those same instructions for Claude. In another checkout or chat, supply this file directly when automatic discovery is unavailable.

## Sources and destination

- Game: `https://github.com/zunath/SWLOR_NWN`.
- Assets: the game's pinned `SWLOR_Haks` submodule, `https://github.com/zunath/SWLOR_Haks`.
- Wiki content: `https://github.com/zunath/SWLOR_Wiki`.
- Live Wiki: `https://wiki.starwarsnwn.com`.
- Upcoming: `ReleaseNotes/RN_Unreleased.html`, URL `/ReleaseNotes/RN_Unreleased`.
- Released: `ReleaseNotes/RN_YYYY-MM-DD.html`.
- Index: `ReleaseNotes.html`, URL `/ReleaseNotes`.

Locate the real checkouts and read applicable instructions. Common Windows paths are `C:\Projects\SWLOR_NWN` and `C:\Projects\SWLOR_Wiki`; the current directory may be a stale worktree. Verify remotes, default branches, and working-tree state. Preserve unrelated work. The destination is the Git-backed Wiki, not a ChatGPT Page or Space.

## Establish what is new

1. Read the current upcoming page, latest dated release, and recent Wiki release-note commit messages (older updates recorded this in PR descriptions). Recover the last reviewed game commit from them, rather than guessing a deployment cutoff from timestamps.
2. Refresh remote refs or query GitHub. Take a specific snapshot of the game's default branch and inspect integrated changes after the coverage boundary. Verify actual merged diffs, not just titles, session summaries, or bot-generated notes. Include direct default-branch commits when their integration is verified.
3. Compare the old and new pinned asset revisions. Include player-visible icons, models, colors, text, and walkmesh fixes. An asset PR merged to its own master is not enough if the game has not integrated it. A pointer-only change with an identical tree adds no release-note entry.
4. Consolidate overlapping fixes into their final behavior. Omit duplicates, reverted changes, tests, tooling, and staff diagnostic reports with no meaningful player-facing outcome. DM gameplay tools can be included under DM Tools.
5. Record the reviewed game commit, asset revision, included PRs, and relevant omissions in the Wiki commit message body. Keep these references out of the public notes. A later update starts from this recorded snapshot.

Merged does not mean deployed. Open PRs, in-progress sessions, local changes, and unmerged companions are ineligible. Never merge game or asset PRs merely to make their content eligible. If the deployment boundary is uncertain, compare released notes and deployment evidence; do not invent a date, cutoff, or NWSync hash.

## Write for players

Describe the resulting experience, recognizable UI labels, and anything players need to do. Use concise bullets under topical headings. Preserve practical restrictions and consequences established by the merged code, such as required permissions, out-of-combat requirements, inventory recovery commands, automatic item corrections, and preservation of customizations.

- Avoid class names, database or serialization details, resource IDs, model filenames, debug output, test histories, and PR numbers.
- Explain new dungeons as finished features. Fold their pre-release repairs into that description; ordinary fixes to already released dungeons can be listed normally.
- Include important icon and appearance changes alongside gameplay changes.
- Keep the introduction, metadata description, and index summary aligned with the final body.
- Do not infer commands, item effects, rewards, or deployment status from intent alone.

Examples: "The ship lists now reliably show all your owned and shared ships." "Fixed characters appearing as Grouped when they are not in a party." "Capstone quest givers have been relocated."

## Disclosure rules

### Enemy balance and the Great Arkanian Dragon

Keep enemy and boss stat adjustments general: "Boss encounters have received balance adjustments." Do not publish exact stat values, percentage changes, hit-chance floors, or detailed balance breakdowns by default.

Keep Arkanian Dragon drops, rewards, and crafting details vague. Do not name specific drops or blueprints, quantities, rates, guarantees, loot conditions, or exact ingredients. The approved level of disclosure is:

> The Great Arkanian Dragon encounter and its rewards have received balance adjustments.
>
> Arkanian Dragon crafting options have been expanded, with updates to existing equipment and recipes.

A general encounter update may mention a new ability and its icons without numerical mechanics. Apply these limits to the body, metadata, index, and user-facing publication summary. Do not restore hidden details from source PRs or earlier drafts.

### RPXP

Routine updates exclude RPXP policy, OOC-message mechanics, penalties, thresholds, additional checks, and logging details. Do not re-add the removed line about how out-of-character chat affects roleplay XP.

The sensitive RPXP explanation was tabled, not approved for publication. If resumed, provide the full proposed text for review and wait for explicit approval before posting it. A generic release-note update is not that approval.

The user separately approved a notice that the RPXP Penalty System would be disabled temporarily for further fine tuning. Preserve it in its relevant historical release; do not copy it into each upcoming set or assume it describes the present system.

### Other omissions

Do not disclose specific locations of relocated capstone quest givers. The free rebuild token for existing players belongs to the combat-upgrade rollout notes; do not imply another grant in later releases. Preserve user-approved omissions when reviewing newer work.

## Page lifecycle

Use the user's local calendar date for visible dates (this publishing workflow uses America/New_York), and an actual UTC edit timestamp for metadata. Preserve `dateCreated` and unrelated metadata when reusing an existing page.

**Update upcoming:** maintain published visibility, the unreleased tag, the Unreleased index category, visible Status Upcoming, and release date/hash TBD until confirmed. Update Notes Updated and metadata timestamps. Leave dated released pages unchanged.

**Start a new set:** use the latest released coverage boundary. Reuse RN_Unreleased as a real upcoming page, with a link to the latest dated release and its own Unreleased index entry. Do not carry released changes forward. If no new eligible changes exist, say none have been added yet and retain TBD fields. Replace that placeholder when changes arrive.

**Publish a release:** when requested or deployment is confirmed within the authorized task, put the complete notes on their own dated page. Use the confirmed release date and exact supplied NWSync hash. Update title, description, tags, visible Released status, date/hash, and introductory wording. Move its index entry into the correct year, newest first; remove its stale Upcoming entry. Preserve disclosure limits and final collected content.

When a new upcoming set is requested after publication, RN_Unreleased must be a fresh upcoming page, not a moved notice. Do not leave the same release listed as both Upcoming and Released. Create another set only when requested or when separately identified pending work requires it.

## Save and verify

A request for a draft, skill, or text first does not authorize posting notes. Respect specific review holds. In an authorized Wiki publishing session, the established user preference is to push the change directly without requiring their review. The skill itself grants no new permission to publish in a different context.

Do not open a Wiki PR. Commit the validated change in a separate worktree based on the freshly fetched Wiki default branch, then push that commit directly to the default branch. If the push is rejected because the branch moved, rebase onto the new tip, re-check the result, and push again; never force-push. Preserve unrelated edits and other checkouts. Do not edit the game to perform a Wiki-only update.

Validate the affected HTML, unique IDs, links, metadata, dates, status, index placement, coverage, and disclosure limits. Run `git diff --check`. Compare released pages to ensure routine upcoming edits did not change them. For a release publication, verify the collected sections carried over. Prose-only work needs document and publication checks, not game builds or in-game tests.

A successful push does not prove the live Wiki updated. Confirm the commit is on the remote default branch, then read the live page and index. Check the new entries and intended status/category. For publication, verify the exact date and hash on the dated page.

If content is stale, the signed-in administration page `/a/storage` offers **Force Sync**. Inspect the current UI and use only that normal action. Do not change storage configuration or use Add Untracked Changes, Import Everything, or Purge Local Repository. Allow the asynchronous operation to finish; inspect its outcome before retrying. Preserve the authenticated session and return the tab to the notes. Do not sign out.

If a browser tab fails to render or interact, use the available browser's documented recovery and a fresh tab when appropriate; do not assume a timeout means the action succeeded. If sign-in needs user participation or live verification is blocked, report what is complete and the concrete blocker. Do not claim live success from the push alone.

Finish with a concise link and the main added topics. Save and include screenshot evidence when the browser tooling requires it. Keep sensitive details out of public commit messages as well as player notes.
