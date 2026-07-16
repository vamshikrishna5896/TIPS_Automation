import pytest
import allure

from TIPS_UAT_Pages.home_page import HomePage
from TIPS_UAT_Pages.login_page import LoginPage
from TIPS_UAT_Pages.Dental_NB_policy_page import DentalPolicyPage
from TIPS_UAT_Utils.excel_reader import ExcelReader
from TIPS_UAT_Utils.excel_writer import ExcelWriter

test_data = ExcelReader.get_test_data("Dental")

@allure.epic("Dental Insurance")
@allure.feature("Dental Shield")
@allure.story("Create New Policy")
@allure.title("Dental Policy Creation")

@pytest.mark.parametrize("data",[test_data[6]])

def test_create_dental_policy(page,data):


    login = LoginPage(page)
    login.login()

    home = HomePage(page)

    dental = DentalPolicyPage(page)

    home.navigate_to_new_quote()

    policy_details = dental.create_dental_policy(mykad=str(data["MyKadID"]),customer_name=data["Name"], date_type="today")


    ExcelWriter.update_dental_details("Dental",str(data["Sno"]),policy_details=policy_details)

    print(f"MyKad : {data['MyKadID']}")
    print(f"Name : {data['Name']}")
    print(f"Quote Number   : {policy_details['Quote Number']}")
    print(f"Policy Number  : {policy_details['Policy Number']}")

    assert True