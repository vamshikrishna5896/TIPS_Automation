from openpyxl import load_workbook
from pathlib import Path


class ExcelWriter:

    # =====================================
    # PA & Dental Policy Number Update
    # Sheet1 -> PA
    # Sheet2 -> Dental
    # Match using MyKadID
    # =====================================
    @staticmethod
    def update_policy_number(
            sheet_name,
            mykad,
            policy_number):

        project_root = Path(__file__).parent.parent

        excel_file = (project_root /"testdata_excel" /"test_data.xlsx")

        workbook = load_workbook(excel_file)

        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_mykad = str(sheet.cell(row=row,column=1).value)

            if excel_mykad == str(mykad):

                # Column 3 = Policy Number
                sheet.cell(row=row,column=3).value = policy_number

                break

        workbook.save(excel_file)

        print(f"Policy Number {policy_number} "f"updated successfully")

    # =====================================
    # Motor Policy Number Update
    # Sheet3 -> Motor
    # Match using RegNo
    # =====================================
    @staticmethod
    def update_motor_policy_number(sheet_name,reg_no,policy_number):

        project_root = Path(__file__).parent.parent

        excel_file = (project_root /"testdata_excel" /"test_data.xlsx")

        workbook = load_workbook(excel_file)

        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_reg_no = str(sheet.cell(row=row,column=1).value)

            if excel_reg_no == str(reg_no):

                # Column 4 = Policy Number
                sheet.cell(row=row,column=4).value = policy_number

                break

        workbook.save(excel_file)

        print(f"Motor Policy Number "f"{policy_number} "f"updated successfully")