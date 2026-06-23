import pytest
import allure

from TIPS_Pages.home_page import HomePage
from TIPS_Pages.PC_RV_policy_page import MotorPCPage
from TIPS_utils.excel_reader import ExcelReader
from TIPS_utils.excel_writer import ExcelWriter

test_data = ExcelReader.get_test_data("Motor_PC")

@pytest.mark.parametrize("data",[test_data[3]])

def test_create_motor_policy(page, data):

    home = HomePage(page)

    motor = MotorPCPage(page)

    home.navigate_to_new_quote()

    motor.create_motor_policy(reg_no=str(data["RegNo"]), mykad=str(data["MyKadID"]),
        customer_name=data["Name"], coverage_type=data["Coverage Type"], date_type="today")

    # Get Quote Number
    quote_number = motor.get_quote_number()

    # Get Policy Number
    policy_number = motor.get_policy_number()

    # Update Quote Number in Column D
    ExcelWriter.update_motor_pc_rv_quote_number("Motor_PC", str(data["RegNo"]), quote_number,policy_number)

    print(f"Reg No : {data['RegNo']}")
    print(f"MyKad : {data['MyKadID']}")
    print(f"Quote Number : {quote_number}")
    print(f"Policy Number : {policy_number}")

    assert True