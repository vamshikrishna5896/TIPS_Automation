import pytest
import allure

from SAP_UAT_Pages import policy_titles
from SAP_UAT_Pages.login_page import LoginPage
from SAP_UAT_Pages.home_page_sap import HomePageSAP
from SAP_UAT_Pages.BP_page import BPPage
from SAP_UAT_Pages.commission_page import CommissionPage
from SAP_UAT_Pages.PA_products.NB_PA_page import PersonalAccident
from SAP_UAT_Pages.Release_page import ReleasePage
from SAP_UAT_Utils.excel_reader import ExcelReader
from SAP_UAT_Utils.excel_writer import ExcelWriter

test_data = ExcelReader.get_test_data("PA")

@pytest.mark.parametrize("data", [test_data[0]])
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
        home.start_new_application_pa(new_business_page, sales_product="Personal Accident, Travel & Health", date_type="today")

        #Policy Titles

        header = policy_titles.HeaderPage(new_business_page)

        header.select_pa_policy_title(data["PolicyTitle"])

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
        # Risk Class
        # ------------------------------------------------
        risk_page = PersonalAccident(new_business_page)
        # risk_page.fill_plan_details(risk_class=data["RiskClass"], plan=data["Plan"])
        risk_page.fill_plan_details(risk_class=data["RiskClass"])


        #------------------------------------------------
        # Coverage_details
        #-------------------------------------------------
        coverage_page = PersonalAccident(new_business_page)
        coverage_page.adpd_coverage_details()

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

        ExcelWriter.update_sap_nb_details("PA", str(data["Sno"]), policy_details)

        print(f"Business Partner : {data['BusinessPartner']}")
        print(f"Commission Contract : {data['CommissionContract']}")


    finally:

        if new_business_page:
            home.logout(new_business_page)

        print("\n========== Cleanup Completed ==========\n")