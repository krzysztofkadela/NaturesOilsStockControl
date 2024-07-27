# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

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
    #print("1 - Goods in Update/n")
    #print("2 - Goods out Update/n")
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




def check_correct_input(choice, menu):
    """
    Checking correct input fromuser for menu functions.
    """
    int[(choice)]
    if(menu == update_stock_menu):
        try:
            if(menu <=0 and menu >5):
                raise ValueError(
                    print("Nie ma takiej opcji!!") 
                )
        except ValueError as e:
            print("uppsss")

def upddate_stock(choice, product_list):
    """
    Updating stock, all option goods in goods out and corrections. 
    """
    if choice == "goods_out":
        data = ()
        for product in product_list:
            while True:
                  # asking user for correct input
                  print("Please enter a numeric value for all products quantity.")
                  value = input(f"How many of {num[0]} you wants to add to the stock?: ")
                  try:
                     # Attempt to convert the input to a float to handle numbers with decimals
                     numeric_value = float(value)
                     # If the conversion is successful, break the loop
                     results += (product, numeric_value)
                     break
                  except ValueError:
                     # If conversion fails, print an error message
                     print("Wrong value. Please enter a valid number.")
    return results

        

    
    

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
                print("You chose Choice 1.")
             elif choice_I == '2':
                 print("You chose Choice 2.")
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
        
        


main()

 