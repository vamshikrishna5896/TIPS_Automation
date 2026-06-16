import allure

class PACorrectionPage:

    def __init__(self, page):
        self.page = page
    # ==========================================
    # SEARCH POLICY
    # ==========================================
    def search_policy(self, policy_number):

        self.page.wait_for_timeout(3000)

        # Product Type
        self.page.locator(".mat-select-placeholder").click(); self.page.get_by_text("Personal Accident", exact=True).click()

        # Policy Number
        self.page.locator("mat-form-field").filter(has_text="Policy #").locator("#dx-input-2").fill(policy_number)
        #search policy number
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

        # Confirm checkbox
        self.page.locator("#dx-checkbox-0-input").check(force=True)
    # ==========================================
    # SELECT MAIN REASON + SUB REASON
    # ==========================================
    def select_correction_reason(self, main_reason, sub_reason):

        self.page.wait_for_timeout(2000)

        # Main Reason
        self.page.get_by_text(main_reason, exact=True).click()


        self.page.wait_for_timeout(1000)


        # Sub Reason Dropdown
        self.page.locator(".mat-select-placeholder").click()
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("option", name=sub_reason).click()

    # ==========================================
    # PERFORM CORRECTION
    # ==========================================
    def perform_correction(self, data):

        sub_reason = data["SubReason"]

        # --------------------------  TAX ID   -----------------------------#

        if sub_reason == "Correct / update Tax ID":

            self.page.locator("mat-form-field").filter(has_text="Tax ID #").get_by_placeholder("Enter").fill(str(data["TaxID"]))

        # -----------------------------
        # LEGAL NAME
        # -----------------------------
        elif sub_reason == "Correct Policyholder Legal Name":

            self.page.locator("#legalName").fill(data["NewName"])

        # -----------------------------
        # CONTACT DETAILS
        # -----------------------------
        elif sub_reason == "Update Contact Details":

            self.page.locator("#mobileNo").fill(str(data["Mobile"]))

            self.page.locator("#email").fill(data["Email"])

        else:

            print(f"No logic configured for {sub_reason}")

    # ==========================================
    # SUBMIT CORRECTION
    # ==========================================
    def submit_correction(self):

        self.page.get_by_text("I/We declare that the Policy").click()

        self.page.get_by_role("button", name="Save").click()

        self.page.wait_for_timeout(2000)

        self.page.get_by_role("button", name="Next").click()

        self.page.wait_for_timeout(2000)

        self.page.get_by_role("button", name="Proceed").click()

        self.page.wait_for_timeout(2000)

        self.page.get_by_role("button", name="Submit for Processing").click()

        self.page.wait_for_timeout(5000)

    # ==========================================
    # DOWNLOAD CORRECTION SCHEDULE
    # ==========================================
    def download_schedule(self):

        self.page.get_by_role("button", name="View Change Schedule").click()

        self.page.get_by_text("Download Endorsement Schedule").click()

        with self.page.expect_download():

            self.page.get_by_role("button", name="Submit").click()
        self.page.wait_for_timeout(3000)
        self.page.get_by_role("button", name="close").click()