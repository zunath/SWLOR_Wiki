---
title: Lightsaber Guide
description: Quickly getting new saber parts into the HAKs.
published: true
date: 2025-10-10T18:16:39.873Z
tags: lightsaber, development, weapon, hak
editor: markdown
dateCreated: 2025-10-10T18:16:32.882Z
---

So you want to add new lightsabers? 

Woe upon you, ye who follow this guide.
It’s not actually that bad.

This guide doesn’t go into blender or editing the actual models. It assumes you have your .mdl files and .tga files ready to go. If you need a guide on prepping your 3d models for NWN please reference Xisifer’s fantastic guide here: https://youtu.be/vnetHQK2yjQ


## **Step 1: Naming Scheme**


Your weapon needs to follow the naming scheme present in baseitems.2da.

For this example we’ll be making a new lightsaber, so the first part of the .mdl name will have to be “wswglsbr” (You can find this on line 516 of the baseitems.2da under the ItemClass column).


Secondly, we need to define what part it will be under. Weapons are typically made of 3 parts. The Top, Middle, and Bottom parts. For lightsabers, we only use the Top and Bottom (Blade and Hilt).

If you’re making a blade, which we are for this example, you’ll use _t_ to specify that. If you’re making a hilt, use _b_

And finally, the toolset reads these parts based on the numbers you assign to them. In this case we’ll want to make a new section for 5 new blades, model 5, with 5 additional colours.
![weaponguide1.png](/weaponguide1.png)

To do this, we give the .mdl a number at the end. 051

The toolset will read “05” as “Model 5” and make a new category if there isn’t one. It will then read “1” as “Colour 1”.

Important note: you need an icon for it to appear in the toolset properly. Icons will be the same name as your .mdl file but with an i at the start. You will need an icon for every part.

For example, the icon for our new part would be: iwswglsbr_t_051

So your .mdl file name should be wswglsbr_t_051







## Step 2: Get it in the toolset

Now that your model file is prepared properly, you can put it into: SWLOR_NWN > SWLOR_Haks > swlor2_mdl

![image.png](/image.png)

Make sure to put your .tga files and icons into SWLOR_NWN > SWLOR_Haks > swlor2_tga.
![weaponguide2.png](/weaponguide2.png)

Now open Visual Studio and rebuild your SWLOR.Game.Server which will compile the haks for you as well.
![weaponguide3.png](/weaponguide3.png)

Once your rebuild is finished, go and open up the toolset. Spawn in a lightsaber and you should see now your new Model number is there as well as your new colour(s).
![weaponguide4.png](/weaponguide4.png)


Good job, your glowstick works! You’re not quite done yet though.





## Step 3: Compile your model

```::---###############-############-#########-######-###
@echo off
setlocal enabledelayedexpansion
::---###############-############-#########-######-###

call :void_main >"%~n0.log" 2>&1

                goto :end
::---###############-############-#########-######-###

:void_main

rem set "CWD=C:\Users\[user]\Beamdog Library\00785\bin\win32\"
set "CWD=D:\SteamLibrary\steamapps\common\Neverwinter Nights\bin\win32" 

for %%F in ("development\*.mdl") do (
    START "" /D "%CWD%" /WAIT /MIN /HIGH nwmain.exe compilemodel "%%~nF"
)

               goto :eof
::---###############-############-#########-######-###

:end
```

AHHHHHH scary CODE. Take this and put it into a notepad save as a .cmd, make sure you change it to point at your Neverwinter Nights/bin/win32 directory in the file itself, and save it into your Documents/Neverwinter Nights folder.


Put all of your .mdl files into your development folder, then run the .cmd file you just made.

It’ll hang for a few seconds or a few minutes, then once it closes your models will be compiled. (This turns then from ASCII to Binary).

Now you can push your changes in GitHub! Here’s a quick overview of that:

![weaponguide5.png](/weaponguide5.png)

Create a new branch, make sure to bring any changes with you when you make it.

Confirm your files changes are present on the changed files side (left hand bar)

![weaponguide6.png](/weaponguide6.png)

Give your commit a summary and a description, then push it!


















“LazyTrain I want to make a new Lightsaber but blender and emitters scare the shit out of me” Good news! You don’t need to touch most of that.

## Quick and Easy TGA Editing for new saber colours.

![weaponguide7.png](/weaponguide7.png)
Lightsaber colours are easy! Open NWNExplorer and open up swlor2_tga.hak.
![weaponguide8.png](/weaponguide8.png)
CTRL + S to search “lsbr_011” and this should take you directly to the .tga used to control the lightsaber colours. 

For this demonstration, we’ll be using lsbr_012.tga. The blue one. Right click the .tga in the sidebar and click “export .tga” Save it somewhere you’ll remember.

![weaponguide9.png](/weaponguide9.png)

Once you’ve exported the .tga, open it in any program of your choosing. Clip Studio & GIMP can handle .tga files just fine, in my experience. I’m sure Photoshop and other programs also work.

![weaponguide10.png](/weaponguide10.png)

From here, you simply need to change the .tga colour to your desired new lightsaber colour. You can do this many ways, but the easy way is to use your chosen program’s Hue/Saturation/Luminosity editor which is fairly standard in most art programs. Make sure the white core stays intact, touch it up if you need to.
![weaponguide11.png](/weaponguide11.png)
A few quick tweaks and we have a deep purple saber. 
From here, you export the image as a .tga file again. Make sure to give it a new number at the end. 
![weaponguide12.png](/weaponguide12.png)
Filetype Targa, if your program is weird and uses its Government name.

Alternatively, if you’re just testing to make sure it looks good, keep the same number and put it in your documents/neverwinter nights/development folder. Give yourself a lightsaber with the blue blade in the toolset, then when you load it to test the development folder with override it and show you your fancy purple blade. 

And that’s it! You did it!
