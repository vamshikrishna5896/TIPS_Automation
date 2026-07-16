import pytest
import allure

from TIPS_UAT_Pages.login_page import LoginPage
from TIPS_UAT_Pages.home_page import HomePage
from TIPS_UAT_Pages.MC_RV_policy_page import MotorMCPage
from TIPS_UAT_Utils.excel_reader import ExcelReader
from TIPS_UAT_Utils.excel_writer import ExcelWriter

test_data = ExcelReader.get_test_data("Motor_MC")

@pytest.mark.parametrize("data",[test_data[2]])

@allure.epic("MotorCycle Insurance")
@allure.feature("Personal MotorCycle Insurance")
@allure.story("Create RV Policy")
@allure.title("Personal MotorCycle Policy Creation")
def test_create_motor_policy(page,data):

    login = LoginPage(page)
    login.login()

    home = HomePage(page)

    motor = MotorMCPage(page)

    home.navigate_to_new_quote()

    policy_details = motor.create_motor_mc_policy(
        reg_no=str(data["RegNo"]),
        mykad=str(data["MyKadID"]),
        customer_name=data["Name"],
        date_type="today")


    ExcelWriter.update_motor_pc_mc_rv_details("Motor_MC", str(data["Sno"]),policy_details=policy_details)

    print(f"Reg No : {data['RegNo']}")
    print(f"MyKad : {data['MyKadID']}")
    print(f"Quote Number   : {policy_details['Quote Number']}")
    print(f"Policy Number  : {policy_details['Policy Number']}")

    assert True