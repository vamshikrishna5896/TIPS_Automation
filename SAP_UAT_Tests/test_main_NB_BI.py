import pytest
import allure

from SAP_UAT_Pages import policy_titles
from SAP_UAT_Pages.login_page import LoginPage
from SAP_UAT_Pages.home_page_sap import HomePageSAP
from SAP_UAT_Pages.BP_page import BPPage
from SAP_UAT_Pages.commission_page import CommissionPage
from SAP_UAT_Pages.BI_Products.All_risk_page import AllRiskPage
from SAP_UAT_Pages.Release_page import ReleasePage
from SAP_UAT_Utils.excel_reader import ExcelReader
from SAP_UAT_Utils.excel_writer import ExcelWriter

test_data = ExcelReader.get_test_data("BI")

@pytest.mark.parametrize("data", [test_data[2]])
def test_create_sap_new_business(page, data):

    login = LoginPage(page)

    home = HomePageSAP(page)

    new_business_page = None

    try:

        # ------ Login -----------#
        login.login()

        # ----- Open Policy Management -------------#
        home.go_to_policy_management()

        # ------------------------------------------------
        # Open New Business
        # ------------------------------------------------
        new_business_page = home.open_new_business()

        # ------------------------------------------------
        # Create New Application
        # ------------------------------------------------
        home.start_new_application_bi(new_business_page, sales_product="Business Insurance", date_type="today")

        #Policy Titles

        header = policy_titles.HeaderPage(new_business_page)

        header.select_policy_title(data["PolicyTitle"])

        # ------------------------------------------------
        # Business Partner
        # ------------------------------------------------
        bp_page = BPPage(new_business_page)

        bp_page.fill_business_partner(business_partner=str(data["BusinessPartner"]))

        # ------------------------------------------------
        # Commission
        # ------------------------------------------------
        commission_page = CommissionPage(new_business_page)

        commission_page.fill_commission(commission_contract=str(data["CommissionContract"]))

        # ------------------------------------------------
        # Risk
        # ------------------------------------------------
        risk_page = AllRiskPage(new_business_page)
        risk_page.fill_nature_and_address(nature_of_risk=data["NatureOfRisk"], state=data["State"], city_hint=data["PostcodeCityHint"],)
        # risk_page.fill_machinery_coverage_and_premium(coverage_item="Machinery and Equipment")
        # risk_page.fill_machinery_limit_amount("25000")
        risk_page.fill_office_equipment(coverage_item="Office Equipment")
        risk_page.fill_office_equipment_limit_amount_(limit_amount="10000")

        # ------------------------------------------------
        # Release
        # ------------------------------------------------
        release_page = ReleasePage(new_business_page)
        policy_data = release_page.release_application()
        print(policy_data)

        # ------------------------------------------------
        # Update Excel
        # ------------------------------------------------
        policy_details = {
            "Effective Date": policy_data["Effective Date"],
            "Policy Holder": policy_data["Policy Holder"],
            "Policy Number": policy_data["Policy Number"],
            "Application Number": policy_data["Application Number"]}

        ExcelWriter.update_sap_nb_details("BI", str(data["Sno"]), policy_details)

        print(f"Business Partner : {data['BusinessPartner']}")
        print(f"Commission Contract : {data['CommissionContract']}")


    finally:

        if new_business_page:
            home.logout(new_business_page)

        print("\n========== Cleanup Completed ==========\n")