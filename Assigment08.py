# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Barclay Bicksler,12-7-2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #


# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "products.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {product,price}
lstOfProductObjects = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strproduct = ""  # Captures the user product data
strprice = 0.0  # Captures the user price data
strStatus = ""  # Captures the status of an processing functions

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    pass

    # Constructor
    def __init__(self, product_name, product_price):
    # Attributes
        self.product_name = product_name
        self.product_price = product_price
# Data -------------------------------------------------------------------- #

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing products """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            product, price = line.split(",")
            row = {"product": product.strip(), "price": price.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(product, price, list_of_rows):
        row = {"product": product, "price": price}  # adding new user input values to the dicRow keys
        list_of_rows.append(row)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(product, list_of_rows):
        for row in list_of_rows:
            if row["product"].lower() == product.lower():
                lstOfProductObjects.remove(row)
        print("row removed")
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["product"] + "," + row["price"] + "\n")
        file.close()
        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output products """

    @staticmethod
    def print_menu_products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Product Data
        2) Add a product
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_products_in_list(list_of_rows):
        """ Shows the current products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products  are: *******")
        for row in list_of_rows:
            print(row["product"] + " (" + row["price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_product_and_price():
        product = input("Enter a product: ")
        price = input("Enter the price: ")
        return product, price

    @staticmethod
    def input_product_to_remove():
        product = input("Enter the product you wish to remove: ").lower().strip()
        print()
        return product

# Main Body of Script  ------------------------------------------------------ #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects1
    # let user save current data to file and exit program

# Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_products_in_list(lstOfProductObjects)  # Show current data in the list/table
    IO.print_menu_products()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Process user's menu choice
    if strChoice.strip() == '1':  # Show list of products
        IO.print_current_products_in_list(lstOfProductObjects)
        continue  # to show the menu

    elif strChoice == '2':  # Add a product
        strproduct, strprice = IO.input_new_product_and_price()
        lstOfProductObjects, strStatus = Processor.add_data_to_list(strproduct, strprice, lstOfProductObjects)
        IO.input_press_to_continue(strStatus)

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            lstOfProductObjects, strStatus = Processor.write_data_to_file(strFileName, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  #  Exit Program
        print("Goodbye!")
        break   # and Exit
