# Agent Rules

## In-Game Documentation

- Keep in-game player documentation and the SWLOR Wiki updated together in the same task. When changing in-game articles, quick answers, combat-style topics, or other player-facing documentation, update the corresponding wiki content too. Update affected authored wiki articles when their descriptions or mechanics would otherwise contradict the in-game docs.
- The in-game Player Guide is the canonical source for `Gameplay/PlayerGuide.html` and `Gameplay/PlayerGuide/*.html`. Do not edit these generated pages by hand. From the SWLOR_NWN checkout containing the documentation changes, run `pwsh -File tools/SyncPlayerGuideWiki.ps1 -WikiPath C:\Projects\SWLOR_Wiki`, then repeat with `-CheckOnly` to verify parity. Substitute the actual wiki checkout path when needed.
- Include the changes from both repositories when publishing a documentation update. If either checkout is unavailable, report the outstanding synchronization instead of calling the task complete.

## Wiki Pages

- Preserve Wiki.js page metadata and the existing HTML/Markdown editor format. Internal page links omit `.html`/`.md` and use one `../` per source path segment so locale-relative links work with trailing slashes. For example, a page at `Gameplay/PlayerGuide/skills` links to the hub with `../../../Gameplay/PlayerGuide`.
- Preserve authored guides and images when updating generated Player Guide content. Link the Player Guide from the home page, Gameplay hub, and Quick Start Guide.
