from openpyxl import load_workbook
from pathlib import Path


class ExcelWriter:
    # =====================================
    # Dental Policy Update
    # Match using MyKadID
    # Policy Number -> Column 3
    # =====================================
    @staticmethod
    def update_dental_details(sheet_name, mykad, policy_details):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_mykad = str(sheet.cell(row=row, column=1).value)

            if excel_mykad == str(mykad):

                sheet.cell(row=row, column=3).value = policy_details["Quote Number"]  # D
                sheet.cell(row=row, column=4).value = policy_details["Policy Number"]  # E

                # ---------------- Numeric columns: force 2-decimal display ----------------
                numeric_cols = {

                    5: "Gross Premium",
                    6: "SST",
                    7: "Stamp Duty",
                    8: "Total Premium",
                }

                for col, key in numeric_cols.items():
                    cell = sheet.cell(row=row, column=col)
                    cell.value = policy_details[key]
                    cell.number_format = "0.00"

                sheet.cell(row=row, column=9).value = "Downloaded Automatically"
                sheet.cell(row=row, column=10).value = "Downloaded Automatically"
                sheet.cell(row=row, column=11).value = "playwright.test@serole.com"

                break

        workbook.save(excel_file)
        print("Policy Summary Updated")
    # =====================================
    # PA Endorsement / Correction
    # Policy Number -> Column 1
    # First Empty Row
    # =====================================
    @staticmethod
    def update_pa_policy_details(sheet_name, mykad, policy_details):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]

        # Find matching MyKad row
        for row in range(2, sheet.max_row + 1):

            excel_mykad = str(sheet.cell(row=row, column=1).value)

            if excel_mykad == str(mykad):

                # Quote Number
                sheet.cell(row=row, column=4).value = policy_details["Quote Number"]

                # Policy Number
                sheet.cell(row=row, column=5).value = policy_details["Policy Number"]

                numeric_cols = {
                    6: "Sum Insured",
                    7: "Gross Premium",
                    8: "SST",
                    9: "Stamp Duty",
                    10: "Total Premium",
                }

                for col, key in numeric_cols.items():
                    cell = sheet.cell(row=row, column=col)
                    cell.value = policy_details[key]
                    cell.number_format = "0.00"

                sheet.cell(row=row, column=11).value = "Downloaded Automatically"
                sheet.cell(row=row, column=12).value = "Downloaded Automatically"
                sheet.cell(row=row, column=13).value = "playwright.test@serole.com"

                break

        workbook.save(excel_file)

        print("Policy Summary Updated")
    # =====================================
    # PC_RV & MC_RV Motor details
    # =====================================
    @staticmethod
    def update_motor_pc_mc_rv_details(sheet_name, reg_no, policy_details):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_reg_no = str(sheet.cell(row=row, column=1).value)

            if excel_reg_no == str(reg_no):

                sheet.cell(row=row, column=3).value = policy_details["Selected Coverage"]  # C
                sheet.cell(row=row, column=4).value = policy_details["Policy Holder"]  # D
                sheet.cell(row=row, column=5).value = policy_details["Quote Number"]  # E
                sheet.cell(row=row, column=6).value = policy_details["Policy Number"]  # F

                # ---------------- Numeric columns: force 2-decimal display ----------------
                numeric_cols = {
                    7: "Sum Insured",
                    8: "Act Premium",
                    9: "Basic Premium",
                    10: "NCD",
                    11: "Premium after NCD",
                    12: "Gross Premium",
                    13: "SST",
                    14: "Stamp Duty",
                    15: "Total Premium",
                }

                for col, key in numeric_cols.items():
                    cell = sheet.cell(row=row, column=col)
                    cell.value = policy_details[key]
                    cell.number_format = "0.00"

                sheet.cell(row=row, column=16).value = "Downloaded Automatically"
                sheet.cell(row=row, column=17).value = "Downloaded Automatically"
                sheet.cell(row=row, column=18).value = "playwright.test@serole.com"

                break

        workbook.save(excel_file)
        print("Policy Summary Updated")

    # =====================================
    # MC_RV Motor Quote & policy Number Update
    # =====================================
    @staticmethod
    def update_motor_cv_rv_details(sheet_name, reg_no, policy_details):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_reg_no = str(sheet.cell(row=row, column=1).value)

            if excel_reg_no == str(reg_no):
                sheet.cell(row=row, column=3).value = policy_details["Selected Coverage"]  # C
                sheet.cell(row=row, column=4).value = policy_details["Policy Holder"]  # D
                sheet.cell(row=row, column=8).value = policy_details["Quote Number"]  # G
                sheet.cell(row=row, column=9).value = policy_details["Policy Number"]  # H

                # ---------------- Numeric columns: force 2-decimal display ----------------
                numeric_cols = {
                    10: "Sum Insured",
                    11: "Act Premium",
                    12: "Basic Premium",
                    13: "NCD",
                    14: "Premium after NCD",
                    15: "Gross Premium",
                    16: "SST",
                    17: "Stamp Duty",
                    18: "Total Premium",
                }

                for col, key in numeric_cols.items():
                    cell = sheet.cell(row=row, column=col)
                    cell.value = policy_details[key]
                    cell.number_format = "0.00"

                sheet.cell(row=row, column=19).value = "Downloaded Automatically"
                sheet.cell(row=row, column=20).value = "Downloaded Automatically"
                sheet.cell(row=row, column=21).value = "playwright.test@serole.com"

        workbook.save(excel_file)
        print("Policy Summary Updated")

    # =====================================
    # PC_NV Motor Quote & policy Number Update
    # =====================================
    @staticmethod
    def update_motor_pc_nv_details(sheet_name, mykad, quote_number, policy_number):

        project_root = Path(__file__).parent.parent

        excel_file = (project_root / "testdata_excel" / "test_data.xlsx")

        workbook = load_workbook(excel_file)

        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_mykad = str(sheet.cell(row=row, column=1).value)

            if excel_mykad == str(mykad):
                # Quote Number
                sheet.cell(row=row, column=5).value = quote_number
                # Policy Number
                sheet.cell(row=row, column=6).value = policy_number

                break

        workbook.save(excel_file)

        print(f"Quote Number : {quote_number}")

        print(f"Policy Number : {policy_number}")