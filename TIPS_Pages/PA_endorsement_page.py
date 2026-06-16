from pathlib import Path

class PAEndorsementPage:

    def __init__(self, page):
        self.page = page

    # ==================================
    # Search Policy
    # ==================================
    def search_policy(self, policy_number):

        # Product Type
        self.page.locator(".mat-select-placeholder").click()
        self.page.get_by_text("Personal Accident", exact=True).click()

        # Policy Number
        self.page.locator("mat-form-field").filter(has_text="Policy #").locator("#dx-input-2").fill(policy_number)

        # Search
        self.page.get_by_role("button", name="search Search Policy").click()

        self.page.wait_for_timeout(5000)

        # Select First Record
        self.page.locator("div.avatar.d-flex").first.click()

        # Next
        self.page.get_by_role("button", name="Next").last.click()

        # Wait loader
        self.page.wait_for_load_state("networkidle")
        self.page.locator(".dx-loading-backdrop").last.wait_for(state="hidden", timeout=60000)
        self.page.wait_for_timeout(4000)

        # Confirm Policy
        self.page.locator("#dx-checkbox-0-input").check(force=True)

    # ==================================
    # Select Endorsement Reason
    # ==================================
    def select_endorsement_reason(self, main_reason, sub_reason):

        self.page.get_by_text(main_reason, exact=True).click()

        self.page.locator(".mat-select-placeholder").click()

        self.page.get_by_role("option", name=sub_reason).click()

    # ==================================
    # Update Occupation
    # ==================================
    def update_occupation(self):

        # Occupation Class
        self.page.locator(".mat-select-placeholder").click()

        self.page.get_by_role("option", name="Class 1").click()

        self.page.get_by_role("button", name="Save").click()

    # ==================================
    # Generate Endorsement Form
    # ==================================
    def generate_endorsement_form(self):

        self.page.get_by_role("button", name="Generate Endorsement Form").click()

        self.page.get_by_text("Download Endorsement Form").click()

        with self.page.expect_download():
            self.page.get_by_role("button", name="Submit").click()
        self.page.get_by_role("button", name="Next").click()
        self.page.wait_for_timeout(4000)


    def upload_file(self):
        project_root = Path(__file__).parent.parent

        file_path = project_root / "uploads" / "Testfile.png"

        # Upload to Endorsement Form row
        self.page.locator("#fileDropRef0").first.set_input_files(str(file_path))

        self.page.wait_for_timeout(3000)

        print("Endorsement Form Uploaded Successfully")


    # ==================================
    # Submit Endorsement
    # ==================================
    def submit_endorsement(self):

        # get Quote Number
        quote_text = self.page.locator("text=Quote Reference #").locator("xpath=following-sibling::*").inner_text()

        quote_number = quote_text.strip()

        print(f"Quote Number : {quote_number}")

        self.page.get_by_role("button", name="Submit for Processing").click()

        self.page.get_by_role("button", name="Proceed").click()

        # Sales Approval  ==> Agency su1
        browser = self.page.context.browser

        sales_context = browser.new_context()

        sales_context_page = sales_context.new_page()

        sales_context_page.goto("https://agent-uat.tuneinsurance.com/#/endorsement/worklist")

        sales_context_page.get_by_role("textbox", name="Username or email").fill("authorizeduser1@gmail.com")

        sales_context_page.get_by_role("textbox", name="Password").fill("Serole@123")

        sales_context_page.get_by_role("button", name="Login").click()

        sales_context_page.wait_for_timeout(30000)



