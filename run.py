# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from datetime import datetime
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('NO_Stock')

products = SHEET.worksheet('Product List')

#Geting all values in the worksheet as DataFrame
data = products.get_all_records()
df = pd.DataFrame(data)
# Creating a list of products from the "Product Name" column.
product_list = df['Product Name'].to_list()
# list printed to the terminal.
print(product_list)

sizes_data = SHEET.worksheet('Product size')

#Geting all values in the worksheet as DataFrame
data_size = sizes_data.get_all_records()
df = pd.DataFrame(data_size)
# Creating a list of products sizes from the "Product Size" column.
product_size_list = df['Product Size'].to_list()
# list printed to the terminal.
print(product_size_list)


def get_valid_choice(menu_option):
    """
    Prompts the user to enter a choice between 1 and 5.
    Returns the valid choice if input is valid, otherwise None.
    """
    while True:  # Loop until valid input is received
        user_input = input("Please enter an integer between 1 and 5: \n")

        try:
            user_input = int(user_input)  # Try to convert the input to an integer
            if 1 <= user_input <= menu_option:  # Check if the value is between 1 and 5
                return user_input  # Return the valid input
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")



def main_menu():
    """
    Displays "Main Menu" for user, ask to make a choice, check the choice and if is valid,
    returns value.
    """
    #Printing options for user.
    print("Welcome in Natures Oils Stock System")
    print("Please select one of the options:")
    print("1 - Update stock")
    print("2 - Updated product list")
    print("3 - Production Report's")
    print("4 - Finsh")
    user_choice_main_menu = input("Whats you want to do? \n") 
    return user_choice_main_menu

def update_stock_menu():
    """
    Displeys "Update stock Menu" for all goods in and orders out.
    """
    print("U are to try update stock")
    print("You have choice 'Update stock' option:")
    print("What you wants to update?:")
    print("1 - Goods In.")
    print("2 - Goods Out.")
    print("3 - Stock Correction.")
    print("4 - Stock Take")
    print("5 - Return to main menu.")
    #function to check valid user choice, asigning value to varible user_choice_stock_menu
    user_choice_stock_menu = get_valid_choice(5)
    #return valid user choice
    return user_choice_stock_menu


def upddate_stock(choice, product_list):
    """
    Updating stock, all option goods in goods out and corrections. 
    """
    #Getting current date.
    current_date = datetime.now()

    #Converted to format "YYYY-MM-DD".
    converted_date = current_date.strftime("%Y-%m-%d")

    if choice == "goods_in":#For Goods In option 
        
        data_in = []
        # Asking user for correct input
        print("Please enter a numeric value for all products quantity.")

        for product in product_list:#Getting values from product_list varible , products imported from worksheet.
            
            while True:
                  # Getting values for each product from user.
                  value = input(f"How many of {product} you wants to add to the stock?: \n")
                  try:
                     # Attempt to convert the input to a intager.
                     numeric_value = int(value)
                     # If the conversion is successful, break the loop
                     data_in.append((converted_date, product, numeric_value))
                     break
                  except ValueError:
                     # If conversion fails, print an error message
                     print("Wrong value. Please enter a valid number.")

        #return tuple(data_in) #convert list to tuple before return.
        return data_in
    elif choice == "goods_out":
        data_out = []
        # asking user for correct input
        print("Please enter a numeric value for all products quantity.")

        for product in product_list:
            
            while True:
                  # asking user for correct input
                  value = input(f"How many of {product} was send out to customers?: \n")
                  try:
                     # Attempt to convert the input to a intager.
                     numeric_value = int(value)
                     # If the conversion is successful, break the loop
                     data_out.append((converted_date, product, numeric_value))
                     break
                  except ValueError:
                     # If conversion fails, print an error message
                     print("Wrong value. Please enter a valid number.")
        #return tuple(data_out)
        return data_out


def update_worksheet(data, worksheet):
    """
    By geting data and worksheet updates appropriate spreadsheet.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    for record in data:
        # Ensure the record is a flat list with string representation for writing
        record_as_list = [str(value) if not isinstance(value, (int, float)) else value for value in record]
        
        # Print for debugging purposes
        print(f"Appending record: {record_as_list}\n")  # Check the data format(added \n Statment!!!!!!!!!!!)

        try:
            worksheet_to_update.append_row(record_as_list)
            print(f"Successfully appended record: {record_as_list}")  # Confirmation of success
        except Exception as e:
            print(f"Failed to append record {record_as_list} due to error: {e}")
    #for record in data:
          #worksheet_to_update.append_row(data)
    #print(f"{worksheet} worksheet updated successfully\n")
    
def add_new_product():
    """
    Asking user for updates product list, user can add new products, all information are 
    store in the dictionary and return from function.
    """
    #Add time.sleep() to delay displaying rules.
    print("      Welcome to the new product addition section.")
    time.sleep(3)
    print("--------------------------------------------------------------")
    print("Please provide information according to the requirements below")
    time.sleep(3)
    print("--------------------------------------------------------------")
    print("  Product Name maximum 20 characters, only contain letters allow to use space to separate worlds")
    time.sleep(3)
    print("--------------------------------------------------------------")
    print("       Product size only from size options provided!")
    time.sleep(3)
    print("--------------------------------------------------------------")
    print("           Barode 13 digits and only digits.")

    # Collecting current date and formating to neede format YYYY-MM-DD.
    current_date_load = datetime.now()
    current_date_new_product = current_date_load.strftime("%Y-%m-%d")

    # New Product fill by user.
    new_product_name = input("Please enter a new product name: \n")

    # Validatting  product name inserted by user.
    while len(new_product_name) > 20 or not all(char.isalpha() or char.isspace() for char in new_product_name) : #Max 20 characters and only letters and spaces.
        print("Error: Product name must be at most 20 characters long and contain only letters.")
        new_product_name = input("Please enter a new product name: \n")

    # New Product size from user:
    valid_sizes = ['220ml', '450ml', '860ml', '4.5L', '10L']  #list of evelible products sizes.
    
    print(f"Available sizes:{valid_sizes} ")
    new_product_size = input("Please enter new product size: \n")

    # Validate product size
    while new_product_size not in valid_sizes:
        print("Error: Please enter a valid product size.")
        new_product_size = input("Please enter new product size (options: 220ml, 450ml, 860ml, 4.5L, 10L): \n")

    # while loop to check are barcode enetered hev 13 digits.
    while True:

        barcode = input("Please enter a 13-digit barcode: \n")

        # checking is barcode enetred valid.
        if len(barcode) == 13 and barcode.isdigit():
            break
        else:
            print("Invalid barcode, please enter 13-digit barcode")

    # Creating dictonary with collected data

    new_product_info = {
        "current_date": current_date_new_product,
        "product_name": new_product_name,
        "product_size": new_product_size,
        "barcode": barcode
    }

    return new_product_info      

def update_worksheet_new_product(new_product,worksheet):
    """
    Taking paramiter with new product info and updating 'Product list' worksheet.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)

    # Creating list of data to be added to worksheet

    row = [new_product["current_date"], new_product["product_name"], new_product["product_size"], new_product["barcode"]]

    worksheet_to_update.append_row(row)

    print("Product list have be updated!")



def main():
    """
    Main function run the program
    """
    while True:
      choice = main_menu()
      if choice == '1':
         print("You chose Choice 1.")
         while True:
             choice_I = update_stock_menu()
             if choice_I == '1':
                #choice 1 updtate product goods in
                data_in = upddate_stock("goods_in", product_list)
                print(data_in)
                update_worksheet(data_in, "Product Good In")
             elif choice_I == '2':
                #choice 2 update product goods out
                data_out = upddate_stock("goods_out", product_list)
                update_worksheet(data_out, "Product Good Out")
                #print(f"You data is: {data_out}")
             elif choice_I == '3':
                 print("You chose Choice 3.")
             elif choice_I == '4':
                 print("You chose Choice 3.")
             elif choice_I == '5':
                   print("Exiting the menu. Goodbye!")
                   break  # Exit the loop
             else:
                 print("Invalid choice. Please select a number between 1 and 4.")
                 print("Please select on number from 1 to 4 and pres enter! ")
      elif choice == '2':
         print("You chose Choice 2.")
      elif choice == '3':
         print("You chose Choice 3.")
      elif choice == '4':
        print("Exiting the menu. Goodbye!")
        break  # Exit the loop
      else:
         print("Invalid choice. Please select a number between 1 and 4.\n")
         print("Please select one number from 1 to 4 and pres enter! ")


    
#main()
#new = add_new_product()
#print(new)
#update_worksheet_new_product(new,"Product List")

#user_input_test = get_valid_choice(5)

#print(user_input_test)