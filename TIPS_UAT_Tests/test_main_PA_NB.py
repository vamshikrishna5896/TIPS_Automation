import pytest
import allure

from TIPS_UAT_Pages.home_page import HomePage
from TIPS_UAT_Pages.login_page import LoginPage
from TIPS_UAT_Pages.PA_NB_policy_page import Policycreation
from TIPS_UAT_Utils.excel_reader import ExcelReader
from TIPS_UAT_Utils.excel_writer import ExcelWriter

test_data = ExcelReader.get_test_data("PA")

@pytest.mark.parametrize("data", [test_data[12]])    # ========>  If want Run only first row from Excel
#@pytest.mark.parametrize("data", test_data[1:5])   # =========> If want to Run 1 to 5 Rows in Excel
#@pytest.mark.parametrize("data",test_data)

@allure.epic("Personal Accident Insurance")
@allure.feature("Personal Accident")
@allure.story("Create New Policy")
@allure.title("Personal Accident Policy Creation")
def test_create_pa_policy(page, data):

    login = LoginPage(page)
    login.login()

    home = HomePage(page)

    quote = Policycreation(page)

    home.navigate_to_new_quote()

    # ===================================== Date Type  =====================================#
    date_type = "tomorrow"

    policy_details = quote.create_personal_accident_quote(mykad=str(data["MyKadID"]), customer_name=data["Name"],
                                         date_type=date_type, product_type=data["ProductType"])
    # =====================================
    # Save Policy Number Based On Date Type
    # =====================================

    if date_type in ["today", "yesterday"]:
        # ======= Policy details saved in PA Sheet======= #
        ExcelWriter.update_pa_policy_details("PA", str(data["Sno"]), policy_details)
        print("Policy details saved in PA sheet")

        # ================= Policy Number saved in PA_Correction sheet ========= #
        ExcelWriter.update_pa_correction_policy_number("PA_Correction", policy_details["Policy Number"])
        print("Policy Number saved in PA_Correction sheet")

    elif date_type in ["tomorrow", "day_after_tomorrow"]:
        # ======= Policy details saved in PA Sheet======= #
        ExcelWriter.update_pa_policy_details("PA", str(data["Sno"]), policy_details)
        print("Policy details saved in PA sheet")

        # ================= Policy Number saved in PA_Correction sheet ========= #
        ExcelWriter.update_pa_correction_policy_number("PA_Correction", policy_details["Policy Number"])
        print("Policy Number saved in PA_Correction sheet")


    print(f"MyKad : {data['MyKadID']}")
    print(f"Name : {data['Name']}")
    print(f"Quote Number   : {policy_details['Quote Number']}")
    print(f"Policy Number  : {policy_details['Policy Number']}")

    assert True