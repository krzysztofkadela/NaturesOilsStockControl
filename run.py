# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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

#data_1 = products.get_all_values()

#print(data_1)

def main_menu():
    """
    displays main menu for user
    """
    print("Welcome in Natures Oils Stock System")
    print("Please select one of the options:")
    print("1 - Update stock")
    print("2 - Updated product list")
    print("3 - Production Report's")
    print("4 - Finsh")
    user_choice = input("Whats you want to do \n?")
    return user_choice

def update_stock_menu():
    """
    Update stock for all goods in and orders out.
    """
    print("U are to try update stock")
    print("You have choice 'Update stock' option:")
    print("What you wants to update?:")
    print("1 - Goods Out.")
    print("2 - Goods In.")
    print("3 - Stock correction.")
    print("4 - Stock Take")
    print("5 - Return to main menu.")
    user_choice = input("Whats you want to do?\n")
    return user_choice




def check_correct_input(choice):
    """
    Checking correct input from user for menu functions.
    """
    if choice < 1 or choice > 5:
        print("Parameter must be between 1 and 5.")
        return False

    user_input = input(f"Please enter an integer between 1 and {choice}: ")

    try:
        user_input = int(user_input)
        if 1 <= user_input <= choice:
            print("Valid input!")
            return True
        else:
            print("Invalid input. Please enter a number within the specified range.")
            return False
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return False        
    

def upddate_stock(choice, product_list):
    """
    Updating stock, all option goods in goods out and corrections. 
    """
    #getting current date.
    current_date = datetime.now()
    #converted to format "YYYY-MM-DD".
    converted_date = current_date.strftime("%Y-%m-%d")

    if choice == "goods_in":
        
        data_in = []
        # asking user for correct input
        print("Please enter a numeric value for all products quantity.")

        for product in product_list:
            
            while True:
                  # asking user for correct input
                  value = input(f"How many of {product} you wants to add to the stock?: ")
                  try:
                     # Attempt to convert the input to a intager.
                     numeric_value = int(value)
                     # If the conversion is successful, break the loop
                     data_in.append((converted_date, product, numeric_value))
                     break
                  except ValueError:
                     # If conversion fails, print an error message
                     print("Wrong value. Please enter a valid number.")

        return tuple(data_in) #convert list to tuple before return.
    elif choice == "goods_out":
        data_out = []
        # asking user for correct input
        print("Please enter a numeric value for all products quantity.")

        for product in product_list:
            
            while True:
                  # asking user for correct input
                  value = input(f"How many of {product} was send out to customers?: ")
                  try:
                     # Attempt to convert the input to a intager.
                     numeric_value = int(value)
                     # If the conversion is successful, break the loop
                     data_out.append((converted_date, product, numeric_value))
                     break
                  except ValueError:
                     # If conversion fails, print an error message
                     print("Wrong value. Please enter a valid number.")
        return tuple(data_out)


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
        print(f"Appending record: {record_as_list}")  # Check the data format

        try:
            worksheet_to_update.append_row(record_as_list)
            print(f"Successfully appended record: {record_as_list}")  # Confirmation of success
        except Exception as e:
            print(f"Failed to append record {record_as_list} due to error: {e}")
    #for record in data:
          #worksheet_to_update.append_row(data)
    #print(f"{worksheet} worksheet updated successfully\n")
    
    

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
                update_worksheet(data_in, "Product Goods In")
             elif choice_I == '2':
                #choice 2 update product goods out
                data_out = upddate_stock("goods_out", product_list)
                print(f"You data is: {data_out}")
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


def update_test(data, worksheet):
    """
    By geting data and worksheet updates appropriate spreadsheet.
    """
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")
   
data_to = ['2024-07-01', 'Dummy Product', 10]


#worksheet = SHEET.worksheet("Product Good In")

#worksheet.append_row(['2024-07-01', 'Dummy Product', 10])

update_test(data_to, "Product Good In")
#resuly_tuple_in = upddate_stock("goods_in", product_list)
#update_worksheet(data_to_insert, "Product Goods In")


#resuly_tuple_out = upddate_stock("goods_out", product_list)

