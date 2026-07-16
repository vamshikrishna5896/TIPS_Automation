from TIPS_SIT_pages.login_page_SIT import LoginPageSIT
from TIPS_SIT_pages.DMS_page import DMS

def test_dms_page(page):
    try:
        login = LoginPageSIT(page)
        username = login.login()

        dms = DMS(page)
        dms.navigate_to_dms()
        print("\n Document Management System page is displayed successfully")

        dms.quote()

        #dms.policy()


    finally:
        page.locator("a").filter(has_text=username).click()
        page.get_by_text("Sign Out").click(timeout=5000)
        print("Logout Successful")


