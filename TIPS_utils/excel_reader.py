from openpyxl import load_workbook
from pathlib import Path

class ExcelReader:

    @staticmethod
    def get_test_data():

        project_root = Path(__file__).parent.parent

        excel_file = (project_root/ "testdata_excel"/ "test_data.xlsx")

        workbook = load_workbook(excel_file)

        print(workbook.sheetnames)

        sheet = workbook["Sheet1"]

        data = []

        for row in sheet.iter_rows(
                min_row=2,
                values_only=True):

            data.append({
                "mykad": str(row[0]),
                "name": row[1]
            })

        return data