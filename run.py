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

"""
Geting all values in the worksheet as DataFrame
"""

products = SHEET.worksheet('Product List')  # product list.

data = products.get_all_records()
df = pd.DataFrame(data)
# Creating a list of products from the "Product Name" column.
product_list = df['Product Name'].to_list()


sizes_data = SHEET.worksheet('Product size')

"""
Geting all values in the worksheet as DataFrame
"""
data_size = sizes_data.get_all_records()
df = pd.DataFrame(data_size)
# Creating a list of products sizes from the "Product Size" column.
product_size_list = df['Product Size'].to_list()


def get_valid_choice(menu_option):
    """
    Prompts the user to enter a choice between 1 and 5.
    Returns the valid choice if input is valid, otherwise None.
    """
    while True:  # Loop until valid input is received
        user_input = input(f"Please enter an integer between 1 and {menu_option}: \n")

        try:
            # Try to convert the input to an integer
            user_input = int(user_input)
            # Check if the value is between 1 and 5
            if 1 <= user_input <= menu_option:
                return user_input  # Return the valid input
            else:
                print(f"Invalid input. Please enter a number between 1 and {menu_option}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main_menu():
    """
    Displays "Main Menu" for user, ask to make a choice,
    check the choice and if is valid,
    returns value.
    """
    print("-----      Welcome in Natures Oils Stock System     --------")
    print("           ------------------------------------             ")
    print("            Please select one of the options:               ")
    print("            ------------------------------------            ")
    print("    1 - Update stock")
    print("    2 - Updated product list")
    print("    3 - Stock Report")
    print("    4 - Finsh")
    user_choice_main_menu = get_valid_choice(4)
    return int(user_choice_main_menu)


def update_stock_menu():
    """
    Displeys "Update stock Menu" for all goods in and orders out.
    """
    print("   You have choice 'Update stock' option:")
    print("   What you wants to update?: \n")
    print("   1 - Goods In.")
    print("   2 - Goods Out.")
    print("   3 - Return to main menu.")

    user_choice_stock_menu = get_valid_choice(3)  # check valid input

    return int(user_choice_stock_menu)  # user choice converted to integer


def report_meu():
    """
    Displeys "Report Menu" options
    """
    print(" Please choice one of the option")
    print(" ------------------------------")
    print("1 - Full Stock By Product")
    print("2 - Total Production")
    print("3 - Total Sale")
    print("4 - Return")
    user_choice_stock_menu = get_valid_choice(3)  # check valid input

    return int(user_choice_stock_menu)  # user choice converted to integer


def upddate_stock(choice, product_list):
    """
    Updating stock, all option goods in goods out and corrections.
    """

    current_date = datetime.now()  # Getting current date

    converted_date = current_date.strftime("%Y-%m-%d")

    if choice == "goods_in":  # For Goods In option

        data_in = []

        print("Please enter a numeric value for all products quantity.")
        """"
        Getting values from product_list varible ,
        products imported from worksheet.
        """

        for product in product_list:
            while True:
               """
               Getting values for each product from user
               """
            value = input(f"Many of {product} you wants to add to the stock?: \n")

            try:
                numeric_value = int(value) # Attempt to convert the input to a intager.
                     
                data_in.append((converted_date, product, numeric_value)) # If the conversion is successful, break the loop
                break
            except ValueError:
                     
                 print("Wrong value. Please enter a valid number.") # If error 

        return data_in

    elif choice == "goods_out":
        data_out = []
        print("Please enter a numeric value for all products quantity.") # Asking user for correct value

        for product in product_list:
            
            while True:
                  """
                  Use try: to check correct value inputed by user

                  """
                  value = input(f"How many of {product} was send out to customers?: \n")
                  try:
                     
                     numeric_value = int(value)
                     data_out.append((converted_date, product, numeric_value))# If the conversion is successful, break the loop
                     break
                  except ValueError:
                     print("Wrong value. Please enter a valid number.") # If conversion fails, print an error message
        return data_out


def update_worksheet(data, worksheet):
    """
    By geting data and worksheet updates appropriate spreadsheet.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    for record in data:
        record_as_list = [str(value) if not isinstance(value, (int, float)) else value for value in record]
        
        print(f"Appending record: {record_as_list}\n")  # Check the data format(added \n Statment!)

        try:
            worksheet_to_update.append_row(record_as_list)
            print(f"Successfully appended record: {record_as_list}")  # Confirmation of success
        except Exception as e:
            print(f"Failed to append record {record_as_list} due to error: {e}")
      
def add_new_product():
    """
    Asking user for updates product list, user can add new products, all information are 
    store in the dictionary and return from function.
    """
    """
    Add time.sleep() to delay displaying rules
    """
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

    """
    Collecting current date and formating to required format YYYY-MM-DD
    """ 
    current_date_load = datetime.now()
    current_date_new_product = current_date_load.strftime("%Y-%m-%d")

    
    new_product_name = input("Please enter a new product name: \n") # New Product fill by user

    """
    Validatting  product name inserted by user.
    """
    while len(new_product_name) > 20 or not all(char.isalpha() or char.isspace() for char in new_product_name) : #Max 20 characters and only letters and spaces.
        print("Error: Product name must be at most 20 characters long and contain only letters.")
        new_product_name = input("Please enter a new product name: \n")

   
    valid_sizes = ['220ml', '450ml', '860ml', '4.5L', '10L']  #list of evelible products sizes.
    
    print(f"Available sizes:{valid_sizes} ")

    new_product_size = input("Please enter new product size: \n")

    """
    Vallidating new product size
    """
    while new_product_size not in valid_sizes:
        print("Error: Please enter a valid product size.")
        new_product_size = input("Please enter new product size (options: 220ml, 450ml, 860ml, 4.5L, 10L): \n")

    
    while True:

        barcode = input("Please enter a 13-digit barcode: \n") # Min 13 digits

        """"
        Validate barcode
        """
        if len(barcode) == 13 and barcode.isdigit():
            break
        else:
            print("Invalid barcode, please enter 13-digit barcode")

    """
      Dictonary: data for new_product
    """
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

    """
    Creating list of data to be added to worksheet
    """ 

    row = [new_product["current_date"], new_product["product_name"], new_product["product_size"], new_product["barcode"]]
        

    worksheet_to_update.append_row(row)

    print("Product list have be updated!")

def get_value_by_product_name(product_name, worksheet):
    """
    By taking the product name and worksheet name,
     it calculates and returns a list includs: 
    'current date',
    'Product Name',
     'QTY'
    """
    goods_in_data = SHEET.worksheet(worksheet) # depend on workssheet.

    records = goods_in_data.get_all_records()
     
    df = pd.DataFrame(records)

    if 'Product Name' in df.columns and 'QTY' in df.columns:
        filtered_df = df[df['Product Name'] == 'Taco Sauce']
        qty_sum = int(filtered_df['QTY'].sum())

        result = [datetime.now().strftime("%m/%d/%Y"), product_name, qty_sum]
        return result
    else:
        raise ValueError("Required columns 'Product Name' and 'QTY' are not in the DataFrame.")   


def get_value_by_product_name_test(product_name, worksheet):
    """
    By taking the product name and worksheet name,
     it calculates and returns a list including: 
    'current date',
    'Product Name',
    'QTY'
    """
    goods_in_data = SHEET.worksheet(worksheet)  # depend on worksheet.

    records = goods_in_data.get_all_records()

    df = pd.DataFrame(records)

    if 'Product Name' in df.columns and 'QTY' in df.columns:
        filtered_df = df[df['Product Name'] == product_name]
        qty_sum = int(filtered_df['QTY'].sum())

        result = [datetime.now().strftime("%m/%d/%Y"), product_name, qty_sum]
        return result
    else:
        raise ValueError("Required columns 'Product Name' and 'QTY' are not in the DataFrame.")


def get_all_product_values(product_list, worksheet):
    """
    Takes a list of products and a worksheet name,
    and returns a list of product details including
    current date, product name, and quantity for each product.
    """
    results = []
    for product_name in product_list:
        product_info = get_value_by_product_name_test(product_name, worksheet)
        results.append(product_info)
        print(f"{product_info[1]} - {product_info[2]}")

    return results

def get_value_by(product_name, worksheet):
    """
    By taking the product name and worksheet name,
    it calculates and returns the quantity for the product.
    """
    goods_data = SHEET.worksheet(worksheet)  # depend on worksheet.

    records = goods_data.get_all_records()
    df = pd.DataFrame(records)

    if 'Product Name' in df.columns and 'QTY' in df.columns:
        filtered_df = df[df['Product Name'] == product_name]
        qty_sum = int(filtered_df['QTY'].sum())
        return qty_sum
    else:
        raise ValueError("Required columns 'Product Name' and 'QTY' are not in the DataFrame.")


def calculate_stock(product_list):
    """
    Takes a list of products
    and returns a list of product details including the current date,
    product name, and calculated stock quantity for each product.
    """
    results = []
    for product_name in product_list:
        qty_in = get_value_by(product_name, 'Product Good In')
        qty_out = get_value_by(product_name, 'Product Good Out')
        stock = qty_in - qty_out
        
        result = [datetime.now().strftime("%m/%d/%Y"), product_name, stock]
        results.append(result)
        print(f"{result[1]} - {result[2]}")  # Display the product stock

    return results  

def main():
    """
    Main function run the program
    """
    while True:
      user_choice = main_menu()
      if user_choice == 1:
         while True:
             choice_I = update_stock_menu()
             if choice_I == 1 : #choice 1 updtate product goods in
                data_in = upddate_stock("goods_in", product_list)
                update_worksheet(data_in, "Product Good In")
             elif choice_I == 2 : #choice 2 update product goods out
                data_out = upddate_stock("goods_out", product_list)
                update_worksheet(data_out, "Product Good Out")
             elif choice_I == 3:
                   print("Exiting the menu. Goodbye!")
                   break  # Exit the loop
             else:
                 print("Invalid choice. Please select a number between 1 and 3.")
      elif user_choice == 2:
                new_product_data = add_new_product()
                update_worksheet_new_product(new_product_data,'Product List')
      elif user_choice == 3:
        while True:
             choice_II = report_meu()
             if choice_II == 1 : # choice 1 display stock by product
                calculate_stock(product_list) # Function display stock
             elif choice_II == 2 : # choice 2 display production for all products
                get_all_product_values(product_list, "Product Good In")
             elif choice_II == 3 :# choice 3 display sale values.
                get_all_product_values(product_list, "Product Good Out")   
             elif choice_II == 4:
                   print("Exiting the menu. Goodbye!")
                   break  # Exit the loop
             else:
                 print("Invalid choice. Please select a number between 1 and 3.")
      elif user_choice == 4:
        print("Exiting the menu. Goodbye!")
        break  # Exit the loop
      else:
         print("Invalid choice. Please select a number between 1 and 4.\n")
         print("Please select one number from 1 to 4 and pres enter! ")


    
main()
