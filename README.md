## spawn_mobs_mcpi [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/Will-777/spawn_mobs_mcpi.git)

Python script to spawn some mobs in your Minecraft Pi world


### Table of Contents
 - [What you need](### What you need)
 - [How to install ](### How to install )
 - [How to use the script ](### How to use the script)
  - [Ignore Whitespace](#ignore-whitespace)

*Read this in other languages: [English](README.md), [French](README.fr.md), [日本語](README.ja.md).*

### What you need
A Raspberry Pi :sparkles: with Raspbian installed.
Minecraft Pi is installed by default.

### How to install 

We open a Terminal session to do it with command line

 1 .In your Raspberry Pi, start a Terminal session.

We go in the folder we chose for the install (ex: desktop)

 2 .type the following command
```bash
$ git clone https://github.com/Will-777/spawn_mobs_mcpi.git
$ cd ~
```
You should have a folder in your Raspberry Pi Pi desktop.

### How to use the script 
Just Launch it with right click "open" and F5 ...
I will explain that with the next update.


### Examples part ###
From Raspberry Pi
-----------------
Be sure that Minecraft Pi game is turned Off.
1) Select your world from the menu
 example : from the menu, press 2 and enter.

2) give a name to your file first (e.g. myMCPI) by typing this command.
 myMCPI can be name you want.
```python
>>> myMCPI = mcpi_mobs_mgr()
```

3) Add mobs by typing
```python
>>> myMCPI.addMob("Pig", 10)
```
 x, y, z coordinate not implemented yet. Sorry.
 If you go around POS: 26.1 / 14.5 / -25.6
 you will find the Mobs you added.

4.1) check how many mobs will be inside your world.
```python
 >>> myMCPI.Mobs_howMany()
 >>> myMCPI.Mobs_show_stats()
 >>> myMCPI.Mobs_list_display()
```
4.2) and if you are really curious, look Binary representation of entities.dat file.
```python
>>> myMCPI.NBT_Header
>>> myMCPI.NBT_Body
```

5) Save your change.
```python
>>> myMCPI.saveNewFile()
```
6) Start Minecraft Pi game and select your world.

7) you cannot kill Mobs with weapons. You need to use dynamite.
 some Mobs like Skeletons will die (because of the sun ?)
 There is a way to turn your Minecraft Pi world as survival mode.
 There is a way to patch with Binary Patch your Minecraft Pi and unlock Craft
 and your own inventory.
 I didn't find the way to be able to kill Mobs in the game with your weapon.

### Additional info : Comment this line for windows tests only
```python
>>> mcpi_world_path = 'C:\Users\username\myFile\Programming\Python\MCPI'
```


### Things I need to do still..
- [ ] Correct the bugs you will find.
- [ ] save poor skelets that are dieing too fast.
- [ ] find why we cannot shoot mobs.
- [ ] add x, y, z for spawning Mobs

### and remember :
  - :chicken: Little Endian = 20 00 00 00
  -  :cow: Little Endian = 20 00 00 00
  -  :sheep:
  -  ::


Enjoy ! :+1:



