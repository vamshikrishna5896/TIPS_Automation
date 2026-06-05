from openpyxl import load_workbook
from pathlib import Path


class ExcelWriter:

    @staticmethod
    def update_policy_number(sheet_name,mykad,policy_number):

        project_root = Path(__file__).parent.parent

        excel_file = (project_root /"testdata_excel" /"test_data.xlsx")

        workbook = load_workbook(excel_file)

        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_mykad = str(sheet.cell(row=row,column=1).value)

            if excel_mykad == str(mykad):

                sheet.cell(row=row,column=3).value = policy_number

                break

        workbook.save(excel_file)

        print(f"Policy Number {policy_number} updated successfully")