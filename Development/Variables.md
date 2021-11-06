---
title: Variables
description: 
published: true
date: 2021-11-06T20:27:20.027Z
tags: 
editor: markdown
dateCreated: 2021-11-06T20:15:29.615Z
---

# Variables

## Animation Events

Sourced from the [AnimationEvent](https://github.com/zunath/SWLOR_NWN/blob/feature/ffo-rewrite/SWLOR.Game.Server/Service/AnimationService/AnimationEvent.cs) enum-ish class

#### Use
In the toolkit, pick any of the supported Event Types (more can be added with a small amount of development work for existing NWNX Events)

Add at least the variable `<animationEventName>_vfx_id`, where Id is the int of the Vfx to run and the animationEventName is one from this list:

- crea_attacked_vfx
- crea_perception_vfx
- crea_roundend_vfx
- crea_damaged_vfx
- crea_death_vfx

It is also possible to modify the duration `(DurationType)` or scale `(Float)`by replacing \_id with \_dur or \_scale

eg,
`crea_attacked_vfx_dur` or `crea_attacked_vfx_scale`


The code also supports attaching these animations in the spawner:  [Link](https://github.com/zunath/SWLOR_NWN/blob/feature/ffo-rewrite/SWLOR.Game.Server/Feature/SpawnDefinition/CZ220SpawnDefinition.cs)

```cs
                .PlayAnimation(DurationType.Instant, AnimationEvent.CreatureOnDeath, VisualEffect.Fnf_Fireball)
```

#### Code
```cs
        public string IdKey { get { return $"{Value}_id"; } }
        public string DurationKey { get { return $"{Value}_dur"; } }
        public string ScaleKey { get { return $"{Value}_scale"; } }

        public static AnimationEvent CreatureOnAttacked { get { return new AnimationEvent("crea_attacked_vfx"); } }
        public static AnimationEvent CreatureOnPerceive { get { return new AnimationEvent("crea_perception_vfx"); } }
        public static AnimationEvent CreatureOnRoundEnd { get { return new AnimationEvent("crea_roundend_vfx"); } }
        public static AnimationEvent CreatureOnDamaged { get { return new AnimationEvent("crea_damaged_vfx"); } }
        public static AnimationEvent CreatureOnDeath { get { return new AnimationEvent("crea_death_vfx");  } }
```
