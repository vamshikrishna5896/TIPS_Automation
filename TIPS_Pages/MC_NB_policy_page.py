import allure
from datetime import datetime
from TIPS_utils.date_picker import DatePicker

class MotorMCPage:

    def __init__(self,page):
        self.page = page

   #@allure.step("Create Motor Policy")
    def create_motor_policy(self,reg_no,mykad,customer_name, date_type):

        # Motor Product
        self.page.get_by_role("heading",name="Motor").click()

        self.page.get_by_role("button",name="Next").click()

        # Vehicle Number
        self.page.get_by_role("textbox").fill(reg_no)

        # State
        self.page.locator(".mat-select-placeholder").click()

        self.page.get_by_role("option",name="Kedah").click()

        # Click on vehicle search button
        self.page.get_by_role("button",name="search Vehicle Search").click()

        self.page.wait_for_timeout(1000)
        try:
            self.page.get_by_role("button",name="Save Vehicle Info").click()
        except:
            print("Save Vehicle Info button not found")

        # ------Inception Date Calendar---------#
        self.page.locator("mat-form-field").filter(has_text="Inception Date").get_by_label("Open calendar").click()
        self.page.wait_for_timeout(1000)
        # Select Date
        DatePicker.select_date(self.page, date_type)

        #--------------- MyKad ------------#
        self.page.locator("mat-form-field").filter(has_text="ID #").locator("#id").fill(mykad)

        # Name
        self.page.locator("mat-form-field").filter(has_text="Name as per ID").locator("#legalName").fill(customer_name)

        self.page.get_by_role("button", name="search Validate Owner as per").click()

        self.page.wait_for_timeout(3000)

        self.page.get_by_role("button", name="Save & Next").click()

        self.page.wait_for_timeout(5000)

        # Proposer Details
        self.page.locator(".mat-select-placeholder").first.click()

        self.page.locator(".item").first.click()

        #-----yes or edit button----#
        # ---- CHECK IF YES BUTTON EXISTS AND IS ENABLED ----
        yes_button = self.page.get_by_role("button", name="Yes").first

        if yes_button.is_visible():
            yes_button.click()
            self.page.wait_for_timeout(1000)

        # ---- CHECK IF ADDRESS ALREADY EXISTS ----#
        # add_button = self.page.locator("button[name='Add'], button:has-text('Add')").first
        # if add_button.is_visible():
        #     add_button.click()
        #     self.page.wait_for_timeout(1000)

            # ---- STATE ---- (runs for both cases)
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.get_by_role("option", name="Johor").click()
        self.page.wait_for_timeout(5000)

            # ---- PINCODE ----
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.get_by_role("option", name="81100").click()
        self.page.wait_for_timeout(2000)

            # ---- STREET ADDRESS ----
        self.page.get_by_role("combobox", name="Address Line").click()
        self.page.get_by_role("option", name="Taman Desa Harmoni", exact=True).click()
        self.page.wait_for_timeout(2000)

            # ---- SAVE BUTTON (if address is added) ----
        address_save = self.page.locator("button#save")
        if address_save.is_visible():
                address_save.click()
                self.page.wait_for_timeout(6000)

        # ---- DECLARATION STATEMENTS ----#
        self.page.get_by_text("We respect your privacy and").click()

        self.page.get_by_text("I hereby confirm that I have").click()

        self.page.get_by_role("button", name="Generate Quote").click()

        self.page.wait_for_timeout(3000)

        # try:
        self.page.get_by_role("button", name="Submit").click()
        # except:
        #     pass

        self.page.wait_for_timeout(5000)

        #------proceed to policy Issue button------#
        self.page.get_by_role("button", name="Proceed to Policy Issuance").click()
        self.page.wait_for_timeout(5000)

        #------Issue policy button----#
        self.page.get_by_role("button", name="Issue Policy").click()
        self.page.wait_for_timeout(18000)

        #------Download & e-mail Policy button----#
        self.page.get_by_role("button", name="Download & e-mail Policy").click()

        self.page.wait_for_timeout(5000)
        self.page.get_by_role("button", name="Submit").click()


        self.page.wait_for_timeout(15000)

    def get_policy_number(self):

        policy_text = self.page.locator("text=Policy #:").text_content()

        policy_number = (policy_text.replace("Policy #:","").strip())

        print(f"Policy Number : {policy_number}")

        return policy_number