import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook


def export_to_excel(connection, query_string, headings, filepath):
    cursor = connection.cursor()
    cursor.execute(query_string)
    data = cursor.fetchall()
    cursor.close()


# Create a Workbook
    wb = Workbook() # The Workbook is a Class for Excel file in openpyxl.
    ws = wb.active
    ws.title = "Lista"
    wb.save (filename = 'assets/planilhas/lista.xlsx')

    wb = load_workbook('lista.xlsx')
    print(wb.sheetnames)