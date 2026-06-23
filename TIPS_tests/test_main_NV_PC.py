import pytest
import allure

from TIPS_Pages.home_page import HomePage
from TIPS_Pages.PC_NV_policy_page import MotorPCNVPage
from TIPS_utils.excel_reader import ExcelReader
from TIPS_utils.excel_writer import ExcelWriter

test_data = ExcelReader.get_test_data("Motor_PC_NV")

@pytest.mark.parametrize("data", [test_data[1]])

def test_create_motor_nv_policy(page, data):

    home = HomePage(page)

    motor = MotorPCNVPage(page)

    home.navigate_to_new_quote()

    motor.create_motor_policy(mykad=str(data["MyKadID"]), customer_name=data["Name"], sum_insured=data["SumInsured"])

    quote_number = motor.get_quote_number()

    policy_number = motor.get_policy_number()

    ExcelWriter.update_motor_pc_nv_details("Motor_PC_NV", str(data["MyKadID"]), quote_number, policy_number)
