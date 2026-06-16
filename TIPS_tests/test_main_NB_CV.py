import pytest
import allure

from TIPS_Pages.home_page import HomePage
from TIPS_Pages.CV_NB_policy_page import CVPolicyPage
from TIPS_utils.excel_reader import ExcelReader
from TIPS_utils.excel_writer import ExcelWriter



test_data = ExcelReader.get_test_data("Motor_CV")


# @allure.epic("Commercial Vehicle")
# @allure.feature("NB Policy")
# @allure.story("Create CV Policy")
# @allure.title("Create Commercial Vehicle Policy")

@pytest.mark.parametrize("data",[test_data[0]])

def test_create_cv_policy(page, data):

    home = HomePage(page)

    cv = CVPolicyPage(page)

    home.navigate_to_new_quote()

    cv.create_cv_policy(reg_no=str(data["RegNo"]), business_reg_no=str(data["BusinessRegNo"]),
                        customer_name=data["Name"],approval_type=data["ApprovalType"],
                        carryingcapacity=str(data["carryingcapacity"]), date_type="today")

    policy_number = cv.get_policy_number()

    ExcelWriter.update_policy_number("Motor_CV", str(data["RegNo"]), policy_number)

    print(f"Reg No : {data['RegNo']}")
    print(f"Policy Number : {policy_number}")

    assert True