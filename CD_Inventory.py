#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes and objects in a program that asks for user input to create a CD inventory
# Change Log: (Who, When, What)
# MPoehler, 2021-Mar-05, Retrieved file created by DBiesinger
# MPoehler, 2021-Mar-06, Added code to CD class, IO class and Main Body
# Mpoehler, 2021-Mar-07, Added code to FileIO class, added some error handling and cleaned up all TODOs
#------------------------------------------#

# -- DATA -- #
strFileName = 'CDInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # -- Fields -- #
    # -- Constructor -- #
    def __init__(self, ID, Title, Artist):
    #   -- Atrributes  -- #
        self.__id = ID
        self.__title = Title
        self.__artist = Artist
    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__id

    @cd_id.setter
    def cd_id(self, value):
        if type(value) == int:
            self.__id = value
        else:
            raise Exception('ID needs to be a numeral')

    @property
    def cd_title(self):
        return self.__title

    @cd_title.setter
    def cd_title(self, value):
        if type(value) == str:
            self.__title = value
        else:
            raise Exception('Title needs to be a string')

    @property
    def cd_artist(self):
        return self.__artist

    @cd_artist.setter
    def cd_artist(self, value):
        if type(value) == str:
            self.__artist
        else:
            raise Exception('Artist needs to be a string')

    # -- Methods -- #

    # Setting the desired format for how the CD attributes should be displayed
    def __str__(self):
        return '{:<6}{:20} {:20}'.format(self.cd_id, self.cd_title, self.cd_artist)

    # Setting the CD attributes in the appropriate format for saving to a file
    def save_CD_data(self):
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

        properties:

        methods:
            save_inventory(file_name, lst_Inventory): -> None
            load_inventory(file_name): -> (a list of CD objects)

        """
    # -- Fields -- #
    # -- Constructor -- #
    #   -- Attributes  -- #
    # -- Properties -- #
    # -- Methods -- #

    # Saving list of CD attributes to a file using preset format
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        with open(file_name, 'w') as objFile:
            for obj in lst_Inventory:
                objFile.write(obj.save_CD_data())
        objFile.close()
        return

    # Loading CD attributes from text file and updating the current inventory
    @staticmethod
    def load_inventory(file_name, lst_Inventory):
        lst_Inventory.clear()
        with open(file_name, 'r') as objFile:
            for line in objFile:
                data = line.strip().split(',')
                fileObjs = [int(data[0]), data[1], data[2]]
                CDObject = CD(fileObjs[0], fileObjs[1], fileObjs[2])
                lst_Inventory.append(CDObject)
        objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
    """ Handling Input and Output:

        properties:

        methods:
            choice: user selection from program menu -> user's choice to be used to select parts of program
            menu: the display of the menu -> prints out menu for user
            inventory(lstOfCDObjects): displaying of the inventory -> prints out inventory
            get_data: collecting user data for the CD object, adding more CD information to inventory -> user data to be used in CD object

        """
    # -- Fields -- #
    # -- Constructor -- #
    #   -- Attributes  -- #
    # -- Properties -- #
    # -- Methods -- #

    @staticmethod
    def choice():
        choice = ''
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def menu():
        print('\nMenu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory\n[s] Save Inventory to file\n[x] Exit\n')

    @staticmethod
    def inventory(invLst):
        print('\n======= The Current Inventory: ============')
        print('{:<6}{:20} {:20}'.format('ID', 'Title', 'Artist'))
        for obj in invLst:
            print(obj.__str__())
        print('===========================================')

    @staticmethod
    def get_data():
        strID = input('Enter ID: ').strip()
        intID = int(strID)
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return [intID, strTitle, strArtist]

# -- Main Body of Script -- #

# Load data from file into a list of CD objects on script start
try:
    FileIO.load_inventory(strFileName, lstOfCDObjects)
except FileNotFoundError:
    print('\nFile:', strFileName, ', Does not exist. Please save Inventory data to create file.')
except EOFError:
    print('\nFile is empty. Please save CD Inventory data.')
except Exception:
    print("Non specific loading error")

print('\nWelcome to the CD Inventory Program!')

while True:

    # Display menu to user
    IO.menu()
    user_choice = IO.choice()

    # show user current inventory
    if user_choice == 'i':
        IO.inventory(lstOfCDObjects)
        continue

    # let user add data to the inventory
    elif user_choice == 'a':
        IO.inventory(lstOfCDObjects)
        user_input = input('Would you like to:\n[n] Start from Scratch and create new inventory items\nOR\n[b] Build on the inventory already established\n Your choice [n or b]: ')
        if user_input == 'n':
            lstOfCDObjects.clear()
            try:
                user_data = IO.get_data()
            except ValueError:
                print('\nEntry Error!')
                print('If you would like to add an entry please enter an integer(number) for an ID.')
            CDObject = CD(user_data[0], user_data[1], user_data[2])
            lstOfCDObjects.append(CDObject)
            continue
        elif user_input == 'b':
            try:
                user_data = IO.get_data()
            except ValueError:
                print('\nEntry Error!')
                print('If you would like to add an entry please enter an integer(number) for an ID.')
            CDObject = CD(user_data[0], user_data[1], user_data[2])
            lstOfCDObjects.append(CDObject)
            continue
        else:
            input('Nothing was added to the inventory. Press [ENTER] to return to the main menu.')
            continue

    # let user save inventory to file
    elif user_choice == 's':
        IO.inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
            print('\nInventory file has been updated\n')
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue

    # let user load inventory from file
    elif user_choice == 'l':
        # loads invetory from file. Used code from previous Assignment, Assignment07 from DBiesinger's programming course.
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory will contain information re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('\nreloading...\n')
            try:
                FileIO.load_inventory(strFileName, lstOfCDObjects)
            except FileNotFoundError:
                print('\nFile:', strFileName, ', Does not exist. Please save Inventory data to create file.')
            except EOFError:
                print('\nFile is empty. Please save CD Inventory data.')
            except Exception:
                print("Non specific loading error")
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.\n')
        IO.inventory(lstOfCDObjects)
        continue

    # let user exit program
    elif user_choice == 'x':
        break

    # Error catch-all brought over from previous assignement script
    else:
        print('General Error')

