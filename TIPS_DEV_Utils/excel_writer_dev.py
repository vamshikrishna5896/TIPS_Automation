from openpyxl import load_workbook
from pathlib import Path

class ExcelWriter:

    # =====================================
    # Save details in PA Sheet
    # =====================================
    @staticmethod
    def update_pa_policy_details(sheet_name, sno, policy_details):
        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data_DEV.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]

        # Find matching MyKad row
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
    # Dental Policy Update
    # =====================================
    @staticmethod
    def update_dental_details(sheet_name, sno, policy_details):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data.xlsx"

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
    # PC_RV & MC_RV Motor details
    # =====================================

    @staticmethod
    def update_motor_pc_mc_rv_details(sheet_name, reg_no, policy_details):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data_DEV.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_reg_no = str(sheet.cell(row=row, column=1).value)

            if excel_reg_no == str(reg_no):

                sheet.cell(row=row, column=6).value = policy_details["Selected Coverage"]  # C
                sheet.cell(row=row, column=7).value = policy_details["Policy Holder"]  # D
                sheet.cell(row=row, column=8).value = policy_details["Quote Number"]  # E
                sheet.cell(row=row, column=9).value = policy_details["Policy Number"]  # F

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

                break

        workbook.save(excel_file)
        print("Policy Summary Updated")
