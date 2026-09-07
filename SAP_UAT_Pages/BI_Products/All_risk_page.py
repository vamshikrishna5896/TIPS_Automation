class AllRiskPage:

    def __init__(self, page):
        self.page = page
        self.frame = page.locator("iframe[title='Application']").content_frame



    # =====================================================
    # Nature of Risk + Address
    # =====================================================
    def fill_nature_and_address(self,nature_of_risk, state, city_hint,premium_type="OneTime Premium"):

        self.page.wait_for_timeout(2000)
        risk_item = self.frame.get_by_text("All Risks", exact=True)
        risk_item.wait_for(timeout=10000)
        risk_item.dblclick()
        self.page.wait_for_timeout(2000)
        expanded = self.frame.get_by_label("Level 2 Expanded")
        expanded.wait_for(timeout=10000)
        expanded.get_by_text("All Risks", exact=True).dblclick()
        print("All Risks opened successfully.")

        # ---- Nature of Risk ----
        self.frame.get_by_role("textbox", name="Nature of Risk Required").click()
        self.frame.get_by_text(nature_of_risk, exact=True).click()
        print("Nature of Risk selected successfully.")

        # ---- Open Risk tab / Address detail panel ----
        self.frame.get_by_role("tab", name="Risk").click()
        self.frame.locator(".urST5SCMetricInner").click()
        self.frame.get_by_role("button", name="Detail").click()
        self.frame.get_by_role("button", name="Create").click()
        print("Risk detail panel opened successfully.")

        # ---- State ----
        self.frame.get_by_role("textbox", name="State").click()
        self.frame.locator("#ls-inputfieldhelpbutton").click()
        self.frame.get_by_text(state).click()
        self.page.wait_for_timeout(1000)
        self.frame.get_by_role("button", name="Copy").click()
        self.page.wait_for_timeout(2000)
        self.page.keyboard.press("Enter")
        self.frame.get_by_title("Message Log", exact=True).click()  # closes the message popup
        self.page.wait_for_timeout(2000)
        print("State selected successfully.")

        # ---- Postcode
        postcode_field = self.frame.get_by_role("textbox", name="Postcode")
        postcode_field.click()
        self.frame.locator("#ls-inputfieldhelpbutton").click()
        city = self.frame.get_by_text(city_hint, exact=True).first
        city.click()
        self.frame.get_by_role("button", name="Copy").click()
        self.page.wait_for_timeout(2000)
        postcode_field.click()
        postcode_field.press("Enter")
        message = self.frame.get_by_title("Message Log", exact=True)
        if message.is_visible():
            message.click()
        print("Postcode selected successfully.")

        # ---- Save the address / risk item ----
        self.frame.get_by_role("button", name="Save  Emphasized").click()
        self.page.wait_for_timeout(1000)
        self.frame.get_by_role("button", name="Complete").click()
        self.frame.get_by_role("button", name="Copy  Emphasized").click()
        print(f"Risk added -> Nature: {nature_of_risk}, State: {state}")

        #=========Premium tab ==============#
        self.frame.get_by_role("tab", name="Premium").click()
        self.frame.get_by_role("textbox", name="Premium Type").click()
        self.frame.get_by_text(premium_type, exact=True).click()
        self.frame.get_by_role("button", name="Create").click()
        self.page.wait_for_timeout(2000)
        self.frame.get_by_role("button", name="Complete Business Transaction").click()
        #self.frame.get_by_role("button", name="Complete Business Transaction").click()


    def fill_machinery_coverage_and_premium(self, coverage_item="Machinery and Equipment"):
        self.page.wait_for_timeout(2000)
        tree = self.frame.locator("[id^='tree']")
        coverage = tree.get_by_text(coverage_item, exact=True).first
        coverage.wait_for(timeout=10000)
        coverage.dblclick()
        self.page.wait_for_timeout(1000)
        coverage.dblclick()
        print(f"{coverage_item} opened successfully.")

    # =====================================================
    # Limit / Sum Insured
    # =====================================================
    def fill_machinery_limit_amount(self, limit_amount):

        self.frame.get_by_role("tab", name="Limit/Deductible").click()
        self.frame.locator(".urST5SCMetricInner").click()
        self.frame.get_by_label("Limit", exact=True).get_by_role("button", name="Detail").click()

        limit_field = self.frame.get_by_role("textbox", name="Limit Amount(SI) Required")
        limit_field.click()
        limit_field.fill(str(limit_amount))

        self.frame.get_by_role("button", name="Copy  Emphasized").click()

        print(f"Limit Amount (SI) set to: {limit_amount}")

    def fill_office_equipment(self, coverage_item="Office Equipment"):
        self.page.wait_for_timeout(2000)
        tree = self.frame.locator("[id^='tree']")
        coverage = tree.get_by_text(coverage_item, exact=True).first
        coverage.wait_for(timeout=10000)
        coverage.dblclick()
        self.page.wait_for_timeout(1000)
        coverage.dblclick()
        print(f"{coverage_item} opened successfully.")

        # =====================================================
        # Limit / Sum Insured
        # =====================================================

    def fill_office_equipment_limit_amount_(self, limit_amount,coverage_amount="ST All Risk Coverage SI"):
        self.frame.get_by_role("tab", name="Limit/Deductible").click()
        self.page.wait_for_timeout(1000)
        self.frame.get_by_role("button", name="Add").click()
        self.frame.get_by_role("textbox", name="ST All Risk Coverage SI").click()
        self.frame.get_by_role("option", name=coverage_amount).click()
        self.frame.get_by_role("button", name="Create").click()
        self.page.wait_for_timeout(2000)
        limit_field = self.frame.get_by_role("textbox", name="Limit Amount(SI) Required")
        limit_field.click()
        limit_field.fill(str(limit_amount))
        self.frame.get_by_role("button", name="Copy  Emphasized").click()
        print(f"Limit Amount (SI) set to: {limit_amount}")