import pytest
import allure

#from TIPS_UAT_Pages.home_page import HomePage
from TIPS_DEV_Pages.login_page_dev import LoginPage
from TIPS_DEV_Pages.PA_NB_page_dev import Policycreation
from TIPS_DEV_Utils.excel_reader_dev import ExcelReader
from TIPS_DEV_Utils.excel_writer_dev import ExcelWriter

test_data = ExcelReader.get_test_data("PA")

@pytest.mark.parametrize("data", [test_data[2]])

@allure.epic("Personal Accident Insurance")
@allure.feature("Personal Accident")
@allure.story("Create New Policy")
@allure.title("Personal Accident Policy Creation")
def test_create_pa_policy(page, data):

    login = LoginPage(page)
    login.login()

    login.navigate_to_new_quote()

    quote = Policycreation(page)


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

    elif date_type in ["tomorrow", "day_after_tomorrow"]:
        # ======= Policy details saved in PA Sheet======= #
        ExcelWriter.update_pa_policy_details("PA", str(data["Sno"]), policy_details)
        print("Policy details saved in PA sheet")



    print(f"MyKad : {data['MyKadID']}")
    print(f"Name : {data['Name']}")
    print(f"Quote Number   : {policy_details['Quote Number']}")
    print(f"Policy Number  : {policy_details['Policy Number']}")

    assert True