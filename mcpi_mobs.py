"""
MCPI Mobs (Kind of Editor)

Description :
    this script is to help you to add some Mobs into Minecraft Raspeberry Pi version
    wellknown as MCPI.
    Here the possible task you can do :
        -List of existing Mobs into the world (by default 0)
        -add mobs
        -display details about mobs.

Author : Skeleton
Date & Version :    September 2016 / beta0.1
Updates : coming one day maybe.

Requirement :   Raspberry Pi
                Minecraft Pi (included with Raspbian).
Input : entities.dat file
Output : entities.dat file with mobs

Process to install from GitHub explained here:
git clone https://github.com/Will-777/spawn_mobs_mcpi.git

To make a local test under windows, you can use file path as following:
 mcpi_world_path = 'C:\Users\username\myFiles\Programming\Python\MCPI'

In the end of this file in comment, you have an example of how to use
this script, command 1 by 1.

Enjoy.
Skel.
P.s : Sorry, it is very ver poor implementation of NBT...
If I have time one day, I will try to have a better look into that.

"""
import os
import binascii
import datetime
import array
import struct
import string
# import getpass #to define current user

try:
    from mcpi_worlds import *
    print "Import of mcpi_worlds: OK !"
except ImportError:
    # log.debug('Import of mcpi_worlds: FAILED!', exc_info=True)
    print "Import of mcpi_worlds: *** FAILED ***"


mobs_pass_dict = {'Chicken' : b'\x0A\x00\x00\x00', 'Cow' : b'\x0B\x00\x00\x00',
                  'Pig' : b'\x0C\x00\x00\x00', 'Sheep' : b'\x0D\x00\x00\x00' }

mobs_agress_dict = {'Zombie' : b'\x20\x00\x00\x00', 'Creeper' : b'\x21\x00\x00\x00',
                    'Skeleton' : b'\x22\x00\x00\x00', 'Spider' : b'\x23\x00\x00\x00',
                    'Zombie Pigman' : b'\x24\x00\x00\x00'}

mobs_all_dict = dict(mobs_pass_dict, **mobs_agress_dict)

print "Welcome to Minecraft Pi Mobs manager."
print "<-- For additional help, use : get_MCPI_Help() -->\n"
# make_MCPI_path()
mcpi_directory = make_MCPI_path()
mcpi_worlds = checkMCPI_World(mcpi_directory)
mcpi_world_path = selectMCPI_World(mcpi_worlds)
# Manually select the world you want to modify.

def insert_spaces(text, s_range):
        return ' '.join(text[start:end] for start, end in 
                        zip([0] + s_range, s_range + [len(text)])).strip()

def manual_display():
    # You can use local path for test
    # mcpi_world_path = 'C:\Users\username\myFiles\Programming\Python\MCPI'
    with open(mcpi_world_path+'/entities.dat','rb+') as entitiesFile:
        content = entitiesFile.read()
        content = insert_spaces(content, range(0, 27, 2))
        # content = insert_spaces(content, range(0, 4, 2))
        print binascii.hexlify(content)


def read_entities(filename='entities.dat'):
    with open(mcpi_world_path+'/'+filename,'rb+') as entitiesFile:
        entitiesFileData = entitiesFile.read()
    return entitiesFileData


def about_mobs(dic1 = mobs_pass_dict, dic2 = mobs_agress_dict):
    for i in dic1:
        print str(i) + ' -> ' + binascii.b2a_hex(dic1.get(i))
    for i in dic2:
        print str(i) + ' -> ' + binascii.b2a_hex(dic2.get(i))
    return


class mcpi_mobs_mgr(object):    
    global Mobs_ID
    Mobs_ID = b'\x69\x64'

    def __init__(self, filename ='entities.dat'):
        self.filename = filename
        # For Data
        self.entitiesFile = open(mcpi_world_path+'/'+ self.filename, 'rb+')
        self.entitiesFileData = self.entitiesFile.read()

        # for menu confirmation
        self.yes = ['yes', 'y', 'ye', '']
        self.no = ['no', 'n']
        self.Mobs_ID = Mobs_ID

        # Header of the NBT file entities
        self.NBT_Header = self.entitiesFileData[:26]
        # Be careful : if you have items, you will have to adjust
        # The footer manually
        self.NBT_Footer = self.entitiesFileData[-22:]
        self.NBT_Body = self.entitiesFileData[26:-22]

    def __str__(self):
        """
        return message about type
        """
        return "This is ENTITIES.dat file. Really..."


    def NBT_PrintAll(self):
        """
        :return:
         the NBT info
        """
        NBT_ALL = self.NBT_Header + self.NBT_Body + self.NBT_Footer
        return ":".join("{:02x}".format(ord(c)) for c in NBT_ALL)
    

    #### MOBS List ####
    def Mobs_howMany(self, Mobs_toCheck = Mobs_ID):
        """
        :param Mobs_toCheck:
        :return:
         the number of mobs into this file.
        """
        number_of_Mobs = self.NBT_Body.count(Mobs_toCheck)
        return ('There is %d mobs/id into this file' % (number_of_Mobs))
    

    def Mobs_index(self):
        """
        :return:
         the list of Mobs index
        """
        return [i for i in range(len(self.NBT_Body)) if self.NBT_Body.startswith(self.Mobs_ID, i)]

    
    def get_Mobs_Hex_Val(self, MobType):
        """
        :input:
        :return: the Hex value according the mob type('pig', 'Cow', etc...)
        """
        MobType = MobType.title()
        try:
            return mobs_all_dict[MobType]
        except:
            return "Didn't find the hex code of the Mob you required." 
       

    def Mobs_list_make(self):
        """
        :return:
            list existing mobs in a world and print
        """
        myListOfMobs = self.Mobs_index()
        mobNumber = 0
        mobs_list_withIndex = []

        for i in myListOfMobs:
            mobNumber += 1
            # ascii_mobs_value = binascii.b2a_hex(entitiesFileData[i+2:i+6])
            index_of_mob = self.NBT_Body[i+2:i+6]
            try:
                type_of_Mob = mobs_all_dict.keys()[mobs_all_dict.values().index(index_of_mob)]
            except ValueError:
                type_of_Mob = 'Unknown Mob!'
            # print str(mobNumber) + ' - Index: ' + str(i) + ', ' + type_of_Mob
            mobs_list_withIndex.append((str(mobNumber), str(i) , type_of_Mob))

        return mobs_list_withIndex


    def Mobs_list_display(self):
        """
        Print the list of mobs inside
        """
        my_mobs_list = self.Mobs_list_make()
        print "   ID - Type  (Index)"
        print "---------------------"
        previous_Mobs = 0
        for each_mobs in my_mobs_list:
            # print each_mobs[0] + ' - ' + each_mobs[2] + ' ('+ each_mobs[1] +')'
            Mobs_size = int(each_mobs[1]) - previous_Mobs
            
            print('{:>5} - {} ({}), size:{}' .format(each_mobs[0], each_mobs[2], each_mobs[1], Mobs_size))
            previous_Mobs = int(each_mobs[1])


    def Mobs_show_stats(self):
        """
        return the number of mobs present on the map for each type of mobs.
        """
        my_mobs_list = self.Mobs_list_make()
        print "Inside this entities.dat file, there is : "
        
        for self.mobs_type in mobs_all_dict:
            mobs_total_number = 0
            
            for each_mobs in my_mobs_list:
                if  self.mobs_type == each_mobs[2]:
                    mobs_total_number += 1
            # print str(self.mobs_type) + ' = ' + str(mobs_total_number)
            print('{:>9} = {:<3}' .format(str(self.mobs_type), str(mobs_total_number)))


    #### MOBS ADD ####
    def addMob(self, Mob_Type = "Skeleton", Mob_Number=1, x=0, y=0, z=0):
        """
        add Mob(s) into your Minecraft Pi world.
        :param Mob_Type: Skeleton, Pig etc...
        :param Mob_Number: How many Mobs do you want to spawn
        :param x: NOT IMPLEMENTED YET
        :param y: NOT IMPLEMENTED YET
        :param z: NOT IMPLEMENTED YET
        :return: will add NBT info to body. return none

        """
        # Mobs_Separator
        NBTTAG_Mobs_Passive_Separator = "\x00\x03\x03\x00"
        # Another Mobs_Separator
        NBTTAG_Mobs_Separator_Last = "\x00\x02\x03\x00"

        # NUMBER OF MOBS HERE \x01 for 1x Mobs, \x02 for 2x, etc...
        # Number_Of_Mobs = "\n\xee\x00\x00" is your friend !
        NBTTAG_Number_Of_Mobs_Empty = "\x00\x01\x00\x00"
        NBTTAG_Number_Of_Mobs_One = "\n\x01\x00\x00"
        self.NBTTAG_Number_Of_Mobs_Any = "\n\xee\x00\x00"

        # Default position will be x = , y = , z =
        # "Pos\x05\x03\x00\x00\x00^W\x1bC\x00\x00\x86B\xd7\x07\xccB\t\x08\x00"

        Mobs_Template_random = "Age\x00\x00\x00\x00\x02\x03\x00" +\
                        "Air,\x01\x02\n\x00" +\
                        "AttackTime\x00\x00\x02\t\x00" +\
                        "DeathTime\x00\x00\x05\x0c\x00" +\
                        "FallDistance\x00\x00\x00\x00\x02\x04\x00" +\
                        "Fire\xff\xff\x02\x06\x00" +\
                        "Health\n\x00\x02\x08\x00" +\
                        "HurtTime\x00\x00\t\x06\x00" +\
                        "Motion\x05\x03\x00\x00\x00\x81\xc8\xcf\xbc.\x90\xa0\xbd\xf8\x13N=\x01\x08\x00" +\
                        "OnGround\x01\t\x03\x00" +\
                        "Pos\x05\x03\x00\x00\x00\xb3\xa4\x01C\x00\x00\x8eB\xa7\xe7\x04C\t\x08\x00" +\
                        "Rotation\x05\x02\x00\x00\x00\xf4\xc2\x0cB\x00\x00\x00\x00\x03\x02\x00" +\
                        "id\x0c\x00\x00\x00"

        Mobs_Template_Cow = "Age\x00\x00\x00\x00\x02\x03\x00" +\
                        "Air,\x01\x02\n\x00" +\
                        "AttackTime\x00\x00\x02\t\x00" +\
                        "DeathTime\x00\x00\x05\x0c\x00" +\
                        "FallDistance\x00\x00\x00\x00\x02\x04\x00" +\
                        "Fire\xff\xff\x02\x06\x00" +\
                        "Health\x06\x00\x02\x08\x00" +\
                        "HurtTime\x00\x00\t\x06\x00" +\
                        "Motion\x05\x03\x00\x00\x00\xc1@\xc4\t.\x90\xa0\xbd\xbd\x15l\t\x01\x08\x00" +\
                        "OnGround\x01\t\x03\x00" +\
                        "Pos\x05\x03\x00\x00\x00\x84@ C\x00\x00\x86B\x0fG\\xcdB\t\x08\x00" +\
                        "Rotation\x05\x02\x00\x00\x00ME\xd7Cl\x16\xe3?\x03\x02\x00" +\
                        "id\x0b\x00\x00\x00"

        # Default POS around : 26.1 / 14.5 / -25.6
        # "\n\x01\x00\x00\x00\x03\x03\x00" +\
        Mobs_Template_Pig = "Age\x00\x00\x00\x00\x02\x03\x00" +\
                            "Air,\x01\x02\n\x00" +\
                            "AttackTime\x00\x00\x02\t\x00" +\
                            "DeathTime\x00\x00\x05\x0c\x00" +\
                            "FallDistance\x00\x00\x00\x00\x02\x04\x00" +\
                            "Fire\xff\xff\x02\x06\x00" +\
                            "Health\x06\x00\x02\x08\x00" +\
                            "HurtTime\x00\x00\t\x06\x00" +\
                            "Motion\x05\x03\x00\x00\x00\x88\xc9\x05=.\x90\xa0\xbd\xbfq\x8b\xbc\x01\x08\x00" +\
                            "OnGround\x01\t\x03\x00" +\
                            "Pos\x05\x03\x00\x00\x00^W\x1bC\x00\x00\x86B\xd7\x07\xccB\t\x08\x00" +\
                            "Rotation\x05\x02\x00\x00\x00Fb\xd0D\x00\x00\x00\x00\x03\x02\x00" +\
                            "id\x0c\x00\x00\x00"

        #sheeps has 2x addition values = Sheared and Color
        mobs_Template_Sheep = "Age\x00\x00\x00\x00\x02\x03\x00" +\
                              "Air,\x01\x02\n\x00" +\
                              "AttackTime\x00\x00\x01\x05\x00" +\
                              "Color\x00\x02\t\x00" +\
                              "DeathTime\x00\x00\x05\x0c\x00" +\
                              "FallDistance\x00\x00\x00\x00\x02\x04\x00" +\
                              "Fire\xff\xff\x02\x06\x00" +\
                              "Health\x06\x00\x02\x08\x00" +\
                              "HurtTime\x00\x00\t\x06\x00" +\
                              "Motion\x05\x03\x00\x00\x00+hT=.\x90\xa0\xbd[\x05f\xbc\x01\x08\x00" +\
                              "OnGround\x01\t\x03\x00" +\
                              "Pos\x05\x03\x00\x00\x00\x05,\x1bC\x00\x00\x86B\x85\xf4\xceB\t\x08\x00" +\
                              "Rotation\x05\x02\x00\x00\x00,N\xbd\xc2\x00\x00\x00\x00\x01\x07\x00" +\
                              "Sheared\x00\x03\x02\x00" +\
                              "id\r\x00\x00\x00"

        # If it is Day time, Skelet are going to die quickly...
        # "\n\x02\x00\x00\x00\x02\x03\x00"
        mobs_Template_Skele = "Air,\x01\x02\n\x00" +\
                              "AttackTime<\x00\x02\t\x00" +\
                              "DeathTime\x00\x00\x05\x0c\x00" +\
                              "FallDistance\x00\x00\x00\x00\x02\x04\x00" +\
                              "Fire\xff\xff\x02\x06\x00" +\
                              "Health\x03\x00\x02\x08\x00" +\
                              "HurtTime\x07\x00\t\x06\x00" +\
                              "Motion\x05\x03\x00\x00\x00\xb5E\xf0\xbc.\x90\xa0\xbd&U\x13=\x01\x08\x00" +\
                              "OnGround\x01\t\x03\x00" +\
                              "Pos\x05\x03\x00\x00\x00\x07\x19\x1bC\x00\x00\x86B @\xd3B\t\x08\x00" +\
                              "Rotation\x05\x02\x00\x00\x00\xa0X\xcd@\x00\x00\xf0\xc1\x03\x02\x00" +\
                              'id"\x00\x00\x00\x00\x02\x03\x00' +\
                              "Air,\x01\x05\x0c\x00" +\
                              "FallDistance\x00\x00\x00\x00\x02\x04\x00" +\
                              "Fire\x00\x00\t\x06\x00" +\
                              "Motion\x05\x03\x00\x00\x00\xe4i\x94>g\x1bb?\xfe>\xac>\x01\x08\x00" +\
                              "OnGround\x00\t\x03\x00" +\
                              "Pos\x05\x03\x00\x00\x00\x08I\x1bC\xcd\xbe\x8aB:\xc3\xd3B\t\x08\x00" +\
                              "Rotation\x05\x02\x00\x00\x00f\xff" + '"B' + "\xff\x1a\x81B\x03\x02\x00" +\
                              "idP\x00\x00\x00\x01\x06\x00" +\
                              "inData\x00\x01\x08\x00" +\
                              "inGround\x00\x01\x06\x00" +\
                              "inTile\x00\x01\x06\x00" +\
                              "player\x00\x01\x05\x00" +\
                              "shake\x00\x02\x05\x00x" +\
                              "Tile\xff\xff\x02\x05\x00" +\
                              "yTile\xff\xff\x02\x05\x00" +\
                              "zTile\xff\xff"

        # Spider are "\n\x01\x00\x00\x00\x02\x03\x00" +\
        mobs_Templace_Spider = "Air,\x01\x02\n\x00" +\
                               "AttackTime\x00\x00\x02\t\x00" +\
                               "DeathTime\x00\x00\x05\x0c\x00" +\
                               "FallDistance\x00\x00\x00\x00\x02\x04\x00" +\
                               "Fire\xff\xff\x02\x06\x00" +\
                               "Health\x06\x00\x02\x08\x00" +\
                               "HurtTime\x00\x00\dt\x06\x00" +\
                               "Motion\x05\x03\x00\x00\x00\x0f)i$.\x90\xa0\xbdl\x0e\x1a\xa5\x01\x08\x00" +\
                               "OnGround\x01\t\x03\x00" +\
                               "Pos\x05\x03\x00\x00\x00\xb8\xfe\x13C\x00\x00\x8aB\xd9\xca\xacB\t\x08\x00" +\
                               "Rotation\x05\x02\x00\x00\x00\xbb\xb3\xbd\xc2\x00\x00\x00\x00\x03\x02\x00" +\
                               "id#\x00\x00\x00"

        NBTTAG_Default_Header = "ENT\x00\x01\x00\x00\x00\xea\x00\x00\x00\n\x00\x00\t\x08\x00Entities"
        NBTTAG_Default_Footer = "\x00\x00\x00\t\x0c\x00TileEntities\x01\x00\x00\x00\x00\x00"

        # Example of positions on Minecraft Pi world.
        # posA = "\x05\x03\x00\x00\x00^W\x1bC\x00\x00\x86B\xd7\x07\xccB\t\x08\x00"
        # posB = "\x05\x03\x00\x00\x00\xb8\xde\x1eC\x00\x00\x86B\xba\x8f\xcfB\t\x08\x00"
        
        # Put the first letter in maj and the rest in min
        Mob_Type = Mob_Type.title()
        
        if Mob_Type not in mobs_all_dict.viewkeys():
            print "Mob_Type value not recognized. Please use :"
            for keys in mobs_all_dict.keys():
                print keys
        else:
            # Assign the Mob ID
            # Mobs_id = mobs_all_dict.get(Mob_Type)
            # Check if the Mob is a Skeleton
            if Mob_Type == "Skeleton":
                Mobs_Template = mobs_Template_Skele
            # Check if the Mob is a Sheep
            elif Mob_Type == "Sheep":
                Mobs_Template = mobs_Template_Sheep
            # For all others Mobs
            else:
                Mobs_Hex_Val = self.get_Mobs_Hex_Val(Mob_Type)
                Mobs_Template = Mobs_Template_Pig
                Mobs_Template = Mobs_Template.replace('id\x0c\x00\x00\x00', 'id' + Mobs_Hex_Val)

            # if the MOB number list is empty, replace by a larger number
            # Default value b'\x01\x00\x00\x00' means Empty.
            # for reference the format is b'\x0n\xXX\x00\x00' with XX a number in Hex.
            if self.NBT_Body == NBTTAG_Number_Of_Mobs_Empty:
                self.NBT_Body = NBTTAG_Number_Of_Mobs_Any

            # Add the Mob to the NBT_Body
            for i in range(Mob_Number):
                self.NBT_Body += NBTTAG_Mobs_Passive_Separator + Mobs_Template

            print "Mob %s added %dx times to the body." % (Mob_Type, Mob_Number)
            print "Don't forget to save with saveNewFile()."
            print "Be careful: all or some of data previously"
            print "into your entities.dat file might be deleted."

        return 

    """
    #### MOBS DELETE ####
    # NOT Implemented yet
    # del a mob by ID
    def delMobByID(self, Mob_byID):
        '''
        Delete the Mobs from NBT file according its ID number from list.
        Input  : Mob_byID
        Output : Binary Data removal
        Var    :
            MobsIndex_current (int) 
            Mobs_size (int) size of the Mob.
            NBT_Pointer (int)
            NBT_MobsBody (str) the string that should be deleted.
        '''
        print "To see the MobID list, please use .Mobs_list_display()"
        MobsList_current = self.Mobs_list_make()
        # print "MobsList_current" , MobsList_current
        found_Mob_byID = False

        if int(Mob_byID) <= 0 :
            print "Mob_byID cannot be negative or egal to 0.\nAbort."
            return
        
        for Mobs in MobsList_current:
            if Mobs[0] == Mob_byID:
                #m ake the magic
                found_Mob_byID = True
                MobsIndex_current = MobsList_current.index(Mobs)
                if MobsIndex_current <= 1 :
                   Mobs_size = int(MobsList_current[MobsIndex_current][1]) 
                else:
                    # If exist Mob_byID-1 means not the end of the file
                    Mobs_size = int(MobsList_current[MobsIndex_current][1]) - int(MobsList_current[MobsIndex_current-1][1])
                print "Info about the mob : %s, size(%s)" % (Mobs[2], Mobs_size )
                NBT_Pointer = int(Mobs[1])
                print "NBT_Pointer" , NBT_Pointer

        if not found_Mob_byID :
            print "Sorry: cannot find existing Mob with ID %s." %(Mob_byID)
            return
            
        NBT_MobsBody = self.NBT_Body[NBT_Pointer-Mobs_size:NBT_Pointer]
        # print "NBT_MobsBody\n"
        # print NBT_MobsBody #doesn't work for display

        query = "Are you sure you want to delete this MobID= %s ?[Y/N]" % (Mob_byID)
        userinput = raw_input(query)

        if userinput in self.yes :                              
            # DELETE the part of file according MobID
            # Select the string of the Mob accordeing its 'id' NBT Tag.
            NBT_MobsBody = self.NBT_Body[NBT_Pointer-Mobs_size:NBT_Pointer]
            # Delete the characters into the NBT_Body
            self.NBT_Body = string.replace(self.NBT_Body, NBT_MobsBody, '')
            # Display the message announcing that the task has been done.
            print "Don't forget to apply your change by using .saveNewFile()"
            # newEntitiesFile.close()
        elif userinput in self.no:
            return "Action aborted."
        else :
            return "Wrong command. Action aborted."   
        
        return  "MobID <%s> has been deleted." % (self.Mobs_ID)

    # del a mob by range of ID
    def delMobRangeByID(self, MobIDfrom, MobIDto):
        print "Sorry. Not implemented yet."
        pass    

    # del all mob from race
    def delMobsByRace(self, MobByRace):
        print "Sorry. Not implemented yet."
        pass
    """

    def FileSizeNBTdisplay(self):
        """
        Compare value of NBT data size :
        1st value read from NBT file.
        2nd value calculated from NBT data size.
        """
        sizeInNewEntitiesFile = self.FileSizeNBTread()
        sizeFileReal = self.FileSizeNBTcalc("Dec")
        return "Size ValueNBT: %s bytes <=> Real Estimated size of file: %s bytes. " % ( sizeInNewEntitiesFile, sizeFileReal)

    def FileSizeNBTcalc(self, NBTformat):
        # NBTformat can be "Dec" for decimal and "Hex" for hexa. 
        # Check of real file size - Don't forget to remove 12 bytes from Header !!
        # otherwise you might cry like I did...
        self.entitiesFile.seek(0, os.SEEK_END)

        if NBTformat == "Dec":
            sizeFileReal = int(self.entitiesFile.tell()) - 12 # 12 is the header of NBT
            return sizeFileReal
        elif NBTformat == "Hex":
            sizeFileReal = int(self.entitiesFile.tell()) - 12 # 12 is the header of NBT
            sizeFileReal = struct.pack('<L', sizeFileReal)
            # return ":".join("x{:02x}".format(ord(c)) for c in sizeFileReal) #for a repr 'xd6:x63:x00:x00'
            return sizeFileReal
        else:
            return "Sorry wrong NBTformat."

    def FileSizeNBTread(self):
        # Check file size NBT Value of file Data file size
        # entitiesFile = open('entities.dat','rb+')
        self.entitiesFile.seek(8)
        # WRONG = sizeInNewEntitiesFile = binascii.b2a_hex(newEntitiesFile.read(4))
        sizeInNewEntitiesFile = array.array('l', (self.entitiesFile.read(4)))
        sizeInNewEntitiesFile.byteswap()
        sizeInNewEntitiesFile = binascii.hexlify(sizeInNewEntitiesFile)
        sizeInNewEntitiesFile = int(sizeInNewEntitiesFile,16)
        return sizeInNewEntitiesFile
        

    def saveNewFile(self, filename='entities.dat'):
        '''
        To save modified data into a new file
        Input   : entities.dat
        :return: entities.dat (with new data)

        '''
        # check File Size
        newEntitiesFileData = self.NBT_Header + self.NBT_Body + self.NBT_Footer
        NewNBTLen = len(newEntitiesFileData) - 12 #delete header 12
        print "Lenght of  : %i " % (NewNBTLen)

        entities_fs_Dec = self.FileSizeNBTcalc("Dec")
        entities_fs_Hex = self.FileSizeNBTcalc("Hex")
        print "OLD NBT file data size %s (Hex : %s)" % (entities_fs_Dec, entities_fs_Hex.encode('hex'))
        print "NEW NBT file data size %s (Hex : %s)" % (entities_fs_Dec, entities_fs_Hex.encode('hex'))
              
        userinput = raw_input("Are you sure you want to save the file? [Y/N] ").lower()

        if userinput in self.yes:
            # Open the file
            newEntitiesFile = open(mcpi_world_path+'/'+filename, 'wb+')

            # Update and conversion of NewNBTLen var to Little Endian value
            NewNBTlen_LE = struct.pack('<Q', NewNBTLen)
            NewNBTlen_LE = NewNBTlen_LE[:4]
            # Update of file size by seeking size Var and Value
            newEntitiesFileData = newEntitiesFileData[:8] + NewNBTlen_LE + newEntitiesFileData[12:]
            # NEED to Update the value of Mobs as well
            newEntitiesFileData = newEntitiesFileData[:26] + self.NBTTAG_Number_Of_Mobs_Any + newEntitiesFileData[30:]
            # Writing into the file
            newEntitiesFile.write(newEntitiesFileData)

            print "New File has been created. \n <%s>" % (newEntitiesFile.name)
            newEntitiesFile.close()
        elif userinput in self.no:
            return "Action aborted."
        else:
            return "Wrong command. Action aborted." 

    def renameMe(self):
        # rename current entities.dat as entities.dat.date&time
        fromNow = str(datetime.datetime.now().strftime("%Y%m%d-%Hh%M"))
        backup_name = 'entities.dat.' + fromNow
        os.rename('entities.dat', backup_name)
        print "File <%s> saved." % (backup_name)
 

"""
Not implemented yet
    #### ADDITIONAL ###  

    # replace mob race by another race:
    def replaceMobs(self, MobTypefrom, MobTypeto):
        print "Sorry. Not implemented yet."
        pass    

    # change items into mobs
    def replaceMobs(self, MobTypefrom, MobTypeto):
        print "Sorry. Not implemented yet."
        pass 
"""

### Examples part ###
# From Raspberry Pi
# -----------------
# Be sure that Minecraft Pi game is turned Off.
# 1) Select your world from the menu
# example : from the menu, press 2 and enter.
#
# 2) give a name to your file first (e.g. myMCPI) by typing this command.
# myMCPI can be name you want.
# >>> myMCPI = mcpi_mobs_mgr()
#
# 3) Add mobs by typing
# >>> myMCPI.addMob("Pig", 10)
#  x, y, z coordinate not implemented yet. Sorry.
# If you go around POS: 26.1 / 14.5 / -25.6
# you will find the Mobs you added.
#
# 4.1) check how many mobs will be inside your world.
# >>> myMCPI.Mobs_howMany()
# >>> myMCPI.Mobs_show_stats()
# >>> myMCPI.Mobs_list_display()
# 4.2) and if you are really curious, look Binary representation of entities.dat file.
# >>> myMCPI.NBT_Header
# >>> myMCPI.NBT_Body
#
# 5) Save your change.
# >>> myMCPI.saveNewFile()
#
# 6) Start Minecraft Pi game and select your world.
#
# 7) you cannot kill Mobs with weapons. You need to use dynamite.
# some Mobs like Skeletons will die (because of the sun ?)
# There is a way to turn your Minecraft Pi world as survival mode.
# There is a way to patch with Binary Patch your Minecraft Pi and unlock Craft
# and your own inventory.
# I didn't find the way to be able to kill Mobs in the game with your weapon.
#
# Additional info : Comment this line for windows tests only
# >>> mcpi_world_path = 'C:\Users\username\myFile\Programming\Python\MCPI'
#


        

