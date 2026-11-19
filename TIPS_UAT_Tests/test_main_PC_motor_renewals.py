
import pytest

from TIPS_UAT_Pages.login_page import LoginPage
from TIPS_UAT_Pages.PC_motor_renewals_page import MotorRenewalPage
from TIPS_UAT_Utils.excel_reader import ExcelReader


test_data = ExcelReader.get_test_data("PC_Motor_Renewal")


@pytest.mark.parametrize("data", [test_data[0]])
def test_motor_renewal(page, data):

    # Step 1: Login
    login = LoginPage(page)
    login.login()

    # Step 2: Initialize renewal page
    renewal = MotorRenewalPage(page)

    # Step 3: Search using policy number from Excel
    renewal.search_policy(str(data["Policy Number"]))

    # Step 4: Open the renewal record
    renewal.open_policy_for_renewal()

    # Step 5: Confirm the policy
    renewal.confirm_renewal_policy()

    # Step 6: Process optional changes

    renewal.process_optional_change(data[0])


    renewal.click_save_to_proceed()
    renewal.click_save_and_next()


