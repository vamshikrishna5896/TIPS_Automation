from openpyxl import load_workbook
from pathlib import Path


class ExcelWriter:
    # =====================================
    # Dental Policy Update
    # =====================================
    @staticmethod
    def update_dental_details(sheet_name, sno, policy_details):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data_UAT.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_sno = str(sheet.cell(row=row, column=1).value)

            if excel_sno == str(sno):

                sheet.cell(row=row, column=6).value = policy_details["Quote Number"]  # D
                sheet.cell(row=row, column=7).value = policy_details["Policy Number"]  # E

                # ---------------- Numeric columns: force 2-decimal display ----------------
                numeric_cols = {

                    8: "Gross Premium",
                    9: "SST",
                    10: "Stamp Duty",
                    11: "Total Premium",
                }

                for col, key in numeric_cols.items():
                    cell = sheet.cell(row=row, column=col)
                    cell.value = policy_details[key]
                    cell.number_format = "0.00"

                sheet.cell(row=row, column=12).value = "Downloaded Automatically"
                sheet.cell(row=row, column=13).value = "Downloaded Automatically"
                sheet.cell(row=row, column=14).value = "playwright.test@serole.com"

                break

        workbook.save(excel_file)
        print("Policy Summary Updated")
    # =====================================
    # Save details in PA Sheet
    # =====================================
    @staticmethod
    def update_pa_policy_details(sheet_name, sno, policy_details):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data_UAT.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]


        for row in range(2, sheet.max_row + 1):

            excel_sno = str(sheet.cell(row=row, column=1).value)

            if excel_sno == str(sno):

                # Quote Number
                sheet.cell(row=row, column=7).value = policy_details["Quote Number"]

                # Policy Number
                sheet.cell(row=row, column=8).value = policy_details["Policy Number"]

                numeric_cols = {
                     9: "Sum Insured",
                    10: "Gross Premium",
                    11: "SST",
                    12: "Stamp Duty",
                    13: "Total Premium",
                }

                for col, key in numeric_cols.items():
                    cell = sheet.cell(row=row, column=col)
                    cell.value = policy_details[key]
                    cell.number_format = "0.00"

                sheet.cell(row=row, column=14).value = "Downloaded Automatically"
                sheet.cell(row=row, column=15).value = "Downloaded Automatically"
                sheet.cell(row=row, column=16).value = "playwright.test@serole.com"

                break

        workbook.save(excel_file)

        print("Policy Summary Updated")

    # =====================================
    # PA Correction - Save Policy Number
    # =====================================
    @staticmethod
    def update_pa_correction_policy_number(sheet_name, policy_number):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data_UAT.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]

        # Find first empty row in Column A
        for row in range(2, sheet.max_row + 2):

            if sheet.cell(row=row, column=1).value in [None, ""]:
                # Column A = Policy Number
                sheet.cell(row=row, column=1).value = policy_number

                break

        workbook.save(excel_file)

        print(f"Policy Number {policy_number} saved in {sheet_name}")

    # =====================================
    # PC_RV & MC_RV Motor details
    # =====================================
    @staticmethod
    def update_motor_pc_mc_rv_details(sheet_name, sno, policy_details):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data_UAT.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_sno = str(sheet.cell(row=row, column=1).value)

            if excel_sno == str(sno):

                sheet.cell(row=row, column=6).value = policy_details["Selected Coverage"]  # C
                sheet.cell(row=row, column=7).value = policy_details["Policy Holder"]  # D
                sheet.cell(row=row, column=8).value = policy_details["Quote Number"]  # E
                sheet.cell(row=row, column=9).value = policy_details["Policy Number"]  # F

                # ---------------- Numeric columns: force 2-decimal display ----------------
                numeric_cols = {
                    10 : "Sum Insured",
                    11 : "Act Premium",
                    12 : "Basic Premium",
                    13 : "NCD",
                    14 : "Premium after NCD",
                    15 : "Gross Premium",
                    16 : "SST",
                    17 : "Stamp Duty",
                    18 : "Total Premium",
                }

                for col, key in numeric_cols.items():
                    cell = sheet.cell(row=row, column=col)
                    cell.value = policy_details[key]
                    cell.number_format = "0.00"

                sheet.cell(row=row, column=19).value = "Downloaded Automatically"
                sheet.cell(row=row, column=20).value = "Downloaded Automatically"
                sheet.cell(row=row, column=21).value = "playwright.test@serole.com"

                break

        workbook.save(excel_file)
        print("Policy Summary Updated")

    # =====================================
    # MC_RV Motor Quote & policy Number Update
    # =====================================
    @staticmethod
    def update_motor_cv_rv_details(sheet_name, sno, policy_details):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data_UAT.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_sno = str(sheet.cell(row=row, column=1).value)

            if excel_sno == str(sno):
                sheet.cell(row=row, column=6).value = policy_details["Selected Coverage"]  # C
                sheet.cell(row=row, column=7).value = policy_details["Policy Holder"]  # D
                sheet.cell(row=row, column=10).value = policy_details["Quote Number"]  # G
                sheet.cell(row=row, column=11).value = policy_details["Policy Number"]  # H

                # ---------------- Numeric columns: force 2-decimal display ----------------
                numeric_cols = {
                    12: "Sum Insured",
                    13: "Act Premium",
                    14: "Basic Premium",
                    15: "NCD",
                    16: "Premium after NCD",
                    17: "Gross Premium",
                    18: "SST",
                    19: "Stamp Duty",
                    20: "Total Premium",
                }

                for col, key in numeric_cols.items():
                    cell = sheet.cell(row=row, column=col)
                    cell.value = policy_details[key]
                    cell.number_format = "0.00"

                sheet.cell(row=row, column=21).value = "Downloaded Automatically"
                sheet.cell(row=row, column=22).value = "Downloaded Automatically"
                sheet.cell(row=row, column=23).value = "playwright.test@serole.com"

        workbook.save(excel_file)
        print("Policy Summary Updated")

    # =====================================
    # PC_NV Motor Quote & policy Number Update
    # =====================================
    @staticmethod
    def update_motor_pc_nv_details(sheet_name, mykad, quote_number, policy_number):

        project_root = Path(__file__).parent.parent

        excel_file = (project_root / "testdata_excel" / "test_data_UAT.xlsx")

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