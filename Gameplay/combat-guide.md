---
title: Combat Guide
description: How combat works in SWLOR
published: true
date: 2022-01-15T12:12:29.273Z
tags: guides combat mechanics
editor: markdown
dateCreated: 2021-12-20T23:52:11.721Z
---

# Combat Mechanics
> This article is DRAFT.  The mechanics are very likely to change before the release of Revamp as we go through testing. 
{.is-warning}

SWLOR uses entirely custom mechanics for attack rolls and for damage rolls.  So forget everything you know about Neverwinter Nights and D&D 3rd edition... and welcome to the frontier!

## Principles of the combat system
Four attributes are relevant to combat.
* Might (MGT), formerly known as Strength
* Perception (PER), formerly known as Dexterity
* Willpower (WIL), formerly known as Wisdom
* Vitality (VIT), formerly known as Constitution

In general, any given combat event will be a contest between the attacker and defender each using one attribute.  For attack rolls, this will typically be a symmetrical contest of MGT, PER or WIL - MGT for a trial of strength, PER where situational awareness is key, and WIL for mental battles. For damage rolls, this will typically be the attacker using MGT, PER or WIL against the defender's VIT or WIL. 

VIT, in general, is not used for attack rolls, but is most commonly used to resist damage - as well as heavily influencing how many HP the character has.

## Hitting Things

The base attack roll is a d100 vs a target of 50.  This roll is modified by the attacker's attribute modifier, the defender's attribute modifier, and various bonuses and penalties from feats, effects and item properties. 

Note that most combat skills (activated abilities) don't have a to hit roll. See [Combat Skills](/Gameplay/combat-skills) for details of what abilities are available to different weapons. 

Attacking placeables does not require a roll to hit.  Inanimate objects are hit automatically (and the attack cannot be a critical hit). 

### Attribute Modifiers

There are three basic types of attack in SWLOR - Melee, Ranged and Spirit.  
* Melee attacks use the attacker's Might vs the defender's Might. 
* Ranged attacks use the attacker's Perception vs the defender's Perception.
* Spirit attacks use the attacker's Will vs the defender's Will.

So the difficulty to hit a target will be based on the type of attack you're using and how strong the target is in that attribute.  You might end up switching attack type to be able to hit a creature where it's vulnerable.

Each point of attribute modifier makes a 10% difference to the roll (+ or - 10 to the d100 roll).  So if it's a Melee attack, and the attacker has 14 (+2) Mgt and the defender has 10 (+0) Mgt, the attacker will get +20 to their roll. If the attacker has 14 Mgt and the defender has 16 Mgt, the attacker will get -10 to their roll.

### Other bonuses and penalties

As you'd expect, there are a great many other things which can modify combat.  In general, an ability that gives +1 to hit in NWN will instead give +5 to the attack roll.  Thus, the penalty for dual wielding light weapons with Ambidexterity and Two Weapon Fighting in NWN is -2/-2.  Here, that corresponds to -10 on each attack roll.

Some abilities or weapons might change the base attribute type used for the attack.  The Weapon Finesse ability, for example, switches both the attacker and defender to use Perception instead of Might for attacks with relevant weapons.  Similarly, a weapon might use an unusual attribute, such as a Force vibroblade that changes the contest to one of Will.

Lastly, the system supports a couple of modifiers that are not normally in NWN.
* Ranged weapons will have a range penalty at very short or at longer ranges.  The Point Blank Shot feat turns the short range penalty into a bonus as usual.  A range over 20m applies -5 to hit, increasing to -10 at 30m and -20 at 40m. 
* In addition to the usual flanking bonus, there is a +30 modifier to hit if you're attacking an enemy from behind.  (This doesn't apply any extra damage, just means you're more likely to hit).  A swarm of creatures is therefore more likely to land blows than an individual creature, and a warrior who uses positioning to their advantage can outmaneuver even a stronger enemy.

### Critical Hits
A Critical Hit happens if the attacker exceeds the target number by the necessary amount.  Critical hits are automatic; there is no confirmation roll.

The base critical range is 40, i.e. if the attacker's modified roll is 90+, a critical hit is scored.  Improving the critical range reduces this by 10 points for each point of critical threat.  So a 19-20 critical range translates into a critical range of 30... and a 17-20 critical range translates into a critical range of 10.

This means that if you are much stronger than the target in the attributes used for the contest, you are likely to score a lot of critical hits.  Similarly, if you are much weaker, you are unlikely to score any critical hits.

### Display of attack rolls
Due to limitations in the engine, we can't show the full numbers used in the calculation.  Instead, the numbers shown are 1/4 of the numbers used in the calculation. So if you roll 80 on your d100 and have +20 in modifiers, this will show as (20 + 5 = 25) in the attack roll calculation.  A hit is therefore scored on a roll of (50/4 = 12.5) or more. 

The critical 'roll' will just show how much your roll exceeded the critical number by.

## Damaging Things

The damage roll on SWLOR is also highly customised.  Damage is based on four things.
* The base DMG rating of the attack.
* The Defense of the target against that sort of attack (min 5).
* The attacker's attribute used to power the attack.
* The defender's attribute used to resist the attack.

The base equation is 
>damage = (75%-100% of) 100 * DMG/defense * (AttackAttr+5)/(DefendAttr+5).

So, a weapon with base Damage rating 1.5 against a target with Defense 5, where both sides have equal attributes, does 100 * 1.5/5 = (75%-100% of) 30 damage per hit. 

### Attributes
In regular combat, the following attributes are used.
Melee: attacker's MGT modifier, defender's VIT modifier
Ranged: 25% of the weapon's DMG modifier is used in place of the attacker's modifier.  The defender still uses VIT.
Spirit: attacker's WIL modifier, defender's WIL modifier.

However, for combat skills, a wide range of different attribute pairings are possible. For example, the Saber Strike ability uses the attacker's WIL and the defender's VIT.

### Modifiers
Various things can modify the damage roll.  The most common ones are:
* Using a heavy weapon increases the attacker's attribute modifier by 50% - so if you have 14 MG (+2) your MGT will be counted as +3 for the purpose of damage calculations.
* Power Attack increases base DMG by +1.
* Improved Power Attack increases base DMG by +2.5.
* The Weapon Specialisation feat increases base DMG by +0.5.

### Critical Hits
A critical hit increases damage as follows.
* The minimum damage changes from 75% of the number above to 100%.
* THe maximum damage is increased by 25% for each point of critical multiplier over x1.
Therefore, a critical hit from a x3 weapon such as an axe, does 100%-150% of damage. With feats to improve your critical multiplier to x4, this rises to 100%-175%. Ouch.

### Damage from Abilities
Abilities, like Double Shot for pistols or Throw Lightsaber for Force, also have DMG ratings and do DMG in a very similar way to weapons.  There are two ways in which ability damage differs slightly from regular attacks.
* Abilities do not normally have a to-hit roll.  Some Force abilities have a resistance check, which works similarly to an attack roll (opposed WIL). 
* Abilities get a DMG bonus equal to 0.15 * the skill level of the user. So if you have 10 Force and use Throw Lightsaber, you will add 1.5 DMG to your Throw Lightsaber's damage rating. 
