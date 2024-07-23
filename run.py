# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

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

data = products.get_all_values()

print(data)

def main_menu():
    """
    displays main menu for user
    """
    print("Welcome in Natures Oils Stok System")
    print("Please select one of the options:/n")
    print("1 - Goods in Update/n")
    print("2 - Goods out Update/n")
    print("3 - Updated product list")
    print("4 - Finsh")
    user_choice = input("Whats you want to do? \n")
    print(user_choice)



def main():
    """
    Main function run the program
    """
    main_menu()


main()

 