import re
from datetime import datetime

today = datetime.now().strftime("%d.%m.%Y")

#date = "25.11.2025"
date = today

class HomePageSAP:

    def __init__(self, page):
        self.page = page

    def go_home(self):
        self.page.get_by_role("link", name="Home").click()

    def go_to_policy_management(self):
        self.page.get_by_label("Group Navigation").get_by_text("POLICY-MANAGEMENT").click()

    def open_new_business(self):

        with self.page.expect_popup() as popup_info:
            self.page.get_by_role("link", name="New Business").click()

        new_business_page = popup_info.value
        new_business_page.on("dialog", lambda dialog: dialog.accept())

        return new_business_page

    # =====================================================
    # Common Date Selection
    # =====================================================
    def fill_dates(self, frame, date_type=None):

        # Policy Start
        frame.get_by_role("textbox" , name="Policy Start Required").fill(date)
        self.page.wait_for_timeout(1000)

        # Submission To PP Date
        frame.get_by_role("textbox", name="Submission To PP Date Required").fill(date)
        self.page.wait_for_timeout(1000)

        # Received Date
        frame.get_by_role("textbox", name="Received Date Required").fill(date)
        self.page.wait_for_timeout(1000)

    # =====================================================
    # Common Product Selection (works even if product is below)
    # =====================================================
    def select_sales_product(self, page, frame, sales_product):

        product_field = frame.get_by_role("textbox", name="Sales Prod.Templ.ID Required")

        product_field.click()
        frame.locator("#ls-inputfieldhelpbutton").click()

        for _ in range(12):

            product = frame.get_by_text(sales_product, exact=True)

            if product.count() > 0:
                try:
                    if product.first.is_visible():
                        product.first.click()
                        frame.get_by_role("button", name="Copy").click()
                        print(f"Selected Product : {sales_product}")
                        return
                except:
                    pass

            # Scroll popup down
            page.mouse.wheel(0, 350)
            page.wait_for_timeout(300)

        raise Exception(f"Sales Product '{sales_product}' not found.")

    # =====================================================
    # Motor car
    # =====================================================
    def start_new_application_pc(
            self,
            new_business_page,
            sales_product="Motorcar",
            date_type=None,
            acquisition_type="New Business"):

        frame = new_business_page.locator("iframe[title='Application']").content_frame
        self.fill_dates(frame, date_type)
        self.select_sales_product(new_business_page, frame, sales_product)
        frame.get_by_role("button", name="Copy").wait_for(state="hidden")
        # Press Enter on the page
        new_business_page.keyboard.press("Enter")


        if acquisition_type is not None:
            frame.get_by_role("textbox", name="Acquisition Type Required").click()
            frame.get_by_role("option", name=acquisition_type).click()
        frame.get_by_role("button", name="Create  Emphasized").click()
        print(f"New application started. Sales Product Template: {sales_product}")

    # =====================================================
    # Motor Motorcycle
    # =====================================================
    def start_new_application_mc(
            self,
            new_business_page,
            sales_product="Motorcycle",
            date_type=None,
            acquisition_type="New Business"):

        frame = new_business_page.locator("iframe[title='Application']").content_frame
        self.fill_dates(frame, date_type)
        self.select_sales_product(new_business_page, frame, sales_product)
        frame.get_by_role("button", name="Copy").wait_for(state="hidden")
        # Press Enter on the page
        new_business_page.keyboard.press("Enter")


        if acquisition_type is not None:
            frame.get_by_role("textbox", name="Acquisition Type Required").click()
            frame.get_by_role("option", name=acquisition_type).click()
        frame.get_by_role("button", name="Create  Emphasized").click()
        print(f"New application started. Sales Product Template: {sales_product}")

    # =====================================================
    # Business Insurance
    # =====================================================
    def start_new_application_bi(self,
            new_business_page,
            sales_product="Business Insurance",
            date_type=None,
            acquisition_type=None):

        frame = new_business_page.locator("iframe[title='Application']").content_frame

        self.fill_dates(frame, date_type)

        self.select_sales_product(new_business_page, frame, sales_product)

        if acquisition_type is not None:
            frame.get_by_role("textbox", name="Acquisition Type Required").click()
            frame.get_by_role("option", name=acquisition_type).click()
        frame.get_by_role("button", name="Create  Emphasized").click()
        print(f"New application started. Sales Product Template: {sales_product}")

    # =====================================================
    # Personal Accident
    # =====================================================
    def start_new_application_pa(self,
            new_business_page,
            sales_product="Personal Accident, Travel & Health",
            date_type=None,
            acquisition_type=None):

        frame = new_business_page.locator("iframe[title='Application']").content_frame

        self.fill_dates(frame, date_type)

        self.select_sales_product(new_business_page, frame, sales_product)

        if acquisition_type is not None:
            frame.get_by_role("textbox", name="Acquisition Type Required").click()
            frame.get_by_role("option", name=acquisition_type).click()
        frame.get_by_role("button", name="Create  Emphasized").click()
        print(f"New application started. Sales Product Template: {sales_product}")

    # =====================================================
    # Logout
    # =====================================================
    def logout(self, new_business_page):

        try:

            if new_business_page.is_closed():
                print("New Business tab is already closed")
                return

            profile_button = new_business_page.get_by_role("button", name=re.compile("^Profile of"))

            profile_button.wait_for(state="visible", timeout=10000)
            profile_button.click()

            new_business_page.get_by_text("Sign Out").click(timeout=10000)
            new_business_page.get_by_role("button", name="OK").click(timeout=10000)

            print("Logged out of SAP")

        except Exception as e:
            print(f"Error occurred while trying to logout of SAP: {e}")