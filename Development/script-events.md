---
title: Script Events
description: 
published: true
date: 2021-11-13T02:16:37.442Z
tags: 
editor: markdown
dateCreated: 2021-11-13T02:16:37.442Z
---

# Events Overview

Todo: A brief explanation of how to hook up events and create a script method.


## Module Events

| Script | Description | Notes |
| --- | --- | --- |
| mod_acquire | Runs when a player acquires an item. | |
| mod_activate | Runs when a player activates an item. | |
| mod_enter | Runs when a player enters the server. | |
| mod_exit | Runs when a player exits the server. | |
| mod_abort_cs | Runs when a player aborts a cutscene. | |
| mod_heartbeat | Runs once every six seconds. | If you are iterating over players, don't use this event. Instead, hook the interval_pc_6s event because it will be more performant. |
| mod_load | Runs when the module loads. | Very useful for caching and other one-time actions. |
| mod_chat | Runs when a player sends a chat message. | Recommended to use the NWNX chat event instead of this one. |
| mod_dying | Runs when a player is dying. | |
| mod_death | Runs when a player dies. | |
| mod_equip | Runs when a player equips an item. | Recommended to use the NWNX equip event instead of this one. |
| mod_level_up | Runs when a player levels up. | Don't use this. We never execute it with our system. |
| mod_respawn | Runs when a player respawns. | |
| mod_rest | Runs when a player rests. | The only time we use this is to open the rest menu. Don't use it for any other purpose. |
| mod_unequip | Runs when a player unequips an item. | This event is preferable over the NWNX event if you need to get the item being unequipped. If you don't need that, the NWNX event is recommended instead of this one. |
| mod_unacquire | Runs when a player loses an item. | |
| mod_user_def | Module's user defined event. | We don't have a use for this. Recommended to avoid using this one. |
| mod_p_target | Runs when a player targets something with the EnterTargetingMode feature. |  |
| mod_gui_event | Runs when a player clicks on a particular GUI interface | https://nwnlexicon.com/index.php?title=OnPlayerGuiEvent |
| mod_tile_event | Runs when surfacemat.2da functions are used. | https://nwnlexicon.com/index.php?title=OnPlayerTileAction |
| mod_nui_event | Runs when a custom NUI window event is raised. |  |
| mod_content_chg | Runs once during the preload event only if the module has changed since the last time the server ran. | |

## Interval Events

| Script | Description | Notes |
| --- | --- | --- |
| interval_pc_6s | Runs on an individual player every six seconds. | OBJECT_SELF is the player in this event. Code absolutely needs to be performant on this event. Avoid using it unless you absolutely need it. |
| interval_pc_1s | Runs on an individual player every second. | OBJECT_SELF is the player in this event. Code absolutely needs to be performant on this event. Avoid using it unless you absolutely need it. |

## Area Events

| Script | Description | Notes |
| --- | --- | --- |
| area_enter | Runs when a creature enters an area. | Be sure to filter area-specific scripts down to the resref of the area. |
| area_exit | Runs when a creature exits an area. | Be sure to filter area-specific scripts down to the resref of the area. |
| area_heartbeat | Runs every six seconds. | Be sure to filter area-specific scripts down to the resref of the area. Avoid using this unless it's absolutely necessary. |
| area_user_def | Area user defined events. | We don't have a use for this. Recommend avoiding using this one. |

## Creature Events
| Script | Description | Notes |
| --- | --- | --- |
| crea_heartbeat | Runs when a creature's OnHeartbeat event fires. | |
| crea_perception | Runs when a creature's OnPerception event fires. | |
| crea_roundend | Runs when a creature's OnCombatRound event fires. | |
| crea_convo | Runs when a creature's OnConversation event fires. | |
| crea_attacked | Runs when a creature's OnAttacked event fires. | |
| crea_damaged | Runs when a creature's OnDamaged event fires. | |
| crea_death | Runs when a creature's OnDeath event fires. | |
| crea_disturb | Runs when a creature's OnDisturbed event fires. | |
| crea_spawn | Runs when a creature's OnSpawn event fires. | |
| crea_rested | Runs when a creature's OnRested event fires. | |
| crea_spellcastat | Runs when a creature's OnSpellCastAt event fires. | Generally not used since we have a custom spell system. |
| crea_userdef | Runs when a creature's OnUserDefined event fires. | |
| crea_blocked | Runs when a creature's OnBlocked event fires. | |

## Server Events
| Script | Description | Notes |
| --- | --- | --- |
| app_shutdown | Runs when the application shuts down. | Can be useful to ensure any async threads finish or if any final cleanup needs to be done. 
| item_eqp_bef | Runs after the custom validation of an item (item_eqpval_bef event) | Subject to the same rules as the NWNX_ON_ITEM_EQUIP_BEFORE event in NWNX.
| cache_data | Runs after events are hooked but before module load. | Any time data is being loaded into memory dictionaries, this event should be used. In many cases, calls during module load will reference this data.

## NWNX Events

NOTE: Please refer to the NWNX documentation on using these events. The information there will be more accurate and up to date. https://github.com/nwnxee/unified/blob/master/Plugins/Events/NWScript/nwnx_events.nss

| Script | NWNX Event | Description | Notes |
| --- | --- | --- | --- |
| on_nwnx_chat | NWNX Chat Event | Fires when players send chat messages. This is the preferred event for anything chat-related. | More info here: https://github.com/nwnxee/unified/blob/master/Plugins/Chat/NWScript/nwnx_chat.nss |
| on_nwnx_dmg | NWNX Damage Event | Fires when damage is applied. | More info here: https://github.com/nwnxee/unified/blob/master/Plugins/Damage/NWScript/nwnx_damage.nss |
| asso_add_bef | NWNX_ON_ADD_ASSOCIATE_BEFORE | |
| asso_add_aft | NWNX_ON_ADD_ASSOCIATE_AFTER | |
| asso_rem_bef | NWNX_ON_REMOVE_ASSOCIATE_BEFORE | |
| asso_rem_aft | NWNX_ON_REMOVE_ASSOCIATE_AFTER | |
| stlent_add_bef | NWNX_ON_ENTER_STEALTH_BEFORE | |
| stlent_add_aft | NWNX_ON_ENTER_STEALTH_AFTER | |
| stlex_add_bef | NWNX_ON_EXIT_STEALTH_BEFORE | |
| stlex_add_aft | NWNX_ON_EXIT_STEALTH_AFTER | |
| examine_bef | NWNX_ON_EXAMINE_OBJECT_BEFORE | |
| examine_aft | NWNX_ON_EXAMINE_OBJECT_AFTER | |
| item_valid_bef | NWNX_ON_VALIDATE_USE_ITEM_BEFORE | | 
| item_valid_aft | NWNX_ON_VALIDATE_USE_ITEM_AFTER | | 
| item_use_bef | NWNX_ON_USE_ITEM_BEFORE | |
| item_use_aft | NWNX_ON_USE_ITEM_AFTER | |
| inv_open_bef | NWNX_ON_ITEM_INVENTORY_OPEN_BEFORE | |
| inv_open_aft | NWNX_ON_ITEM_INVENTORY_OPEN_AFTER | |
| inv_close_bef | NWNX_ON_ITEM_INVENTORY_CLOSE_BEFORE | |
| inv_close_aft | NWNX_ON_ITEM_INVENTORY_CLOSE_AFTER | |
| ammo_reload_bef | NWNX_ON_ITEM_AMMO_RELOAD_BEFORE | |
| ammo_reload_aft | NWNX_ON_ITEM_AMMO_RELOAD_AFTER | |
| scroll_lrn_bef | NWNX_ON_ITEM_SCROLL_LEARN_BEFORE | |
| scroll_lrn_aft | NWNX_ON_ITEM_SCROLL_LEARN_AFTER | |
| item_val_bef | NWNX_ON_VALIDATE_ITEM_EQUIP_BEFORE | | Runs **after** the item equip event, limiting its usefulness
| item_val_aft | NWNX_ON_VALIDATE_ITEM_EQUIP_AFTER | | Runs **after** the item equip event, limiting its usefulness
| item_eqpval_bef | NWNX_ON_ITEM_EQUIP_BEFORE | | We use this as a way to validate item equips. If you need to hook the equip event, use item_eqp_bef
| item_eqpval_aft | NWNX_ON_ITEM_EQUIP_AFTER | | We use this as a way to validate item equips. If you need to hook the equip event, use item_eqp_aft
| item_uneqp_bef | NWNX_ON_ITEM_UNEQUIP_BEFORE | |
| item_uneqp_aft | NWNX_ON_ITEM_UNEQUIP_AFTER | |
| item_dest_bef | NWNX_ON_ITEM_DESTROY_OBJECT_BEFORE | |
| item_dest_aft | NWNX_ON_ITEM_DESTROY_OBJECT_AFTER | |
| item_dec_bef | NWNX_ON_ITEM_DECREMENT_STACKSIZE_BEFORE | |
| item_dec_aft | NWNX_ON_ITEM_DECREMENT_STACKSIZE_AFTER | |
| lore_id_bef | NWNX_ON_ITEM_USE_LORE_BEFORE | |
| lore_id_aft | NWNX_ON_ITEM_USE_LORE_AFTER | |
| pay_id_bef | NWNX_ON_ITEM_PAY_TO_IDENTIFY_BEFORE | |
| pay_id_aft | NWNX_ON_ITEM_PAY_TO_IDENTIFY_AFTER | |
| item_splt_bef | NWNX_ON_ITEM_SPLIT_BEFORE | |
| item_splt_aft | NWNX_ON_ITEM_SPLIT_AFTER | |
| feat_use_bef | NWNX_ON_USE_FEAT_BEFORE | |
| feat_use_aft | NWNX_ON_USE_FEAT_AFTER | |
| dm_givegold_bef | NWNX_ON_DM_GIVE_GOLD_BEFORE | |
| dm_givegold_aft | NWNX_ON_DM_GIVE_GOLD_AFTER | |
| dm_givexp_bef | NWNX_ON_DM_GIVE_XP_BEFORE | |
| dm_givexp_aft | NWNX_ON_DM_GIVE_XP_AFTER | |
| dm_givelvl_bef | NWNX_ON_DM_GIVE_LEVEL_BEFORE | |
| dm_givelvl_aft | NWNX_ON_DM_GIVE_LEVEL_AFTER | |
| dm_givealn_bef | NWNX_ON_DM_GIVE_ALIGNMENT_BEFORE | |
| dm_givealn_aft | NWNX_ON_DM_GIVE_ALIGNMENT_AFTER | |
| dm_spwnobj_bef | NWNX_ON_DM_SPAWN_OBJECT_BEFORE | |
| dm_spwnobj_aft | NWNX_ON_DM_SPAWN_OBJECT_AFTER | |
| dm_giveitem_bef | NWNX_ON_DM_GIVE_ITEM_BEFORE | |
| dm_giveitem_aft | NWNX_ON_DM_GIVE_ITEM_AFTER | |
| dm_heal_bef | NWNX_ON_DM_HEAL_BEFORE | |
| dm_heal_aft | NWNX_ON_DM_HEAL_AFTER | |
| dm_kill_bef | NWNX_ON_DM_KILL_BEFORE | |
| dm_kill_aft | NWNX_ON_DM_KILL_AFTER | |
| dm_invuln_bef | NWNX_ON_DM_TOGGLE_INVULNERABLE_BEFORE | |
| dm_invuln_aft | NWNX_ON_DM_TOGGLE_INVULNERABLE_AFTER | |
| dm_forcerest_bef | NWNX_ON_DM_FORCE_REST_BEFORE | |
| dm_forcerest_aft | NWNX_ON_DM_FORCE_REST_AFTER | |
| dm_limbo_bef | NWNX_ON_DM_LIMBO_BEFORE | |
| dm_limbo_aft | NWNX_ON_DM_LIMBO_AFTER | |
| dm_ai_bef | NWNX_ON_DM_TOGGLE_AI_BEFORE | |
| dm_ai_aft | NWNX_ON_DM_TOGGLE_AI_AFTER | |
| dm_immortal_bef | NWNX_ON_DM_TOGGLE_IMMORTAL_BEFORE | |
| dm_immortal_aft | NWNX_ON_DM_TOGGLE_IMMORTAL_AFTER | |
| dm_goto_bef | NWNX_ON_DM_GOTO_BEFORE | |
| dm_goto_aft | NWNX_ON_DM_GOTO_AFTER | |
| dm_poss_bef | NWNX_ON_DM_POSSESS_BEFORE | |
| dm_poss_aft | NWNX_ON_DM_POSSESS_AFTER | |
| dm_possfull_bef | NWNX_ON_DM_POSSESS_FULL_POWER_BEFORE | |
| dm_possfull_aft | NWNX_ON_DM_POSSESS_FULL_POWER_AFTER | |
| dm_lock_bef | NWNX_ON_DM_TOGGLE_LOCK_BEFORE | |
| dm_lock_aft | NWNX_ON_DM_TOGGLE_LOCK_AFTER | |
| dm_distrap_bef | NWNX_ON_DM_DISABLE_TRAP_BEFORE | |
| dm_distrap_aft | NWNX_ON_DM_DISABLE_TRAP_AFTER | |
| dm_jumppt_bef | NWNX_ON_DM_JUMP_TO_POINT_BEFORE | |
| dm_jumppt_aft | NWNX_ON_DM_JUMP_TO_POINT_AFTER | |
| dm_jumptarg_bef | NWNX_ON_DM_JUMP_TARGET_TO_POINT_BEFORE | |
| dm_jumptarg_aft | NWNX_ON_DM_JUMP_TARGET_TO_POINT_AFTER | |
| dm_jumpall_bef | NWNX_ON_DM_JUMP_ALL_PLAYERS_TO_POINT_BEFORE | |
| dm_jumpall_aft | NWNX_ON_DM_JUMP_ALL_PLAYERS_TO_POINT_AFTER | |
| dm_chgdiff_bef | NWNX_ON_DM_CHANGE_DIFFICULTY_BEFORE | |
| dm_chgdiff_aft | NWNX_ON_DM_CHANGE_DIFFICULTY_AFTER | |
| dm_vwinven_bef | NWNX_ON_DM_VIEW_INVENTORY_BEFORE | |
| dm_vwinven_aft | NWNX_ON_DM_VIEW_INVENTORY_AFTER | |
| dm_spwntrap_bef | NWNX_ON_DM_SPAWN_TRAP_ON_OBJECT_BEFORE | |
| dm_spwntrap_aft | NWNX_ON_DM_SPAWN_TRAP_ON_OBJECT_AFTER | |
| dm_dumploc_bef | NWNX_ON_DM_DUMP_LOCALS_BEFORE | |
| dm_dumploc_aft | NWNX_ON_DM_DUMP_LOCALS_AFTER | |
| dm_appear_bef | NWNX_ON_DM_APPEAR_BEFORE | |
| dm_appear_aft | NWNX_ON_DM_APPEAR_AFTER | |
| dm_disappear_bef | NWNX_ON_DM_DISAPPEAR_BEFORE | |
| dm_disappear_aft | NWNX_ON_DM_DISAPPEAR_AFTER | |
| dm_setfac_bef | NWNX_ON_DM_SET_FACTION_BEFORE | |
| dm_setfac_aft | NWNX_ON_DM_SET_FACTION_AFTER | |
| dm_takeitem_bef | NWNX_ON_DM_TAKE_ITEM_BEFORE | |
| dm_takeitem_aft | NWNX_ON_DM_TAKE_ITEM_AFTER | |
| dm_setstat_bef | NWNX_ON_DM_SET_STAT_BEFORE | |
| dm_setstat_aft | NWNX_ON_DM_SET_STAT_AFTER | |
| dm_getvar_bef | NWNX_ON_DM_GET_VARIABLE_BEFORE | |
| dm_getvar_aft | NWNX_ON_DM_GET_VARIABLE_AFTER | |
| dm_setvar_bef | NWNX_ON_DM_SET_VARIABLE_BEFORE | |
| dm_setvar_aft | NWNX_ON_DM_SET_VARIABLE_AFTER | |
| dm_settime_bef | NWNX_ON_DM_SET_TIME_BEFORE | |
| dm_settime_aft | NWNX_ON_DM_SET_TIME_AFTER | |
| dm_setdate_bef | NWNX_ON_DM_SET_DATE_BEFORE | |
| dm_setdate_aft | NWNX_ON_DM_SET_DATE_AFTER | |
| dm_setrep_bef | NWNX_ON_DM_SET_FACTION_REPUTATION_BEFORE | |
| dm_setrep_aft | NWNX_ON_DM_SET_FACTION_REPUTATION_AFTER | |
| dm_getrep_bef | NWNX_ON_DM_GET_FACTION_REPUTATION_BEFORE | |
| dm_getrep_aft | NWNX_ON_DM_GET_FACTION_REPUTATION_AFTER | |
| client_disc_bef | NWNX_ON_CLIENT_DISCONNECT_BEFORE | |
| client_disc_aft | NWNX_ON_CLIENT_DISCONNECT_AFTER | |
| client_conn_bef | NWNX_ON_CLIENT_CONNECT_BEFORE | |
| client_conn_aft | NWNX_ON_CLIENT_CONNECT_AFTER | |
| comb_round_bef | NWNX_ON_START_COMBAT_ROUND_BEFORE | |
| comb_round_aft | NWNX_ON_START_COMBAT_ROUND_AFTER | |
| cast_spell_bef | NWNX_ON_CAST_SPELL_BEFORE | |
| cast_spell_aft | NWNX_ON_CAST_SPELL_AFTER | |
| set_spell_bef | NWNX_SET_MEMORIZED_SPELL_SLOT_BEFORE | |
| set_spell_aft | NWNX_SET_MEMORIZED_SPELL_SLOT_AFTER | |
| clr_spell_bef | NWNX_CLEAR_MEMORIZED_SPELL_SLOT_BEFORE | |
| clr_spell_aft | NWNX_CLEAR_MEMORIZED_SPELL_SLOT_AFTER | |
| heal_kit_bef | NWNX_ON_HEALER_KIT_BEFORE | |
| heal_kit_aft | NWNX_ON_HEALER_KIT_AFTER | |
| pty_leave_bef | NWNX_ON_PARTY_LEAVE_BEFORE | |
| pty_leave_aft | NWNX_ON_PARTY_LEAVE_AFTER | |
| pty_kick_bef | NWNX_ON_PARTY_KICK_BEFORE | |
| pty_kick_aft | NWNX_ON_PARTY_KICK_AFTER | |
| pty_chgldr_bef | NWNX_ON_PARTY_TRANSFER_LEADERSHIP_BEFORE | |
| pty_chgldr_aft | NWNX_ON_PARTY_TRANSFER_LEADERSHIP_AFTER | |
| pty_invite_bef | NWNX_ON_PARTY_INVITE_BEFORE | |
| pty_invite_aft | NWNX_ON_PARTY_INVITE_AFTER | |
| pty_ignore_bef | NWNX_ON_PARTY_IGNORE_INVITATION_BEFORE | |
| pty_ignore_aft | NWNX_ON_PARTY_IGNORE_INVITATION_AFTER | |
| pty_accept_bef | NWNX_ON_PARTY_ACCEPT_INVITATION_BEFORE | |
| pty_accept_aft | NWNX_ON_PARTY_ACCEPT_INVITATION_AFTER | |
| pty_reject_bef | NWNX_ON_PARTY_REJECT_INVITATION_BEFORE | |
| pty_reject_aft | NWNX_ON_PARTY_REJECT_INVITATION_AFTER | |
| pty_kickhen_bef | NWNX_ON_PARTY_KICK_HENCHMAN_BEFORE | |
| pty_kickhen_aft | NWNX_ON_PARTY_KICK_HENCHMAN_AFTER | |
| combat_mode_on | NWNX_ON_COMBAT_MODE_ON | |
| combat_mode_off | NWNX_ON_COMBAT_MODE_OFF | |
| use_skill_bef | NWNX_ON_USE_SKILL_BEFORE | |
| use_skill_aft | NWNX_ON_USE_SKILL_AFTER | |
| mappin_add_bef | NWNX_ON_MAP_PIN_ADD_PIN_BEFORE | |
| mappin_add_aft | NWNX_ON_MAP_PIN_ADD_PIN_AFTER | |
| mappin_chg_bef | NWNX_ON_MAP_PIN_CHANGE_PIN_BEFORE | |
| mappin_chg_aft | NWNX_ON_MAP_PIN_CHANGE_PIN_AFTER | |
| mappin_rem_bef | NWNX_ON_MAP_PIN_DESTROY_PIN_BEFORE | |
| mappin_rem_aft | NWNX_ON_MAP_PIN_DESTROY_PIN_AFTER | |
| det_listen_bef | NWNX_ON_DO_LISTEN_DETECTION_BEFORE | |
| det_listen_aft | NWNX_ON_DO_LISTEN_DETECTION_AFTER | |
| det_spot_bef | NWNX_ON_DO_SPOT_DETECTION_BEFORE | |
| det_spot_aft | NWNX_ON_DO_SPOT_DETECTION_AFTER | |
| polymorph_bef | NWNX_ON_POLYMORPH_BEFORE | |
| polymorph_aft | NWNX_ON_POLYMORPH_AFTER | |
| unpolymorph_bef | NWNX_ON_UNPOLYMORPH_BEFORE | |
| unpolymorph_aft | NWNX_ON_UNPOLYMORPH_AFTER | |
| effect_app_bef | NWNX_ON_EFFECT_APPLIED_BEFORE | |
| effect_app_aft | NWNX_ON_EFFECT_APPLIED_AFTER | |
| effect_rem_bef | NWNX_ON_EFFECT_REMOVED_BEFORE | |
| effect_rem_aft | NWNX_ON_EFFECT_REMOVED_AFTER | |
| quickchat_bef | NWNX_ON_QUICKCHAT_BEFORE | |
| quickchat_aft | NWNX_ON_QUICKCHAT_AFTER | |
| inv_open_bef | NWNX_ON_INVENTORY_OPEN_BEFORE | |
| inv_open_aft | NWNX_ON_INVENTORY_OPEN_AFTER | |
| inv_panel_bef | NWNX_ON_INVENTORY_SELECT_PANEL_BEFORE | |
| inv_panel_aft | NWNX_ON_INVENTORY_SELECT_PANEL_AFTER | |
| bart_start_bef | NWNX_ON_BARTER_START_BEFORE | |
| bart_start_aft | NWNX_ON_BARTER_START_AFTER | |
| bart_end_bef | NWNX_ON_BARTER_END_BEFORE | |
| bart_end_aft | NWNX_ON_BARTER_END_AFTER | |
| trap_disarm_bef | NWNX_ON_TRAP_DISARM_BEFORE | |
| trap_disarm_aft | NWNX_ON_TRAP_DISARM_AFTER | |
| trap_enter_bef | NWNX_ON_TRAP_ENTER_BEFORE | |
| trap_enter_aft | NWNX_ON_TRAP_ENTER_AFTER | |
| trap_exam_bef | NWNX_ON_TRAP_EXAMINE_BEFORE | |
| trap_exam_aft | NWNX_ON_TRAP_EXAMINE_AFTER | |
| trap_flag_bef | NWNX_ON_TRAP_FLAG_BEFORE | |
| trap_flag_aft | NWNX_ON_TRAP_FLAG_AFTER | |
| trap_rec_bef | NWNX_ON_TRAP_RECOVER_BEFORE | |
| trap_rec_aft | NWNX_ON_TRAP_RECOVER_AFTER | |
| trap_set_bef | NWNX_ON_TRAP_SET_BEFORE | |
| trap_set_aft | NWNX_ON_TRAP_SET_AFTER | |
| timing_start_bef | NWNX_ON_TIMING_BAR_START_BEFORE | |
| timing_start_aft | NWNX_ON_TIMING_BAR_START_AFTER | |
| timing_stop_bef | NWNX_ON_TIMING_BAR_STOP_BEFORE | |
| timing_stop_aft | NWNX_ON_TIMING_BAR_STOP_AFTER | |
| timing_canc_bef | NWNX_ON_TIMING_BAR_CANCEL_BEFORE | |
| timing_canc_aft | NWNX_ON_TIMING_BAR_CANCEL_AFTER | |
| webhook_success | NWNX_ON_WEBHOOK_SUCCESS | |
| webhook_failure | NWNX_ON_WEBHOOK_FAILURE | |
| name_reserve_bef | NWNX_ON_CHECK_STICKY_PLAYER_NAME_RESERVED_BEFORE | |
| name_reserve_aft | NWNX_ON_CHECK_STICKY_PLAYER_NAME_RESERVED_AFTER | |
| lvl_up_bef | NWNX_ON_LEVEL_UP_BEFORE | |
| lvl_up_aft | NWNX_ON_LEVEL_UP_AFTER | |
| lvl_upauto_bef | NWNX_ON_LEVEL_UP_AUTOMATIC_BEFORE | |
| lvl_upauto_aft | NWNX_ON_LEVEL_UP_AUTOMATIC_AFTER | |
| lvl_down_bef | NWNX_ON_LEVEL_DOWN_BEFORE | |
| lvl_down_aft | NWNX_ON_LEVEL_DOWN_AFTER | |
| inv_add_bef | NWNX_ON_INVENTORY_ADD_ITEM_BEFORE | |
| inv_add_aft | NWNX_ON_INVENTORY_ADD_ITEM_AFTER | |
| inv_rem_bef | NWNX_ON_INVENTORY_REMOVE_ITEM_BEFORE | |
| inv_rem_aft | NWNX_ON_INVENTORY_REMOVE_ITEM_AFTER | |
| add_gold_bef | NWNX_ON_INVENTORY_ADD_GOLD_BEFORE | |
| add_gold_aft | NWNX_ON_INVENTORY_ADD_GOLD_AFTER | |
| add_gold_bef | NWNX_ON_INVENTORY_REMOVE_GOLD_BEFORE | |
| add_gold_aft | NWNX_ON_INVENTORY_REMOVE_GOLD_AFTER | |
| pvp_chgatt_bef | NWNX_ON_PVP_ATTITUDE_CHANGE_BEFORE | |
| pvp_chgatt_aft | NWNX_ON_PVP_ATTITUDE_CHANGE_AFTER | |
| input_walk_bef | NWNX_ON_INPUT_WALK_TO_WAYPOINT_BEFORE | |
| input_walk_aft | NWNX_ON_INPUT_WALK_TO_WAYPOINT_AFTER | |
| material_chg_bef | NWNX_ON_MATERIALCHANGE_BEFORE | |
| material_chg_aft | NWNX_ON_MATERIALCHANGE_AFTER | |
| input_atk_bef | NWNX_ON_INPUT_ATTACK_OBJECT_BEFORE | |
| input_atk_aft | NWNX_ON_INPUT_ATTACK_OBJECT_AFTER | |
| force_move_bef | NWNX_ON_INPUT_FORCE_MOVE_TO_OBJECT_BEFORE | |
| force_move_aft | NWNX_ON_INPUT_FORCE_MOVE_TO_OBJECT_AFTER | |
| obj_lock_bef | NWNX_ON_OBJECT_LOCK_BEFORE | |
| obj_lock_aft | NWNX_ON_OBJECT_LOCK_AFTER | |
| obj_unlock_bef | NWNX_ON_OBJECT_UNLOCK_BEFORE | |
| obj_unlock_aft | NWNX_ON_OBJECT_UNLOCK_AFTER | |
| uuid_coll_bef | NWNX_ON_UUID_COLLISION_BEFORE | |
| uuid_coll_aft | NWNX_ON_UUID_COLLISION_AFTER | |
| resource_added | NWNX_ON_RESOURCE_ADDED | |
| resource_removed | NWNX_ON_RESOURCE_REMOVED | |
| resource_modified | NWNX_ON_RESOURCE_MODIFIED | |