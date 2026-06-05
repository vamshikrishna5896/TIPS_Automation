import allure


class PAEndorsementPage:

    def __init__(self, page):
        self.page = page

    @allure.step("Search Policy")
    def search_policy(self, policy_no):

        self.page.wait_for_timeout(3000)

        # Product Dropdown
        self.page.locator(".mat-select-placeholder").click()

        self.page.get_by_text("Personal Accident",exact=True).click()

        # Policy Number
        self.page.locator("mat-form-field").filter(has_text="Policy #").locator("#dx-input-2").fill(policy_no)

        # Search
        self.page.get_by_role("button",name="search Search Policy").click()

        self.page.wait_for_timeout(5000)

        # Select Policy
        self.page.get_by_text("M",exact=True).click()

        self.page.get_by_role("button",name="Next").click()

    @allure.step("Select Endorsement Type")
    def select_endorsement_type(self):

        self.page.wait_for_timeout(3000)

        self.page.get_by_text("Confirm this is the policy to").click()

        self.page.get_by_text("Correct Policyholder Details").click()

    @allure.step("Update Tax ID")
    def update_tax_id(self, tax_id):

        self.page.locator(".mat-select-placeholder").click()

        self.page.get_by_text("Correct / update Tax ID").click()

        self.page.locator("mat-form-field").filter(has_text="Tax ID # *").get_by_placeholder("Enter").fill(tax_id)

    @allure.step("Submit Endorsement")
    def submit_endorsement(self):

        self.page.get_by_text("I/We declare that the Policy").click()

        self.page.get_by_role("button",name="Save").click()

        self.page.wait_for_timeout(2000)

        self.page.get_by_role("button",name="Next").click()

        self.page.wait_for_timeout(2000)

        self.page.get_by_role("button",name="Proceed").click()

        self.page.wait_for_timeout(2000)

        self.page.get_by_role("button",name="Submit for Processing").click()

    @allure.step("Download Endorsement Schedule")
    def download_schedule(self):

        self.page.get_by_role("button",name="View Change Schedule").click()

        self.page.get_by_text("Download Endorsement Schedule").click()

        with self.page.expect_download():

            self.page.get_by_role("button",name="Submit").click()

        self.page.wait_for_timeout(3000)