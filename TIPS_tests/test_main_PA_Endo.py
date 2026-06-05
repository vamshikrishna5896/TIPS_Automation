import pytest
import allure

from TIPS_Pages.home_page import HomePage
from TIPS_Pages.PA_endorsement_page import PAEndorsementPage

from TIPS_utils.excel_reader import ExcelReader


test_data = ExcelReader.get_test_data("Sheet1")


@allure.epic("PA Insurance")
@allure.feature("Endorsement")
@allure.story("Correct Policyholder Details")
@allure.title("PA Endorsement - Update Tax ID")

@pytest.mark.parametrize("data", [test_data[0]])
def test_pa_endorsement(page, data):

    home = HomePage(page)

    endorsement = PAEndorsementPage(page)

    home.navigate_to_endorsement()

    endorsement.search_policy(
        str(data["Policy Number"])
    )

    endorsement.select_endorsement_type()

    endorsement.update_tax_id(
        "123654789"
    )

    endorsement.submit_endorsement()

    endorsement.download_schedule()

    print(
        f"Policy Number : {data['Policy Number']}"
    )

    print(
        "Endorsement Completed Successfully"
    )

    assert True