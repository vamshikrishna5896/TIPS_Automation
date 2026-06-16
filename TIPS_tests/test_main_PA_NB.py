import pytest
import allure

from TIPS_Pages.home_page import HomePage
from TIPS_Pages.PA_NB_policy_page import Policycreation
from TIPS_utils.excel_reader import ExcelReader
from TIPS_utils.excel_writer import ExcelWriter


test_data = ExcelReader.get_test_data("PA")

@pytest.mark.parametrize("data", [test_data[0]])

def test_create_quote(page, data):

    home = HomePage(page)

    quote = Policycreation(page)

    home.navigate_to_new_quote()

    # =====================================
    # Date Type
    # =====================================
    date_type = "tomorrow"

    quote.create_personal_accident_quote(mykad=str(data["MyKadID"]), customer_name=data["Name"],
                                         date_type=date_type, product_type=data["ProductType"])

    # =====================================
    # Get Policy Number
    # =====================================
    policy_number = quote.get_policy_number()

    # =====================================
    # Save Policy Number Based On Date Type
    # =====================================

    if date_type in ["today", "yesterday"]:

        ExcelWriter.update_pa_policy_number("PA_Endo", policy_number)

        print("Policy saved in PA_Endo sheet")

    elif date_type in ["tomorrow", "day_after_tomorrow"]:

        ExcelWriter.update_pa_policy_number("PA_Correction", policy_number)

        print("Policy saved in PA_Correction sheet")

    print(f"MyKad : {data['MyKadID']}")
    print(f"Name : {data['Name']}")
    print(f"Policy Number : {policy_number}")

    assert True