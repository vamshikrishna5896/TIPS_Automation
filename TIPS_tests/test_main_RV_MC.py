import pytest
import allure

from TIPS_Pages.home_page import HomePage
from TIPS_Pages.MC_RV_policy_page import MotorMCPage
from TIPS_utils.excel_reader import ExcelReader
from TIPS_utils.excel_writer import ExcelWriter

test_data = ExcelReader.get_test_data("Motor_MC")

# @allure.epic("Motor Insurance")
# @allure.feature("Private Car")
# @allure.story("NB Policy")
# @allure.title("Motor PC Policy Creation")

@pytest.mark.parametrize("data",[test_data[2]])

def test_create_motor_policy(page,data):

    home = HomePage(page)

    motor = MotorMCPage(page)

    home.navigate_to_new_quote()

    motor.create_motor_mc_policy(
        reg_no=str(data["RegNo"]),
        mykad=str(data["MyKadID"]),
        customer_name=data["Name"],
        coverage_type=data["Coverage Type"],
        date_type="today")

    # Get Quote Number
    quote_number = motor.get_quote_number()

    # get Policy Number
    policy_number = motor.get_policy_number()

    # Update Quote Number & policy Number Column E & F
    ExcelWriter.update_motor_mc_rv_policy_number("Motor_MC", str(data["RegNo"]), quote_number, policy_number)

    print(f"Reg No : {data['RegNo']}")
    print(f"MyKad : {data['MyKadID']}")
    print(f"Quote Number : {quote_number}")
    print(f"Policy Number : {policy_number}")

    assert True