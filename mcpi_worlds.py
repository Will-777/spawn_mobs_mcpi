"""
MCPI Mobs Manipulator
Description :
    this script is to manipulate Mobs into Minecraft Raspeberry Pi version
    wellknown as MCPI.
    Here the possible task you can do :
        -List of existing Mobs into the world (by default 0)
        -add mobs
        -display details about mobs.
        -remove mobs
        
Author : Skeleton
Contact :
    
Date & Version :    May 2016 / beta0.1
Updates : 
    

How does it work ?
type the following command :
>>> get_current_user()
'pi'
>>> make_MCPI_path()
'/home/pi/.minecraft/games/com.mojang/minecraftWorlds'
>>> mcpi_directory = make_MCPI_path()
>>> checkMCPI_World(mcpi_directory)
['/home/pi/.minecraft/games/com.mojang/minecraftWorlds',
'/home/pi/.minecraft/games/com.mojang/minecraftWorlds/world----',...] 
>>> mcpi_worlds = checkMCPI_World(mcpi_directory)
>>> selectMCPI_World(mcpi_worlds)
List of MCPI worlds
[0] /home/pi/.minecraft/games/com.mojang/minecraftWorlds
[1] /home/pi/.minecraft/games/com.mojang/minecraftWorlds/world----
[2] /home/pi/.minecraft/games/com.mojang/minecraftWorlds/world-
...
Select the MCPI world : 2
 MCPI world selected
'/home/pi/.minecraft/games/com.mojang/minecraftWorlds/world'


"""

import os
import getpass #to define current user

mcpi_exist_path = ''
mcpi_select_world = ''
mcpi_directory = ''


def get_current_user():
    return getpass.getuser()


def make_MCPI_path():
    '''
    Output : the proper path of MCPI world according user
    '''
    global mcpi_directory
    mcpi_user = get_current_user()
    mcpi_directory = "/home/%s/.minecraft/games/com.mojang/minecraftWorlds" % (mcpi_user)
    return mcpi_directory


def checkMCPI_World(mcpi_directory):
    '''
    Check the existing MCPI world
    by default, MCPI folders for words is :
    /home/pi/.minecraft/games/com.mojang/minecraftWorlds
    Input : mcpi_directory = make_MCPI_path().
    Output : will return a List
    '''
    
    os.walk(mcpi_directory)
    mcpi_worlds = [x[0] for x in os.walk(mcpi_directory)]

    #mcpi_worlds.remove('') 

    return mcpi_worlds



def selectMCPI_World(mcpi_worlds):
    '''
    Assist to select the existing MCPI world from existing ones.
    Input : mcpi_worlds = checkMCPI_World(mcpi_directory).
    Output : return a string for selected folder path.
    '''
    while True:
        path_id = 1
        print 'List of MCPI worlds'
        for i in mcpi_worlds[1:]:
            print '[%d] %s' % (path_id, i)
            path_id += 1

        if mcpi_worlds == []:
            print "ERROR: There is currently no world created under your account. "
            print "Path : \n %s" % (mcpi_directory)
            print "Selection aborted but you can still manully use commands."
            break

            
        #MCPIworld_choice = int(raw_input('Select the MCPI world : '))
        MCPIworld_choice = input('Select the MCPI world : ')
        #assert (mcpi_worlds[MCPIworld_choice]), "Wrong selection ! Please try again."
        
        try:
            mcpi_worlds[MCPIworld_choice]
        except IndexError:
            print 'Wrong selection ! Please try again. \n'
            
        else:
            print '\n MCPI world selected :\n' + str(mcpi_worlds[MCPIworld_choice]) 
            return mcpi_worlds[MCPIworld_choice]


def renameMCPI_World(mcpi_selected_world):
    '''
    input : mcpi_selected_world = selectMCPI_World(mcpi_worlds)
    output : none. (but changed the name)
    
    '''

    return "Sorry, not yet implemented."


def get_MCPI_Help():
    return "Do you need help ?! Uh ?"


