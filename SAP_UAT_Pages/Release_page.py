class ReleasePage:

    def __init__(self, page):
        self.page = page
        self.frame = page.locator("iframe[title='Application']").content_frame

    def release_application(self):

        # -------------------------------
        # Complete Business Transaction
        # -------------------------------
        try:
            complete_button = self.frame.get_by_role(
                "button", name="Complete Business Transaction")

            if complete_button.is_visible(timeout=5000):
                complete_button.click()
                print("Complete Business Transaction clicked successfully.")
            else:
                print("Complete Business Transaction button not available. Continuing...")

        except Exception:
            print("Complete Business Transaction button not available. Continuing...")
        
        

        # -------------------------------
        # Check Application
        # -------------------------------
        self.frame.get_by_role("button", name="Check").click()

        self.page.wait_for_timeout(3000)

        # -------------------------------
        # Calculate Application
        # -------------------------------
        self.frame.get_by_role("button", name="Calculate Application").click()


        self.page.wait_for_timeout(8000)


        # -------------------------------
        # # Read Premium Details
        # # -------------------------------
        # premium_before_tax = self.frame.get_by_role("textbox", name="Premium Before Tax").input_value()
        #
        # cum_tax_submission = self.frame.get_by_role("textbox", name="Cum.Tax/Submissn Amt").input_value()
        #
        # premium_after_tax = self.frame.get_by_role("textbox", name="Premium After Tax").input_value()
        #
        # stamp_duty = self.frame.get_by_role("textbox", name="Stamp Duty").input_value()
        #
        # basic_premium = self.frame.get_by_role("textbox", name="Basic Premium").input_value()

        # print("\n===== PREMIUM DETAILS =====")
        # print(f"Premium Before Tax   : {premium_before_tax}")
        # print(f"Cum.Tax/Submissn Amt : {cum_tax_submission}")
        # print(f"Premium After Tax    : {premium_after_tax}")
        # print(f"Stamp Duty           : {stamp_duty}")
        # print(f"Basic Premium        : {basic_premium}")

        # -------------------------------
        # Read Policy Details
        # -------------------------------
        policy_number = self.frame.get_by_role("textbox", name="Policy Number").input_value()

        policy_holder = self.frame.get_by_role("textbox", name="Policyholder").input_value()

        application_number = self.frame.get_by_role("textbox", name="Application Number").input_value()

        effective_date = self.frame.get_by_role("textbox", name="Effective Date").input_value()

        # -------------------------------
        # Release Application
        # -------------------------------
        self.frame.get_by_role("button", name="Release Application").click()

        self.page.wait_for_timeout(3000)

        # -------------------------------
        # Continue Release
        # -------------------------------
        self.frame.get_by_role("button", name="Continue Release").click()

        self.page.wait_for_timeout(3000)

        self.frame.get_by_role("button", name="Continue Release").click()
        print("Policy Released successfully")

        # Wait until Policy Summary page loads
        self.frame.get_by_role("textbox", name="Policy Number").wait_for(state="visible", timeout=30000)


        # -------------------------------
        # Print in Terminal
        # -------------------------------
        print("\n========== POLICY DETAILS ==========")
        print(f"\nPolicy Number      : {policy_number}")
        print(f"\nPolicy Holder      : {policy_holder}")
        print(f"\nApplication Number : {application_number}")
        print(f"\nEffective Date     : {effective_date}")

        print("Application released successfully.")

        # -------------------------------
        # Return Details
        # -------------------------------
        return {
            "Policy Number": policy_number,
            "Policy Holder": policy_holder,
            "Application Number": application_number,
            "Effective Date": effective_date,
            # "premium_before_tax": premium_before_tax,
            # "Cum.Tax/Submissn Amt": cum_tax_submission,
            # "Premium After Tax": premium_after_tax,
            # "Stamp Duty": stamp_duty,
            # "Basic Premium": basic_premium
        }