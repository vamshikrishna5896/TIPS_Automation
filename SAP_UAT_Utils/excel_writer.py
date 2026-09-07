from openpyxl import load_workbook
from pathlib import Path

# =====================================
# SAP New Business - BI sheet update utility
# =====================================
class ExcelWriter:
    @staticmethod

    def update_sap_nb_details(sheet_name, sno, policy_details):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data_SAP.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_sno = str(sheet.cell(row=row, column=1).value)

            if excel_sno == str(sno):

                # Adjust these column numbers to match where you want
                # the results written in your NB_BI sheet.
                sheet.cell(row=row, column=10).value = policy_details["Effective Date"]
                sheet.cell(row=row, column=11).value = policy_details["Policy Holder"]
                sheet.cell(row=row, column=12).value = policy_details["Policy Number"]
                sheet.cell(row=row, column=13).value = policy_details["Application Number"]

                break

        workbook.save(excel_file)
        print("SAP New Business BI Policy Summary Updated")

    # =====================================
    # SAP New Business - PC sheet update utility
    # =====================================
    @staticmethod
    def update_sap_nb_pc_details(sheet_name, sno, policy_details):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data_SAP.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_sno = str(sheet.cell(row=row, column=1).value)

            if excel_sno == str(sno):

                sheet.cell(row=row, column=12).value = policy_details["Effective Date"]
                sheet.cell(row=row, column=13).value = policy_details["Policy Holder"]
                sheet.cell(row=row, column=14).value = policy_details["Policy Number"]
                sheet.cell(row=row, column=15).value = policy_details["Application Number"]
                # sheet.cell(row=row, column=16).value = policy_details["premium_before_tax"]
                # sheet.cell(row=row, column=17).value = policy_details["Cum.Tax/Submissn Amt"]
                # sheet.cell(row=row, column=18).value = policy_details["Premium After Tax"]
                # sheet.cell(row=row, column=19).value = policy_details["Stamp Duty"]
                # sheet.cell(row=row, column=20).value = policy_details["Basic Premium"]
                break

        workbook.save(excel_file)
        print("PC Policy Details Updated")

        # =====================================
        # SAP New Business - MC sheet update utility
        # =====================================

    @staticmethod
    def update_sap_nb_mc_details(sheet_name, sno, policy_details):

        project_root = Path(__file__).parent.parent
        excel_file = project_root / "testdata_excel" / "test_data_SAP.xlsx"

        workbook = load_workbook(excel_file)
        sheet = workbook[sheet_name]

        for row in range(2, sheet.max_row + 1):

            excel_sno = str(sheet.cell(row=row, column=1).value)

            if excel_sno == str(sno):
                sheet.cell(row=row, column=8).value = policy_details["Effective Date"]
                sheet.cell(row=row, column=9).value = policy_details["Policy Holder"]
                sheet.cell(row=row, column=10).value = policy_details["Policy Number"]
                sheet.cell(row=row, column=11).value = policy_details["Application Number"]

                break

        workbook.save(excel_file)
        print("PC Policy Details Updated")