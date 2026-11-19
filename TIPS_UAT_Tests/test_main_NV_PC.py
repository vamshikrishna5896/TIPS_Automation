import pytest
import allure

from TIPS_UAT_Pages.login_page import LoginPage
from TIPS_UAT_Pages.home_page import HomePage
from TIPS_UAT_Pages.PC_NV_policy_page import MotorPCNVPage
from TIPS_UAT_Utils.excel_reader import ExcelReader
from TIPS_UAT_Utils.excel_writer import ExcelWriter

test_data = ExcelReader.get_test_data("Motor_PC_NV")

@pytest.mark.parametrize("data", [test_data[10]])

def test_create_motor_nv_policy(page, data):

    login_page = LoginPage(page)
    login_page.login()

    home = HomePage(page)

    motor = MotorPCNVPage(page)

    home.navigate_to_new_quote()

    policy_details = motor.create_motor_policy(mykad=str(data["MyKadID"]), customer_name=data["Name"],
                              sum_insured=data["SumInsured"])

    ExcelWriter.update_motor_pc_mc_nv_details("Motor_PC_NV", str(data["Sno"]), policy_details)


