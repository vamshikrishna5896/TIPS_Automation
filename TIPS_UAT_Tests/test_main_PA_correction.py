import pytest

from TIPS_SIT_pages.login_page_SIT import LoginPage
from TIPS_UAT_Pages.home_page import HomePage
from TIPS_UAT_Pages.PA_correction_page import PACorrectionPage
from TIPS_UAT_Utils.excel_reader import ExcelReader

test_data = ExcelReader.get_test_data("PA_Correction")


@pytest.mark.parametrize("data",[test_data[0]])

def test_pa_correction(page,data):

    login_page = LoginPage(page)
    login_page.login()

    home = HomePage(page)

    correction = PACorrectionPage(page)

    home.navigate_to_correctionandEndo()

    correction.search_policy(str(data["Policy Number"]))

    correction.select_correction_reason(data["MainReason"], data["SubReason"])

    correction.perform_correction(data)

    correction.submit_correction()

    correction.download_schedule()

    print(f"Policy Number : {data['Policy Number']}")

    print("Correction Completed Successfully")