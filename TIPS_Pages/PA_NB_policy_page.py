import allure
from TIPS_utils.date_picker import DatePicker


class Policycreation:

    def __init__(self, page):
        self.page = page

   # @allure.step("Create Personal Accident Policy")
    def create_personal_accident_quote(self, mykad, customer_name, date_type, product_type):

        # Select Product Category
        self.page.get_by_role("heading",name="Personal Accident, Travel & Health").click()

        # Select PA Product
        self.page.locator("h5:has-text('Personal Accident')").click()
        # Next
        self.page.get_by_role("button",name="Next").click()

        # MyKad
        self.page.locator("#dx-input-0").nth(1).fill(mykad)

        # Customer Name
        self.page.locator("mat-form-field").filter(has_text="Name as per ID *").locator("#dx-input-1").fill(customer_name)
        self.page.wait_for_timeout(2000)
        #self.page.pause()

        # Occupation Class
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.get_by_role("option", name="Class 1").click()
        # self.page.get_by_role("option", name="Class 2").click()
        # self.page.get_by_role("option", name="Class 3").click()

        # Product Type
        self.page.locator("#mat-select-value-17").click()
        self.page.get_by_role("option", name=product_type).click()

        self.page.wait_for_timeout(2000)

        # Sum Insured based on Product Type
        self.page.locator(".mat-select-placeholder").click()

        if product_type == "Personal Accident Safe":
            self.page.get_by_role("option", name="50,000", exact=True).click()
            print("Selected Product: PA Safe")
            print("Selected Sum Insured: 50,000")

        else:  # Default = PA Shield
            self.page.get_by_role("option", name="200,000").click()
            print("Selected Product: PA Shield")
            print("Selected Sum Insured: 200,000")
        self.page.wait_for_timeout(2000)

        # Weekly Benefit = No
        self.page.locator("mat-radio-button:has-text('No')").nth(1).click()
        #self.page.pause()
        # ====== Renewal Bonus  ====== #
        # self.page.locator(".mat-slide-toggle-bar").click()
        # self.page.get_by_role("spinbutton").click()
        # self.page.get_by_role("spinbutton").fill("20")
        # self.page.wait_for_timeout(2000)
        # self.page.locator(".mat-select-placeholder").click()
        # self.page.get_by_role("option", name="AIG Malaysia Insurance Berhad").click()

        # ------Inception Date Calendar---------#
        self.page.locator("mat-form-field").filter(has_text="Inception Date").get_by_label("Open calendar").click()
        self.page.wait_for_timeout(1000)
        # Select Date
        DatePicker.select_date(self.page, date_type)

        #--------- Declaration Checkbox ---------------#
        self.page.locator("dx-label.fw-medium.declaration-text.d-inline-block.text-wrap").click()

        # Save & Next
        self.page.get_by_text("Save & Next",exact=True).click()

        self.page.wait_for_timeout(14000)

        # =============================
        # Add Proposer (Optional)
        # =============================

        try:
            self.page.get_by_role("button",name="Add").click(timeout=3000)

            print("Add button found")

        except:
            print("Add button not found")

        # State
        self.page.locator(".mat-select-placeholder").first.click()

        self.page.get_by_role("option",name="Johor").click()
        self.page.wait_for_timeout(2000)
        # Postcode
        self.page.locator(".mat-select-placeholder").click()

        self.page.get_by_role("option",name="81100").click()
        self.page.wait_for_timeout(2000)

        # Address
        self.page.get_by_role("combobox",name="Address Line").click()

        self.page.get_by_text("Desa Harmoni",exact=True).click()
        self.page.wait_for_timeout(2000)

        try:
            self.page.get_by_role("button",name="Save").click(timeout=2000)

        except:
            print("Save button not found")

        # Phone number
        self.page.get_by_role("textbox",name="123456789").fill("123654789")

        # Email
        self.page.get_by_role("textbox",name="Enter").fill("vamshikrishna45@gmail.com")

        #======  Rebate percentage ====== #
        # self.page.locator("mat-form-field").filter(has_text="Rebate to Proposer%").locator("#rebate").click()
        # self.page.locator("mat-form-field").filter(has_text="Rebate to Proposer%").locator("#rebate").fill("25")

        # UW writer Questions  #
        self.page.locator("#mat-radio-16-input").check()
        self.page.locator("#mat-radio-18-input").check()
        self.page.locator("#mat-radio-20-input").check()
        self.page.locator("#mat-radio-22-input").check()
        self.page.locator("#mat-radio-24-input").check()

        # Privacy
        self.page.get_by_text("We respect your privacy and").click()
        self.page.get_by_text("I hereby confirm that I have").click()

        # Generate Quote
        self.page.get_by_role("button",name="Generate Quote").click()

        self.page.wait_for_timeout(6000)

        # Download Quote
        self.page.get_by_role("button", name="Download Quote & PDS Documents").click()
        self.page.wait_for_timeout(1000)
        self.page.locator("form").get_by_text("Download Quote & PDS Documents").click()

        self.page.get_by_role("button",name="Download").click()

        self.page.wait_for_timeout(2000)

        try:
            self.page.get_by_text("close").click()
        except:
            pass

        # Issue Policy
        self.page.get_by_role("button",name="Issue Policy").click()

        self.page.get_by_role("button",name="Accept & Proceed").click()

        self.page.wait_for_timeout(30000)
        # # Wait until policy number is generated
        # self.page.locator("text=Policy #:").wait_for(state="visible", timeout=120000)

        # Quote Number
        try:
            quote_number = self.page.locator("text=Quote Reference #").locator("xpath=following-sibling::*").inner_text()

            #print(f"Quote Number : {quote_number.strip()}")

        except:
            print("Quote Number not found")

    #@allure.step("Get Policy Number")
    def get_policy_number(self):

        self.page.wait_for_timeout(5000)

        try:
            policy_text = self.page.locator("text=Policy #:").text_content()

            policy_number = (policy_text.replace("Policy #:", "").strip())

            #print(f"Policy Number : {policy_number}")

            return policy_number

        except Exception as e:

            print(f"Unable to fetch policy number: {e}")

            return None