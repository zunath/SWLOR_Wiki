---
title: Key Access Setup
description: 
published: true
date: 2021-11-07T12:32:04.819Z
tags: 
editor: markdown
dateCreated: 2021-11-07T12:32:04.819Z
---

### Door

| Variable | Type | Required | Purpose |

| -------- | ----  | --------- | -------- |

| REQ_KEY_TAG | string | x | Sets the item key to check in opening player's inventory |

| REQ_KEY_TIER | int | x | Sets the tier the item key must match or exceed to open |

| REQ_KEY_FAIL_MSG | string |  | Optionally emits a message if the opening player is denied access |

### Key Item

Should have a Tag that matches the REQ_KEY_TAG of any door that it should open.

EG for the Jedi Temple, this may be called `JEDI_KEY` in both the Door Variable and Key Tag

Also has a variable:

| Variable | Type | Required | Purpose |

| -------- | ----  | --------- | -------- |

| TIER | int| x | The value the OnOpen event checks when verifying whether the user can open a door |

If the TAG matches, the door will then check against the TIER.  If the TIER >= the REQ_KEY_TIER, then the door will open.

### Relationship

| Door | Key (an NWN Item) |

| ----- | -------------------- |

| var: REQ_KEY_TAG | tag |

| var: REQ_KEY_TIER | var: TIER |

