import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPRED_CLIENT = gspred.authorize(SCOPED_CREDS)
SHEET -GSPRED_CLIENT.open('love_sandwidges')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)

# import os
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     #return '<h1>'Hello, World'<,h1>'
#     return render_template('index.html')


# if __name__ == '__main__':
#     app.run(
#         host=os.environ.get("IP", "0.0.0.0"),
#         port=int(os.environ.get("PORT", 5000)),
#         debug=True #change this to False
#     )