## spawn_mobs_mcpi [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/Will-777/spawn_mobs_mcpi.git)

Python script to spawn some mobs in your Minecraft Pi world.
Animals and monsters... yeah everything's OK!
Impossible right ? Hum... well... just follow the below instructions then!


### Table of Contents
 - [What you need](https://github.com/Will-777/spawn_mobs_mcpi#what-you-need)
 - [How to install ](https://github.com/Will-777/spawn_mobs_mcpi#how-to-install)
 - [How to use the script ](https://github.com/Will-777/spawn_mobs_mcpi#how-to-use-the-script)

*Read this in other languages: [English](README.md), [French](README.fr.md), [日本語](README.ja.md).*

### What you need
A Raspberry Pi :sparkles: with Raspbian installed.
Minecraft Pi is installed by default.

### How to install 

We open a Terminal session to do it with command line

 1. In your Raspberry Pi, start a Terminal session.

We go in the folder we chose for the install (ex: desktop)

 2. type the following command
```bash
$ git clone https://github.com/Will-777/spawn_mobs_mcpi.git
$ cd ~
```
You should have a folder in your Raspberry Pi Pi desktop.

### How to use the script 
in your downloads, you should have a folder nammed "spawn_mobs_mcpi".
Have a look inside and search "mcpi_mobs.py".
Just Launch it with right click and "open"/"Python2 IDLE" 
You should have a window with the code. Then press F5 to launch it.
I will try to provide some details on the next update...


### Examples part ###
From Raspberry Pi
-----------------
Be sure that your Minecraft Pi game is turned Off.
This process is Offline.  

1) Select your world from the menu according its number
 example : from the menu, press "2" and enter.

2) You have now the Python prompt. Give a name to your file first (e.g. myMCPI) by typing this command.
 myMCPI can be replaced by any name you want.
```python
>>> myMCPI = mcpi_mobs_mgr()
```

3) Add mobs by adding .addMob to your world, write the type and how many mobs you want.
```python
>>> myMCPI.addMob("Sheep", 10)
>>> myMCPI.addMob("Chicken", 10)
>>> myMCPI.addMob("Skeleton", 10)
>>> myMCPI.addMob("Cow", 10)
>>> myMCPI.addMob("Creeper", 10)
>>> myMCPI.addMob("Spider", 10)
>>> myMCPI.addMob("Pig", 10)
>>> myMCPI.addMob("Zombie", 10)
>>> myMCPI.addMob("Zombie Pigman", 10)

```
 x, y, z coordinate not implemented yet. Sorry.
 If you go around POS: 26.1 / 14.5 / -25.6 on your map
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

5) Save your change. You are done with the Python script.
```python
>>> myMCPI.saveNewFile()
```
6) Start Minecraft Pi game from the menu and select the world you changed.

7) Please note that you cannot kill Mobs with weapons. You need to use dynamite.
 some Mobs like Skeletons will die (because of the sun ?)
 Mobs might hrt each others with arrows or their attacks.
 There is a way to turn your Minecraft Pi world as survival mode.
 There is a way to patch with Binary Patch your Minecraft Pi and unlock Craft
 and your own inventory.
 I didn't find the way to be able to kill Mobs in the game with "Steve's weapons".
 If you search by your own, you might be able to change steve's armor !^^

### Additional info : Comment this line for windows tests only
```python
>>> mcpi_world_path = 'C:\Users\username\myFile\Programming\Python\MCPI'
```


### Things I need to do still..
- [ ] Correct the bugs you will find.
- [ ] add x, y, z for spawning Mobs
- [ ] add function to change your Armor by what you want.
- [ ] save poor skelets that are dieing too fast.
- [ ] find why we cannot shoot mobs.
- [ ] Your imagination and beyond ..!

### and remember :
  - [![chicken-emoticon-by-pwassonne-d7ua2ro.png](https://i.postimg.cc/3RZ762KD/chicken-emoticon-by-pwassonne-d7ua2ro.png)](https://postimg.cc/PpNBvpvt) Little Endian = 0A 00 00 00
  -  [![cow-emoticon-by-pwassonne-d6vg79i.png](https://i.postimg.cc/J40m6ySG/cow-emoticon-by-pwassonne-d6vg79i.png)](https://postimg.cc/nMy6MLFJ) Little Endian = 0B 00 00 00
  -  [![pig-emoticon-by-pwassonne-d7ua25h.png](https://i.postimg.cc/qBj4xcbP/pig-emoticon-by-pwassonne-d7ua25h.png)](https://postimg.cc/fktGwdhC) Little Endian = 0C 00 00 00
  -  [![white-sheep-emoticon-by-pwassonne-d6zh0rh.png](https://i.postimg.cc/C5P0MYnh/white-sheep-emoticon-by-pwassonne-d6zh0rh.png)](https://postimg.cc/XBCmxRgm) Little Endian = 0D 00 00 00
  -  [![zombie-emoticon-by-pwassonne-d61ooul.png](https://i.postimg.cc/V6wmDKc8/zombie-emoticon-by-pwassonne-d61ooul.png)](https://postimg.cc/kVT05F41) Little Endian = 20 00 00 00
  -  [![d3compr-3780ca39-76d2-42cd-b8eb-da79c0d4cabd.gif](https://i.postimg.cc/qv9kCkbg/d3compr-3780ca39-76d2-42cd-b8eb-da79c0d4cabd.gif)](https://postimg.cc/Yvzc5www) Little Endian = 21 00 00 00
  -  [![skeleton-emoticon-by-pwassonne-d61oncm.png](https://i.postimg.cc/VNnzq3pg/skeleton-emoticon-by-pwassonne-d61oncm.png)](https://postimg.cc/p9VNx125) Little Endian = 22 00 00 00
  -  [![spider-emoticon-by-pwassonne-d65p64o.png](https://i.postimg.cc/j2dKrC53/spider-emoticon-by-pwassonne-d65p64o.png)](https://postimg.cc/S25H6Scc) Little Endian = 23 00 00 00
  -  [![zombie-pigman-emoticon-by-pwassonne-d6q6au3.png](https://i.postimg.cc/4ytvs4St/zombie-pigman-emoticon-by-pwassonne-d6q6au3.png)](https://postimg.cc/Fkrkxvms) Little Endian = 24 00 00 00


Enjoy ! :+1:



