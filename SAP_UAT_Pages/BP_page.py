class BPPage:

    def __init__(self, page):
        self.page = page
        self.frame = page.locator("iframe[title='Application']").content_frame

    def fill_policy_and_business_partner(self, business_partner):
        """Sets the Policy Title and links the Business Partner to the policy."""

        # ---- Policy Title ----
        self.frame.get_by_role("textbox", name="Policy Title Required").click()
        self.frame.get_by_text("All Risk", exact=True).click()
        #self.frame.get_by_text(policy_title, exact=True).click()

        # ---- Open the Business Partner detail panel ----
        self.frame.locator(".urST5SCMetricInner").click()
        self.frame.get_by_role("button", name="Detail").click()

        # ---- Enter Business Partner number and confirm ----
        bp_field = self.frame.get_by_role("textbox", name="Business Partner Required")
        bp_field.click()
        bp_field.fill(str(business_partner))
        bp_field.press("Enter")
        self.page.wait_for_timeout(2000)  # wait for the Business Partner details to load

        self.frame.get_by_role("button", name="Copy").click()

        print(f"Business Partner No: {business_partner}")