import allure
from TIPS_utils.date_picker import DatePicker

class Policycreation:

    def __init__(self, page):
        self.page = page

    def create_personal_accident_quote(self,mykad,customer_name, date_type="today"):
        #select product
        self.page.get_by_role("heading",name="Personal Accident, Travel & Health").click()
        # select product type PA
        self.page.locator("h5:has-text('Personal Accident')").click()
        # Next button
        self.page.get_by_role("button",name="Next").click()
        # Mykad ID
        self.page.locator("#dx-input-0").nth(1).fill(mykad)
        # Customer Name
        self.page.locator("mat-form-field").filter(has_text="Name as per ID *").locator("#dx-input-1").fill(customer_name)
        #Select Class type
        self.page.locator(".mat-select-placeholder").first.click()

        self.page.get_by_role("option",name="Class 2").click()
        # Select Occupation
        self.page.locator(".mat-select-placeholder").click()
        #Select Sum Insured
        self.page.get_by_role("option", name="200,000").click()
        self.page.wait_for_timeout(2000)
        #self.page.pause()
        #Radio button No
        self.page.locator("mat-radio-button:has-text('No')").nth(1).click()
        #self.page.get_by_text("No", exact=True).click(force=True)
        #self.page.locator("#mat-radio-9-input").check()
        #self.page.locator("#dx-checkbox-1 > .mat-checkbox-layout > .mat-checkbox-inner-container").click()

        def select_inception_date(self, date_type):

            # Click calendar icon
            self.page.get_by_label("Open calendar").last.click(force=True)

            self.page.wait_for_timeout(2000)

            # Select Today/Tomorrow
            DatePicker.select_date(self.page,date_type)
        #check box
        self.page.locator("dx-label.fw-medium.declaration-text.d-inline-block.text-wrap").click()
        #Save & next button
        self.page.get_by_text("Save & Next", exact=True).click()

        self.page.wait_for_timeout(5000)

        try:
            # If Add button is available
            self.page.get_by_role("button",name="Add").click(timeout=3000)
            print("Add button found")
        except:
            print("Add button not found, proceeding directly")

        # Fill proposer details
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.wait_for_timeout(3000)
        self.page.get_by_role("option",name="Johor").click()
        self.page.wait_for_timeout(2000)
        self.page.locator(".mat-select-placeholder").click()
        self.page.wait_for_timeout(3000)
        self.page.get_by_role("option",name="81100").click()
        self.page.wait_for_timeout(2000)
        self.page.get_by_role("combobox",name="Address Line").click()
        self.page.wait_for_timeout(2000)
        self.page.get_by_text("Desa Harmoni",exact=True).click()
        try:
            # If save button is available
            self.page.get_by_role("button",name="Save").click(timeout=2000)
        except:
            print("Save button not found, proceeding directly")
        self.page.get_by_role("textbox", name="123456789").click()
        self.page.get_by_role("textbox", name="123456789").fill("123654789")
        self.page.get_by_role("textbox", name="Enter").click()
        self.page.get_by_role("textbox", name="Enter").fill("sai@gmial.com")
        self.page.locator("#mat-radio-16-input").check()
        self.page.locator("#mat-radio-18-input").check()
        self.page.locator("#mat-radio-20-input").check()
        self.page.locator("#mat-radio-22-input").check()
        self.page.locator("#mat-radio-24-input").check()
        self.page.get_by_text("We respect your privacy and").click()
        self.page.get_by_text("I hereby confirm that I have").click()
        self.page.get_by_role("button", name="Generate Quote").click()
        self.page.wait_for_timeout(4000)
        self.page.get_by_role("button", name="Download Quote & PDS Documents").click()
        self.page.locator("form").get_by_text("Download Quote & PDS Documents").click()
        self.page.wait_for_timeout(4000)
        self.page.get_by_role("button", name="Download").click()
        self.page.wait_for_timeout(2000)
        self.page.get_by_text("close").click()
        self.page.get_by_role("button", name="Issue Policy").click()
        self.page.get_by_role("button", name="Accept & Proceed").click()
        self.page.wait_for_timeout(18000)
        #------Print Quote Number-------#
        quote_text = self.page.locator("text=Quote Reference #").locator("xpath=following-sibling::*").inner_text()
        quote_number = quote_text.strip()
        print("Quote Number:", quote_number)
        # ---- Printing the policy number ----#
        self.page.policy_locator = self.page.locator("text=Policy #:")
        policy_text = self.page.policy_locator.text_content()
        policy_number = policy_text.replace("Policy #:", "").strip()
        print("Policy Number:", policy_number)
