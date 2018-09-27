import sys
import xlrd
from db_table import db_table

## build_table
## params: file_name:String path to workbook file
## return: None
## This fuction takes the path of a .xls file agenda file
## and builds an agenda table based on the contents of the workbook.
def build_table(file_name):
    agenda_table = db_table("agenda", { "id": "integer PRIMARY KEY", 
                                        "date": "text NOT NULL", 
                                        "start_time": "text NOT NULL", 
                                        "end_time": "text NOT NULL",
                                        "title": "text NOT NULL",
                                        "location": "text",
                                        "description": "text"})

    book = xlrd.open_workbook(file_name)
    if book is None:
        print("Please provide a valid path to a workbook.")
        exit(1)

    worksheet = book.sheet_by_index(0)

    for i in range(13, worksheet.nrows): ## Starting at row 14, assuming the first 13 rows are metadata/examples
        row = worksheet.row(i)
        if len(row) < 6:
            continue

        date = row[0].value.replace("'", "''")
        start = row[1].value.replace("'", "''")
        end = row[2].value.replace("'", "''")
        title = row[3].value.replace("'", "''")
        location = row[4].value.replace("'", "''")
        description = row[5].value.replace("'", "''")

        agenda_table.insert({"date" : date, 
                            "start_time" : start,
                            "end_time" : end,
                            "title" : title,
                            "location" : location,
                            "description" : description})

def main():
    if len(sys.argv) < 2:
        print("Usage: import_agenda.py <file path>")
        exit(1)

    build_table(sys.argv[1])


main()