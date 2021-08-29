#---------------------------------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# KHauser, 2021-Aug-29, Modified Assignment07 to read .txt
# KHauser, 2021-Aug-29, Mdoified to replace list of dicts w/ objects
#---------------------------------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstOfCDObjects = []
strFileName = 'CDInventory.txt'  # data storage file

class CD:
    """Stores data about a CD:
    
    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
        
    methods:
        none.

    """
    def __init__(self, cd_id, cd_title, cd_artist):
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, new_cd_id):
        self.__cd_id = new_cd_id
    
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, new_cd_title):
        self.__cd_title = new_cd_title
            
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, new_cd_artist):
        self.__cd_artist = new_cd_artist

class DataProcessor:
    """Processing the data in the application:
    
    properties:
        none
                
    methods:
        add_inventory(strID, strTitle, strArtist, lstInventory): -> None

    """

    @staticmethod
    def add_inventory(strID, strTitle, strArtist, lstInventory):
        """Function to add a new entry to the inventory

        Args:
            strID (string): ID for the new CD added to the inventory
            strTitle (string):Title for the new CD added to the inventory
            strArtist (string):Artist for the new CD added to the inventory
            lst_Inventory (list of CD objects): 2D data structure (list of dicts) that holds the data during runtime
        
        Returns:
            None.
        """
        try:
            intID = int(strID)
            newCD = CD(intID, strTitle, strArtist)
            lstInventory.append(newCD)
        except ValueError:
            print('Oops! ID must be an integer. Please try again')

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:
        none
        
    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
       
    @staticmethod
    def load_inventory(file_name, lstInventory):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D list
        (list of objects) list one line in the file represents one object in the list.

        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list of objects): 2D data structure (list of objects) that holds the data during runtime

        Returns:
            none
        """
        try:
            with open(file_name, 'r') as fileObject:
                lstInventory.clear()
                for line in fileObject:
                    data = line.strip().split(',')
                    newCD = CD(int(data[0]), data[1], data[2])
                    lstInventory.append(newCD)
        except FileNotFoundError:
            print('Oops! No such file or directory: ', file_name)
    
    @staticmethod
    def save_inventory(file_name, lstInventory):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D list
        (list of dicts) list one line in the file represents one dictionary row in list.

        Args:
            file_name (string): name of file used to write the data from
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            error_type (string): returns the class name of the error that was thrown 
        """
        try:
            with open(file_name, 'w') as fileObject:
                for cd in lstInventory:
                    fileObject.write("{},{},{}\n".format(cd.cd_id, cd.cd_title, cd.cd_artist))
        except FileNotFoundError:
            print('Oops! No such file or directory: ', file_name)

# -- PRESENTATION (Input/Output) -- #
class IO:
    """displays data and prompts about the CD inventory program:
    
    properties:
        none
        
    methods:
        print_menu(): -> None
        menu_choice(): -> choice
        show_inventory(table): -> None
        get_cd_info(): -> ID, title, artist
    """
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        
        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
        
    @staticmethod
    def menu_choice():
        """Function to get user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def show_inventory(lstInventory):
        """Displays current inventory table

        Args:
            lstInventory (list of objects): 2D data structure (list of objects) that holds the data during runtime.

        Returns:
            None.

        """
        print('\n======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        try:
            for cd in lstInventory:
                print('{}\t{} (by: {})'.format(cd.cd_id, cd.cd_title, cd.cd_artist))
        except:
            print('\nNo CDs currently stored')
        print('======================================\n')

    @staticmethod
    def get_cd_info():
        """Get User Input for CD ID, Album, Artist

        Args:
            None.
            
        Returns:
            ID (int): CD ID from user input
            title (string): the CD title from user input
            artist (string): the CD artist name from user input
        """
        while True:
            try:
                ID = int(input('Enter ID: ').strip())
                break
            except ValueError:
                print('Oops! ID must be an integer. Please try again')
        title = input('What is the CD\'s title? ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        return ID, title, artist


# -- Main Body of Script -- #
FileIO.load_inventory(strFileName, lstOfCDObjects)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    
    
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        intID, strTitle, strArtist = IO.get_cd_info()
        # 3.3.2 Add item to the table
        DataProcessor.add_inventory(intID, strTitle, strArtist, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
        
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
        
    # 3.5 process save inventory to file
    elif strChoice == 's':
        # 3.5.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.5.2 Process choice
        if strYesNo == 'y':
            # 3.5.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
        
        
    # 3.6 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')