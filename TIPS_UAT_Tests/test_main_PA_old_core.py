import pytest
import allure

from TIPS_UAT_Pages.login_page import LoginPage
from TIPS_UAT_Pages.home_page import HomePage
from TIPS_UAT_Pages.PA_old_core_renewals_page import RenewalPage

# @allure.epic("Insurance Renewal")
# @allure.feature("Personal Accident and Travel Renewal")
# @allure.story("Inspect Renewal Search Form")
# @allure.title("Open PA Travel Renewal Search Form")
def test_inspect_pa_travel_renewal(page):

   # --------Login page --------#
    login = LoginPage(page)
    login.login()

    # ---------------- Initialize Renewal Page ----------------
    renewal = RenewalPage(page)

    # ---------------- QMS tile ------------------#
    renewal.open_qms()

    # ---------------- Open Renewal Module ----------------#
    renewal.open_renewal()

    # ---------------- Select PA / Travel Category ----------------#
    renewal.select_pa_travel_category()

    # ---------------- Inspect Search Fields ----------------#
    renewal.inspect_search_form()

    # ---------------- Test Completed ----------------#
    assert page.url.endswith("/qms/newrenewal/list")