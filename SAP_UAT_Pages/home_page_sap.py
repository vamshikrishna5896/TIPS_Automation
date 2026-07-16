import re

from SAP_UAT_Pages.date_picker import DatePicker


class HomePageSAP:

    def __init__(self, page):
        self.page = page

    # ---- Step 1: open the Policy Management menu ----
    def go_to_policy_management(self):
        self.page.get_by_label("Group Navigation").get_by_text("POLICY-MANAGEMENT").click()

    # ---- Step 2: click "New Business" -> this opens a NEW TAB ----
    def open_new_business(self):

        with self.page.expect_popup() as popup_info:
            self.page.get_by_role("link", name="New Business").click()

        new_business_page = popup_info.value
        return new_business_page

    # ---- Step 3: fill the header + Sales Product Template, then create ----
    def start_new_application(self, new_business_page, sales_product="Business Insurance", date_type="today"):

        frame = new_business_page.locator("iframe[title='Application']").content_frame

        # ---- Date field 1 ----
        frame.locator("#ls-inputfieldhelpbutton").click()
        DatePicker.select_date(frame, date_type)

        # ---- Date field 2: Submission To PP Date ----
        frame.get_by_role("textbox", name="Submission To PP Date Required").click()
        frame.locator("#ls-inputfieldhelpbutton").click()
        DatePicker.select_date(frame, date_type)

        # ---- Date field 3: Received Date ----
        frame.get_by_role("textbox", name="Received Date Required").click()
        frame.locator("#ls-inputfieldhelpbutton").click()
        DatePicker.select_date(frame, date_type)

        # ---- Sales Product Template (e.g. "Business Insurance") ----
        frame.get_by_role("textbox", name="Sales Prod.Templ.ID Required").click()
        frame.locator("#ls-inputfieldhelpbutton").click()
        frame.get_by_text(sales_product).click()

        # ---- Confirm and start the new application ----
        frame.get_by_role("button", name="Copy").click()
        frame.get_by_role("button", name="Create  Emphasized").click()

        print(f"New application started. Sales Product Template: {sales_product}")

    # ---- Step 4 (last step of the test, or the cleanup step on error): logout ----
    def logout(self, new_business_page):
        try:

            if new_business_page.is_closed():
                print("New Business tab is already closed - nothing to log out of")
                return

            profile_button = new_business_page.get_by_role("button", name=re.compile("^Profile of"))
            profile_button.wait_for(state="visible", timeout=10_000)
            profile_button.click()

            new_business_page.get_by_text("Sign Out").click(timeout=10_000)
            new_business_page.get_by_role("button", name="OK").click(timeout=10_000)

            print("Logged out of SAP")

        except Exception as e:
            print(f"Error occurred while trying to logout of SAP: {e}")