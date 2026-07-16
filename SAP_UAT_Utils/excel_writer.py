from openpyxl import load_workbook
from pathlib import Path

# =====================================================================
# PASTE THIS METHOD INTO YOUR EXISTING SAP_UAT_Utils/excel_writer.py
# Add it as another @staticmethod inside your ExcelWriter class.
# =====================================================================

# =====================================
# SAP New Business - Save Policy Result
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
                sheet.cell(row=row, column=8).value = policy_details["Business Partner"]
                sheet.cell(row=row, column=9).value = policy_details["Commission Contract"]
                sheet.cell(row=row, column=10).value = policy_details["Nature of Risk"]
                sheet.cell(row=row, column=11).value = policy_details["State"]
                sheet.cell(row=row, column=12).value = policy_details["Limit Amount"]
                sheet.cell(row=row, column=13).value = "Processed"

                break

        workbook.save(excel_file)
        print("SAP New Business Policy Summary Updated")