import smartsheet
import logging
import os
import gui as g

_dir = os.path.dirname(os.path.abspath(__file__))


def getLogin():
    loginInfo = open("login.txt", "r") \
        .readline() \
        .split(";")

    return loginInfo[0], loginInfo[1], loginInfo[2]


print("Starting ...")

# Sheet Setup
smart = smartsheet.Smartsheet(access_token=getLogin()[2])
smart.errors_as_exceptions(True)
logging.basicConfig(filename='rwsheet.log', level=logging.INFO)

# Variables
sheet_name = "pho_review_data"
rows_list = []
column_map = {}


# Helper Functions
def add_row_to_sheet(sheet, row_data):
    new_row = smartsheet.models.Row()
    new_row.to_bottom = True

    sheet_id = sheet.id
    sheet_columns = sheet.get_columns(sheet_id).data
    col_ids = []

    for col in sheet_columns:
        col_ids.append(col.id)

    sheet_column_count = len(col_ids)

    keys = list(row_data.keys())

    for i in range(sheet_column_count):
        data = \
            {
                'column_id': col_ids[i],
                'value': row_data[keys[i]]
            }
        new_row.cells.append(data)

    return new_row


# Search for the sheet by name, if it exists then we can begin the app if not create it
sheets = smart.Sheets.list_sheets(include_all=True)
found_sheet = None
for sheet in sheets.data:
    if sheet.name == sheet_name:
        found_sheet = sheet
        break


def app():
    rows_to_add = []
    g.gui(rows_to_add)

    for row in rows_to_add:
        n_row = add_row_to_sheet(found_sheet, row)
        rows_list.append(n_row)

    found_sheet.add_rows(rows_list)


# Sheet exists, you can now add data to it
if found_sheet:
    app()
    print("App closing... Please check Smartsheet to verify data entered")
else:
    print("Creating pho_review_data Smartsheet...")
    result = smart.Sheets.import_csv_sheet(_dir + "/pho_review_data.csv", header_row_index=0)
    print("Rerun program to begin adding to newly created Smartsheet!")
