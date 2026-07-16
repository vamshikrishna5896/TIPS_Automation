import pytest
import allure

from TIPS_UAT_Pages.login_page import LoginPage
from TIPS_UAT_Pages.home_page import HomePage
from TIPS_UAT_Pages.CV_RV_policy_page import CVPolicyPage
from TIPS_UAT_Utils.excel_reader import ExcelReader
from TIPS_UAT_Utils.excel_writer import ExcelWriter

test_data = ExcelReader.get_test_data("Motor_CV")

# @allure.epic("Commercial Vehicle")
# @allure.feature("NB Policy")
# @allure.story("Create CV Policy")
# @allure.title("Create Commercial Vehicle Policy")

@pytest.mark.parametrize("data",[test_data[0]])

def test_create_cv_policy(page, data):

    login = LoginPage(page)
    login.login()

    home = HomePage(page)

    cv = CVPolicyPage(page)

    home.navigate_to_new_quote()

    policy_details = cv.create_cv_policy(reg_no=str(data["RegNo"]), business_reg_no=str(data["BusinessRegNo"]),
                        customer_name=data["Name"],approval_type=data["ApprovalType"],
                        carryingcapacity=str(data["carryingcapacity"]), date_type="today")



    # Update Quote Number in Column D
    ExcelWriter.update_motor_cv_rv_details("Motor_CV", str(data["Sno"]),policy_details)

    print(f"Reg No : {data['RegNo']}")
    print(f"Business Reg No : {data['BusinessRegNo']}")
    print(f"Quote Number   : {policy_details['Quote Number']}")
    print(f"Policy Number  : {policy_details['Policy Number']}")

    assert True