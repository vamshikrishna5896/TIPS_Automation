import pytest
import allure

from SAP_UAT_Pages.login_page import LoginPage
from SAP_UAT_Pages.home_page_sap import HomePageSAP
from SAP_UAT_Pages.BP_page import BPPage
from SAP_UAT_Pages.commission_page import CommissionPage
from SAP_UAT_Pages.Products.All_risk_page import AllRiskPage
from SAP_UAT_Pages.Release_page import ReleasePage
from SAP_UAT_Utils.excel_reader import ExcelReader
from SAP_UAT_Utils.excel_writer import ExcelWriter

# Create a sheet called "NB_BI" in your test_data.xlsx with columns:
# Sno | BusinessPartner | CommissionContract | NatureOfRisk |
# State | PostcodeCityHint | Street
test_data = ExcelReader.get_test_data("BI")


@pytest.mark.parametrize("data", [test_data[0]])

# @allure.epic("SAP Policy Management")
# @allure.feature("New Business")
# @allure.story("Create New Business - Business Insurance")
# @allure.title("SAP New Business Policy Creation")

def test_create_sap_new_business(page, data):

    # ---- Step 1: Login and open Policy Management on the main SAP tab ----

    login = LoginPage(page)
    login.login()

    home = HomePageSAP(page)
    home.go_to_policy_management()


    # ---- Step 2: "New Business" opens a NEW TAB - capture it ----
    new_business_page = home.open_new_business()

    # ---- Step 3: Fill header dates + Sales Product Template, then Create ----
    home.start_new_application(new_business_page, sales_product="Business Insurance", date_type="today")

    # ---- Step 4: Policy Title + Business Partner ----
    bp_page = BPPage(new_business_page)
    bp_page.fill_policy_and_business_partner(business_partner=str(data["BusinessPartner"]))

    # ---- Step 5: Commission ----
    commission_page = CommissionPage(new_business_page)
    commission_page.fill_commission(commission_contract=str(data["CommissionContract"]))

    # ---- Step 6: Risk, address, coverage, premium type, limit amount ----
    risk_page = AllRiskPage(new_business_page)

    risk_page.fill_nature_and_address(
        nature_of_risk=data["NatureOfRisk"],
        state=data["State"],
        city_hint=data["PostcodeCityHint"],
    )

    risk_page.fill_coverage_and_premium(coverage_item="Machinery and Equipment", premium_type="OneTime Premium",)

    risk_page.fill_limit_amount(limit_amount="25000")



    # ---- Step 7: Check, Calculate, Release ----
    release_page = ReleasePage(new_business_page)
    release_page.release_application()

    # ---- Step 8: Save results back to Excel ----
    policy_details = {"Business Partner": data["BusinessPartner"], "Commission Contract": data["CommissionContract"], "Nature of Risk": data["NatureOfRisk"], "State": data["State"], "Limit Amount": "25000",}
    ExcelWriter.update_sap_nb_details("BI", str(data["Sno"]), policy_details=policy_details)

    print(f"Business Partner : {data['BusinessPartner']}")
    print(f"Commission Contract : {data['CommissionContract']}")

    # ---- Step 9: Logout (on the popup tab) ----
    home.logout(new_business_page)

    assert True