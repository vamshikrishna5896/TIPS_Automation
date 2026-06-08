import allure
from TIPS_utils.date_picker import DatePicker

class DentalPolicyPage:

    def __init__(self, page):
        self.page = page

    #@allure.step("Create Dental Policy")
    def create_dental_policy(self,mykad,customer_name,date_type):

        # Product Category
        self.page.get_by_role("heading",name="Personal Accident, Travel & Health").click()

        # Dental Shield
        self.page.get_by_role("heading",name="Dental Shield").click()

        # Next
        self.page.get_by_role("button",name="Next").click()
        self.page.wait_for_timeout(2000)

        # MyKad
        self.page.locator("mat-form-field").filter(has_text="ID #").locator("#dx-input-0").fill(mykad)

        # Name
        self.page.locator("mat-form-field").filter(has_text="Name as per ID").locator("#dx-input-1").fill(customer_name)
        self.page.wait_for_timeout(1000)
        #calender
        #self.page.pause()
        # ------Inception Date Calendar---------#
        #self.page.locator("mat-form-field").filter(has_text="Inception Date").get_by_label("Open calendar").click()
        self.page.locator("mat-form-field").filter(has_text="Start Date event").get_by_label("Open calendar").click()
        self.page.wait_for_timeout(1000)
        # Select Date
        DatePicker.select_date(self.page,date_type)

        # Declaration
        self.page.get_by_text("The Proposer/Person(s) to be").click()

        # Proceed
        self.page.get_by_role("button",name="Proceed Quote").click()

        self.page.wait_for_timeout(6000)
        try:
            self.page.get_by_role("button",name="Add").click(timeout=3000)

            print("Add button found")

        except:
            print("Add button not found")

        # State
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.locator("#mat-option-19").click()
        self.page.wait_for_timeout(2000)

        # Postcode
        self.page.locator(".mat-select-placeholder").click()

        self.page.locator(".item").first.click()
        self.page.wait_for_timeout(2000)

        # Address
        self.page.get_by_role("combobox",name="Address Line").click()

        self.page.get_by_text("DYMM Sultan Kedah").click()
        self.page.wait_for_timeout(2000)
        # save button
        try:
            self.page.get_by_role("button",name="Save").click(timeout=2000)

        except:
            print("Save button not found")

        # Tax ID
        self.page.get_by_role("textbox",name="123456789").fill("123654789")

        # Email
        self.page.get_by_role("textbox",name="Enter").fill("vamshi@gmail.com")

        self.page.get_by_text("We respect your privacy and").click()

        self.page.get_by_text("I hereby confirm that I have").click()

        self.page.get_by_role("button",name="Generate Quote").click()

        self.page.wait_for_timeout(8000)

        # Download Quote
        self.page.get_by_role("button",name="Download Quote & PDS Documents").click()

        self.page.wait_for_timeout(2000)

        self.page.get_by_role("button",name="Send").click()

        self.page.wait_for_timeout(2000)

        self.page.get_by_text("close").click()
        self.page.wait_for_timeout(2000)

        # Issue Policy
        self.page.get_by_role("button",name="Issue Policy").click()

        self.page.get_by_role("button",name="Accept & Proceed").click()

        self.page.wait_for_timeout(25000)

    def get_policy_number(self):

        policy_text = self.page.locator("text=Policy #:").text_content()

        policy_number = (policy_text.replace("Policy #:", "").strip())

        print("Policy Number:",policy_number)

        return policy_number