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

# don't change the space into this dic for Zombie Pigman entry. I later sanitize input with .title()
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
    global NBTTAG_Number_Of_Mobs_Empty, NBTTAG_Number_Of_Mobs_One, NBTTAG_Number_Of_Mobs_Any
    NBTTAG_Number_Of_Mobs_Empty = "\x00\x01\x00\x00"
    NBTTAG_Number_Of_Mobs_One = "\n\x01\x00\x00"
    NBTTAG_Number_Of_Mobs_Any = "\n\xee\x00\x00"

    def __init__(self, filename ='entities.dat'):
        self.filename = filename
        # For Data
        self.entitiesFile = open(mcpi_world_path+'/'+ self.filename, 'rb+')
        self.entitiesFileData = self.entitiesFile.read()

        # for menu confirmation
        self.yes = ['yes', 'y', 'ye', '']
        self.no = ['no', 'n']
        self.Mobs_ID = Mobs_ID

        # All the NBT date from file
        self.NBT_ALL = self.entitiesFileData[:]
        
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


    def NBT_All(self):
        """
        :return:
         the NBT info
        """
        self.NBT_ALL = self.NBT_Header + self.NBT_Body + self.NBT_Footer
        return (self.NBT_ALL)

    

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
        # Call the global variable
        global NBTTAG_Number_Of_Mobs_Empty, NBTTAG_Number_Of_Mobs_One, NBTTAG_Number_Of_Mobs_Any
        
        # Mobs_Separator
        NBTTAG_Mobs_Passive_Separator = "\x00\x03\x03\x00"
        # Another Mobs_Separator
        NBTTAG_Mobs_Separator_Last = "\x00\x02\x03\x00"

        # NUMBER OF MOBS HERE \x01 for 1x Mobs, \x02 for 2x, etc...
        # Number_Of_Mobs = "\n\xee\x00\x00" is your friend !
        #self.NBTTAG_Number_Of_Mobs_Empty = "\x00\x01\x00\x00"
        #self.NBTTAG_Number_Of_Mobs_One = "\n\x01\x00\x00"
        #self.NBTTAG_Number_Of_Mobs_Any = "\n\xee\x00\x00"

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
        # >>> Pos\x05\x03\x00\x00\x00^W\x1bC\x00\x00\x86B\xd7\x07\xccB\t\x08\x00
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
        # id\0d\x00\x00\x00 but representation of b'\x0d' will turn to \r
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
        # id\x22\x00\x00\x00 but representation of b'\x22' will turn to '"'
        # to avoid the mess, use for this portion ' ' for that value
        mobs_Template_Skele = "Age\x00\x00\x00\x00\x02\x03\x00" +\
                              "Air,\x01\x02\n\x00" +\
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
                              'id"\x00\x00\x00'

  

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
            print "Don't forget to save with myMCPI.saveNewFile()."
            print "Be careful: all or some of data previously"
            print "into your entities.dat file might be deleted."

        return 

  

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
        

    def saveNewFile(self, filename='entities.dat', ):
        '''
        To save modified data into a new file
        Input   : entities.dat
        :return: entities.dat (with new data)

        '''
        global NBTTAG_Number_Of_Mobs_Empty, NBTTAG_Number_Of_Mobs_One, NBTTAG_Number_Of_Mobs_Any
        
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
            # But first... test if you don't update only the Header ^^;
            if self.NBT_Body == NBTTAG_Number_Of_Mobs_Empty:
                NBTTAG_Number_Of_Mobs_Any = NBTTAG_Number_Of_Mobs_Empty
            newEntitiesFileData = newEntitiesFileData[:26] + NBTTAG_Number_Of_Mobs_Any + newEntitiesFileData[30:]
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
        return ("File <%s> saved." % (backup_name))
        

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

# To start changing your game mode from Creative into Survival
# myLevel = mcpi_Mode_mgr()


class mcpi_Mode_mgr(object):
    global Mode_ID, NBTTAG_Mode_Creative, NBTTAG_Mode_Survival, GameTypeStr

    # GameType is just after
    Mode_ID     = b'\x47\x61\x6D\x65\x54\x79\x70\x65'
    # GameType is just after
    GameTypeStr = b'\x47\x61\x6D\x65\x54\x79\x70\x65' 

    NBTTAG_Mode_Creative = b'\x01'
    # "\x01\x00\x00\x00" 
    NBTTAG_Mode_Survival = b'\x00'
    # "\x00\x00\x00\x00"
    #NBTTAG_Number_Of_Mobs_Any = "\n\xee\x00\x00"
    
    def __init__(self, levelfilename ='level.dat'):
        self.levelfilename = levelfilename
        # For Data
        self.levelFile = open(mcpi_world_path+'/'+ self.levelfilename, 'rb+')
        self.levelFileData = self.levelFile.read()
    
        # for menu confirmation
        self.yes = ['yes', 'y', 'ye', '']
        self.no = ['no', 'n']
        self.Mode_ID = Mode_ID
    
        # Header of the NBT file level 
        self.NBT_levelHeader = self.levelFileData[:23]
        # Be careful : if you have items, you will have to adjust
        # The footer manually
        self.NBT_levelFooter = self.levelFileData[-22:]
        self.NBT_levelBody = self.levelFileData[23:-22]
    
    def __str__(self):
        """
        return message about type
        """
        return "This is LEVEL.dat file. Really..."


    def NBT_PrintAll(self):
        """
        :return:
         the NBT Level info
        """
        NBT_LEVEL_ALL = self.NBT_levelHeader + self.NBT_levelBody + self.NBT_levelFooter
        return ":".join("{:02x}".format(ord(c)) for c in NBT_LEVEL_ALL)


    def findHexaString(self, HexaString=GameTypeStr):
        """
        Input: provide Hexa string that you are looking for.
            ex: 
        output: provide the ID into the file of the first binary value found
              AFTER the HexaString you were searching.
        
        """
        # Lenght of Binary String
        lbs = len(HexaString)
        hexChrIndex = 0
        
        for i in self.levelFileData:
            if i == str(HexaString[:1]):
                if self.levelFileData[hexChrIndex:hexChrIndex+lbs] == HexaString:
                    binIDbegin = hexChrIndex+lbs+1
                    return binIDbegin
            hexChrIndex += 1
        return ("Bad News ! Couldn't find the string into the Binary data of the file.")
        ### end of function
        # yep extra !! : myLevel.levelFileData[23-len(HexaString)11:23]


    def changeHexString(self, ID, HexaString, HexaStringLenght ):
        # go to the ID place.

        # If HexaString == HexaStringLenght
        # print("Your Hexa String and lenght are same. For your reference, you are in replacement mode.")

        # If HexaString < HexaStringLenght
        # print("Your Hexa String is shorter than your lenght. For your reference, you are in removal mode.")

        # If HexaString > HexaStringLenght
        # print("Your Hexa String is longer than your lenght. For your reference, you are inserting more code insertion mode.")
        
        #Change the string
        pass


    def checkGameMode(self):
        """
        Input : as class, it is Level.dat data file (included)
        Output : will return if the world is in Creative or Survival mode.
        """
        global GameTypeStr
        
        GameModeValue_ID = self.findHexaString(GameTypeStr)
        GameModeValue = self.levelFileData[GameModeValue_ID-1]

        print("Game mode is by default Creative. In survival mode," +\
              " you will be able to see day and night time." +\
              " Mobs like Skeletons will also leave longer.")        
        if GameModeValue == b'\x01' :
            print("The game is in Creative mode :" + GameModeValue)
        elif GameModeValue == b'\x00' :
            print("The game is in Survival mode :" + GameModeValue)
        else:
            print("The game is in undetermined mode :" + GameModeValue)
        return GameModeValue

    # myLevel = mcpi_Mode_mgr()
    # myLevel.checkMode()


    def changeGameMode(self):
        """
        add Mob(s) into your Minecraft Pi world.
        """
        # NBT_levelHeader

        #check mode:
        resultCheckGameMode = self.checkGameMode()
        dictGameMode = [{b'\x00' : "Survival"}, {b'\x01' :"Creative"}]
        for curDict in dictGameMode:
            if curDict.has_key(resultCheckGameMode):
                print("Currently your world is in " + curDict[resultCheckGameMode] + " mode.")
                
                userinput = input("Would you like to change the mode to " + "--TO CHANGE THAT MEC----")
        print("Currently your world is in undetermined mode.")
        userinput = input("Would you like to change the mode in 0-Survival or 1-Creative [0/1] ?")
        if userinput == 0:
            pass
        elif userinput == 1:
            pass
        else:
            return("can't understand. Aborted.")
                
        #GameModeValue_ID = findHexaString(GameTypeStr)
        #GameModeValue = int(self.levelFileData[GameModeValue_ID])
        pass        


    def changeGameMode2(self, CurrentGameMode):
        """
        Suggest to change the game mode to the other.
        """
        # NBT_levelHeader
        #Choose Opposite Game mode:
        dictGameMode = [{b'\x00' : "Survival"}, {b'\x01' :"Creative"}]
        currentId = 0
        swapId = 0
        
        while True:
            if dictGameMode[currentId].has_key(CurrentGameMode):
                swapID = currentId - 1
                userinput = input("Would you like to change the mode <"+ str(dictGameMode[currentId]) +"> to <" + str(dictGameMode[swapId]) +"> [1=Yes]/[0=No]?")
                if userinput == 1:
                    # change to swapId
                    print("Change to " + str(dictGameMode[swapId]) + " under progress...")
                    return("Change done: Enjoy!")
                elif userinput == 0:
                    return("Change cancelled.")
                else:
                    return("can't understand. Aborted.")
            currentId += 1
            if currentId > 2:
                print("Currently your world is in undetermined mode.")
                userinput = input("Would you like to change the mode in 0-Survival or 1-Creative [0/1] ?")
                # NewGameMode

        #GameModeValue_ID = findHexaString(GameTypeStr)
        #GameModeValue = int(self.levelFileData[GameModeValue_ID])
        return("newGameMode done.")

   


    def saveNewFile(self, filename='level.dat', ):
        """
        To save modified data into a new file
        Input   : level.dat
        :return: level.dat (with new data)

        """
        global Mode_ID, NBTTAG_Mode_Creative, NBTTAG_Mode_Survival
        Mode_ID = b'\x47\x61\x6D\x65\x54\x79\x70\x65' # GameType text is just after
        # NBTTAG_Mode_Creative = b'\x01' # "\x01\x00\x00\x00"
        # NBTTAG_Mode_Survival = b'\x00'  # "\x00\x00\x00\x00"
        
        # check File Size
        newEntitiesFileData = self.NBT_levelHeader + self.NBT_levelBody + self.NBT_levelFooter
        NewNBTLen = len(newEntitiesFileData) - 12 #delete header 12
        print "Lenght of  : %i " % (NewNBTLen)

        #entities_fs_Dec = self.FileSizeNBTcalc("Dec")
        #entities_fs_Hex = self.FileSizeNBTcalc("Hex")
        #print "OLD NBT file data size %s (Hex : %s)" % (entities_fs_Dec, entities_fs_Hex.encode('hex'))
        #print "NEW NBT file data size %s (Hex : %s)" % (entities_fs_Dec, entities_fs_Hex.encode('hex'))
              
        userinput = raw_input("Are you sure you want to change the world to Survival mode? [Y/N] ").lower()

        if userinput in self.yes:
            # Open the file
            newLevelFile = open(mcpi_world_path+'/'+filename, 'wb+')

            # Update and conversion of NewNBTLen var to Little Endian value
            NewNBTlen_LE = struct.pack('<Q', NewNBTLen)
            NewNBTlen_LE = NewNBTlen_LE[:4]
            # Update of file size by seeking size Var and Value
            newLevelFileData = newLevelFileData[:8] + NewNBTlen_LE + newLevelFileData[12:]

            # NEED to Update the value of Mobs as well
            # newEntitiesFileData = newEntitiesFileData[:26] + NBTTAG_Number_Of_Mobs_Any + newEntitiesFileData[30:]
            # to be continue .... newLevelFileData =
            
            # Writing into the file
            newLevelFile.write(newLevelFileData)

            print "New File has been created. \n <%s>" % (newLevelFile.name)
            newLevelFile.close()
        elif userinput in self.no:
            return "Action aborted."
        else:
            return "Wrong command. Action aborted."     



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




def willTest():
    myMCPI = mcpi_mobs_mgr()
    myMCPI.Mobs_howMany()
    myMCPI.addMob("Skeleton", 30)
    myMCPI.saveNewFile()
    print("Spawn, Update & Save => done")
    



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


        

