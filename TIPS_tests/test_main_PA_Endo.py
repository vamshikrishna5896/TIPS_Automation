import pytest

from TIPS_Pages.home_page import HomePage
from TIPS_Pages.PA_endorsement_page import PAEndorsementPage

from TIPS_utils.excel_reader import ExcelReader


test_data = ExcelReader.get_test_data("PA_Endo")


@pytest.mark.parametrize("data", [test_data[0]])
def test_pa_endorsement(page, data):

    home = HomePage(page)

    endorsement = PAEndorsementPage(page)

    home.navigate_to_correctionandEndo()

    endorsement.search_policy(str(data["Policy Number"]))

    endorsement.select_endorsement_reason(data["MainReason"], data["SubReason"])

    endorsement.update_occupation()

    endorsement.generate_endorsement_form()

    endorsement.upload_file()

    endorsement.submit_endorsement()

    print(f"Policy Number : {data['Policy Number']}")