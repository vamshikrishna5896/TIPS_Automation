import allure

from TIPS_Pages.home_page import HomePage
from TIPS_Pages.PA_endorsement_page import PAEndorsementPage
from TIPS_utils.excel_reader import ExcelReader


# Read data from Sheet2
test_data = ExcelReader.get_test_data("Sheet2")


@allure.epic("PA Insurance")
@allure.feature("Endorsement")
@allure.story("Correct Policyholder Details")
@allure.title("PA Endorsement - Update Tax ID")
def test_pa_endorsement(page):

    # First row from Excel
    data = test_data[0]

    home = HomePage(page)

    endorsement = PAEndorsementPage(page)

    # Navigate to Endorsement
    home.navigate_to_endorsement()

    # Search Policy Number from Excel
    endorsement.search_policy(str(data["policy_no"]))

    # Select Endorsement Type
    endorsement.select_endorsement_type()

    # Update Tax ID from Excel
    endorsement.update_tax_id(str(data["tax_id"]))

    # Submit Endorsement
    endorsement.submit_endorsement()

    # Download Schedule
    endorsement.download_schedule()

    print(
        f"Policy No : {data['policy_no']}")

    print(
        f"Tax ID : {data['tax_id']}")

    print(
        "Endorsement Completed Successfully")

    assert True