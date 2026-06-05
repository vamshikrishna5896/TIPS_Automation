import pytest
import allure

from TIPS_Pages.home_page import HomePage
from TIPS_Pages.PA_NB_policy_page import Policycreation

from TIPS_utils.excel_reader import ExcelReader
from TIPS_utils.excel_writer import ExcelWriter


test_data = ExcelReader.get_test_data("Sheet1")


@allure.epic("PA Insurance")
@allure.feature("Personal Accident Quote")
@allure.story("Create New Quote")
@allure.title("Create Personal Accident Quote")

@pytest.mark.parametrize("data", [test_data[0]])
def test_create_quote(page, data):

    home = HomePage(page)

    quote = Policycreation(page)

    home.navigate_to_new_quote()

    quote.create_personal_accident_quote(mykad=str(data["MyKadID"]),customer_name=data["Name"],date_type="today")

    # Get Policy Number
    policy_number = quote.get_policy_number()

    # Update Excel
    ExcelWriter.update_policy_number("Sheet1",str(data["MyKadID"]),policy_number)

    print(f"MyKad : {data['MyKadID']}")
    print(f"Name : {data['Name']}")
    print(f"Policy Number : {policy_number}")

    assert True