import pytest
import allure

from TIPS_Pages.home_page import HomePage
from TIPS_Pages.PA_NB_policy_page import Policycreation
from TIPS_utils.excel_reader import ExcelReader
from TIPS_utils.excel_writer import ExcelWriter


test_data = ExcelReader.get_test_data("PA")

@pytest.mark.parametrize("data", [test_data[0]])    # ========>  If want Run only first row from Excel
#@pytest.mark.parametrize("data", test_data[1:5])   # =========> If want to Run 1 to 5 Rows in Excel
#@pytest.mark.parametrize("data",test_data)
def test_create_quote(page, data):

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

        ExcelWriter.update_pa_policy_details("PA", str(data["MyKadID"]), policy_details)

        print("Policy saved in PA sheet")

    elif date_type in ["tomorrow", "day_after_tomorrow"]:

        ExcelWriter.update_pa_policy_details("PA", str(data["MyKadID"]), policy_details)

        print("Policy saved in PA sheet")

        #ExcelWriter.update_pa_policy_details("PA_Correction",policy_details=policy_details )
        print("Policy saved in PA_Correction sheet")

    print(f"MyKad : {data['MyKadID']}")
    print(f"Name : {data['Name']}")
    print(f"Quote Number   : {policy_details['Quote Number']}")
    print(f"Policy Number  : {policy_details['Policy Number']}")

    assert True