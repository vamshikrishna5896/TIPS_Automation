import pytest
import allure
from TIPS_Pages.home_page import HomePage
from TIPS_utils.excel_reader import ExcelReader
from TIPS_Pages.policy_creation import Policycreation

test_data = ExcelReader.get_test_data()

# @allure.epic("PA Insurance")
# @allure.feature("Personal Accident Quote")
# @allure.story("Create New Quote")
# @allure.title("Create Personal Accident Quote")
def test_create_quote(page):

    data = test_data[0]

    home = HomePage(page)

    quote = Policycreation(page)

    home.navigate_to_new_quote()

    quote.create_personal_accident_quote(
        mykad=data["mykad"],
        customer_name=data["name"],
        date_type="today"
    )

    print(f"MyKad : {data['mykad']}")
    print(f"Name : {data['name']}")

    assert True