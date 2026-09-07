import pytest
import allure

from SAP_UAT_Pages.login_page import LoginPage
from SAP_UAT_Pages.home_page_sap import HomePageSAP
from SAP_UAT_Pages.BP_page import BPPage
from SAP_UAT_Pages.commission_page import CommissionPage
from SAP_UAT_Pages.Motor_products.NB_PC_page import MotorcarPage
from SAP_UAT_Pages.Release_page import ReleasePage
from SAP_UAT_Utils.excel_reader import ExcelReader
from SAP_UAT_Utils.excel_writer import ExcelWriter


test_data = ExcelReader.get_test_data("Motor_PC")


@pytest.mark.parametrize("data", [test_data[2]])

# @allure.epic("SAP Policy Management")
# @allure.feature("New Business")
# @allure.story("Create New Business - Motorcar")
# @allure.title("SAP New Business Policy Creation - Motorcar")

def test_create_sap_motorcar_business(page, data):

    login = LoginPage(page)

    home = HomePageSAP(page)

    new_business_page = None

    try:
        # ---- Step 1: Login, then this flow needs a "Home" click first ----
        login.login()
        home.go_home()
        home.go_to_policy_management()

        # ---- Step 2: "New Business" opens a NEW TAB - capture it ----
        new_business_page = home.open_new_business()

        # ---- Step 3: Header dates + Product Template + Acquisition Type ----
        home.start_new_application_pc(new_business_page, sales_product="Motorcar", date_type="15.08.2025", acquisition_type="New Business",)

        # ---- Step 4: Policy Title + Business Partner ----
        bp_page = BPPage(new_business_page)
        bp_page.fill_business_partner(business_partner=str(data["BusinessPartner"]))

        # ---- Step 5: Commission ----
        commission_page = CommissionPage(new_business_page)
        commission_page.fill_commission(commission_contract=str(data["CommissionContract"]))

        # ---- Step 6: Risk item, vehicle registration + details, coverage, clause ----
        motor_page = MotorcarPage(new_business_page)
        motor_page.open_risk_item()
        motor_page.register_vehicle(vehicle_reg_no=data["VehicleRegNo"])

        motor_page.fill_vehicle_details(
            safety_features=data["SafetyFeatures"],
            unit_type=data["UnitType"],
            garaged=data["Garaged"],
            anti_theft=data["AntiTheft"],)

        motor_page.rebate_percentage()

        motor_page.select_coverage(coverage_name="Comprehensive")

        motor_page.add_clause(clause_type="Named Driver", clause_name=data["ClauseName"])

        # ------------------------------------------------
        # Release
        # ------------------------------------------------
        release_page = ReleasePage(new_business_page)
        policy_data = release_page.release_application()
        print(policy_data)

        # ---- Step 8: Save results back to Excel ----
        policy_details = {
            "Business Partner": data["BusinessPartner"],
            "Commission Contract": data["CommissionContract"],
            "Vehicle Reg No": data["VehicleRegNo"],

            "Policy Number": policy_data["Policy Number"],
            "Policy Holder": policy_data["Policy Holder"],
            "Application Number": policy_data["Application Number"],
            "Effective Date": policy_data["Effective Date"],

            # "premium_before_tax": policy_data["premium_before_tax"],
            # "Cum.Tax/Submissn Amt": policy_data["Cum.Tax/Submissn Amt"],
            # "Premium After Tax": policy_data["Premium After Tax"],
            # "Stamp Duty": policy_data["Stamp Duty"],
            # "Basic Premium": policy_data["Basic Premium"],
        }

        # Add the values returned from ReleasePage
        policy_details.update(policy_data)

        ExcelWriter.update_sap_nb_pc_details("Motor_PC", str(data["Sno"]), policy_details)

        print(f"Business Partner : {data['BusinessPartner']}")
        print(f"Vehicle Reg No : {data['VehicleRegNo']}")

        # ---- Step 9: Normal logout, everything went fine ----
        home.logout(new_business_page)

    except Exception as error:
        print(f"Test failed - cleaning up session before re-raising: {error}")

        if new_business_page is not None:
            home.logout(new_business_page)

        raise

    assert True