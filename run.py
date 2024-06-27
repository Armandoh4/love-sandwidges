# import gspread
# from google.oauth2.service_account import Credentials
from pprint import pprint
# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]

# CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPRED_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPRED_CLIENT.open('love_sandwiches')

# sales = SHEET.worksheet('sales')

# data = sales.get_all_values()

# print(data)

def get_sales_data():
    """
    Get sales data
    """
    while True:
        print("Please enter sales data from the last market")
        print("Data should ne six numbers, seperated by commas.")
        print("example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print('Data is valid')
            break
    return sales_data

def validate_data(values):
    """"
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there arn't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def update_sales_worksheet(data):
    # Update sale workshhet, add new row
    print('update_sales_worksheet...\n')
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print('Sales worksheet upsated successfully')

def calculate_surplus_data(sales_row):
    print('calculating surplus data\n')
    stock = SHEET.worksheet('stock').get_all_values()
    stock_row = stock[-1]
    # pprint(stock)

def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)

print("welcome to love-sandwidges data automation")
main()
    