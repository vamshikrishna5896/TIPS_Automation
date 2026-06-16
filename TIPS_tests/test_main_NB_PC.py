import pytest
import allure

from TIPS_Pages.home_page import HomePage
from TIPS_Pages.PC_NB_policy_page import MotorPCPage
from TIPS_utils.excel_reader import ExcelReader
from TIPS_utils.excel_writer import ExcelWriter

test_data = ExcelReader.get_test_data("Motor_PC")

# @allure.epic("Motor Insurance")
# @allure.feature("Private Car")
# @allure.story("NB Policy")
# @allure.title("Motor PC Policy Creation")

@pytest.mark.parametrize("data",[test_data[0]])

def test_create_motor_policy(page,data):

    home = HomePage(page)

    motor = MotorPCPage(page)

    home.navigate_to_new_quote()

    motor.create_motor_policy(reg_no=str(data["RegNo"]),mykad=str(data["MyKadID"]),customer_name=data["Name"],date_type="today")

    policy_number = motor.get_policy_number()

    ExcelWriter.update_policy_number("Motor_PC",str(data["MyKadID"]),policy_number)

    print(f"Reg No : {data['RegNo']}")
    print(f"MyKad : {data['MyKadID']}")
    print(f"Policy Number : {policy_number}")

    assert True