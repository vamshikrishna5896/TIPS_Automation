import pytest
import allure

from TIPS_Pages.home_page import HomePage
from TIPS_Pages.Dental_NB_policy_page import DentalPolicyPage
from TIPS_utils.excel_reader import ExcelReader
from TIPS_utils.excel_writer import ExcelWriter


test_data = ExcelReader.get_test_data("Sheet2")


# @allure.epic("Dental Insurance")
# @allure.feature("Dental Shield")
# @allure.story("Create New Policy")
# @allure.title("Dental Policy Creation")

@pytest.mark.parametrize("data",[test_data[0]])

def test_create_dental_policy(page,data):

    home = HomePage(page)

    dental = DentalPolicyPage(page)

    home.navigate_to_new_quote()

    dental.create_dental_policy(mykad=str(data["MyKadID"]),customer_name=data["Name"])

    policy_number = dental.get_policy_number()

    ExcelWriter.update_policy_number("Sheet2",str(data["MyKadID"]),policy_number)

    print(f"MyKad : {data['MyKadID']}")

    print(f"Name : {data['Name']}")

    print(f"Policy Number : {policy_number}")

    assert True