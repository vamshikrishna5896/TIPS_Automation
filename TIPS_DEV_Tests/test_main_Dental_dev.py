import pytest
import allure


from TIPS_DEV_Pages.login_page_dev import LoginPage
from TIPS_DEV_Pages.Dental_NB_Page_dev import DentalPolicyPage
from TIPS_DEV_Utils.excel_reader_dev import ExcelReader
from TIPS_DEV_Utils.excel_writer_dev import ExcelWriter

test_data = ExcelReader.get_test_data("Dental")

# @allure.epic("Dental Insurance")
# @allure.feature("Dental Shield")
# @allure.story("Create New Policy")
# @allure.title("Dental Policy Creation")

@pytest.mark.parametrize("data",[test_data[0]])

def test_create_dental_policy(page,data):


    login = LoginPage(page)
    login.login()

    dental = DentalPolicyPage(page)

    login.navigate_to_new_quote()

    policy_details = dental.create_dental_policy(mykad=str(data["MyKadID"]),customer_name=data["Name"], date_type="today")


    ExcelWriter.update_dental_details("Dental",str(data["Sno"]),policy_details=policy_details)

    print(f"MyKad : {data['MyKadID']}")
    print(f"Name : {data['Name']}")
    print(f"Quote Number   : {policy_details['Quote Number']}")
    print(f"Policy Number  : {policy_details['Policy Number']}")

    assert True