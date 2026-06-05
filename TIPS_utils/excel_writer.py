from openpyxl import load_workbook
from pathlib import Path


class ExcelWriter:

    @staticmethod
    def update_policy_number(
            sheet_name,
            mykad,
            policy_no):

        project_root = Path(__file__).parent.parent

        excel_file = (
            project_root
            / "testdata_excel"
            / "test_data.xlsx"
        )

        workbook = load_workbook(excel_file)

        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            if str(sheet.cell(row, 1).value) == str(mykad):

                sheet.cell(
                    row=row,
                    column=3
                ).value = policy_no

                break

        workbook.save(excel_file)