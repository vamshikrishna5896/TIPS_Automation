
class MotorcarPage:

    def __init__(self, page):
        self.page = page
        self.frame = page.locator("iframe[title='Application']").content_frame
        self.coverage_frame = page.locator("iframe[name='application-ZPM_SEM_OBJ-display']").content_frame

    def wait_for_text_and_click(self, text, exact=False):
        self.frame.get_by_text(text, exact=exact).click()

    # =====================================================
    # Open the risk item + set Coverage Type
    # =====================================================
    def open_risk_item(self, coverage_type="Comprehensive"):
        self.page.wait_for_timeout(2000)
        # Open Risk Item
        self.frame.get_by_text("Private Motor Car Contract", exact=True).dblclick()
        self.frame.get_by_label("Level 2 Expanded").get_by_text("Private Motor Car Contract", exact=True).dblclick()
        # Open Coverage Type dropdown
        coverage_field = self.frame.get_by_role("textbox", name="Coverage Type Required")
        coverage_field.click()
        self.frame.get_by_role("option", name=coverage_type).click()
        print(f"Coverage Type selected: {coverage_type}")
    # =====================================================
    # Vehicle registration
    # =====================================================
    def register_vehicle(self, vehicle_reg_no):

        self.frame.get_by_role("tab", name="Risk").click()
        self.frame.locator(".urST5SCMetricInner").click()
        self.frame.get_by_role("button", name="Detail").click()
        self.frame.get_by_role("button", name="Create").click()

        reg_field = self.frame.get_by_role("textbox", name="Vehicle reg. no.")
        reg_field.click()
        reg_field.fill(str(vehicle_reg_no))
        reg_field.press("Enter")
        self.page.wait_for_timeout(4000)
        self.frame.get_by_role("button", name="Save  Emphasized").click()
        self.page.wait_for_timeout(2000)
        self.frame.get_by_role("button", name="Yes").click()      # confirm save
        self.frame.get_by_role("button", name="Complete").click()
        self.frame.get_by_role("button", name="Yes").click()      # confirm complete
        print(f"Vehicle registered: {vehicle_reg_no}")

    # =====================================================
    # Vehicle detail dropdowns
    # =====================================================
    def fill_vehicle_details(self, safety_features, unit_type, garaged, anti_theft):

        self.frame.get_by_role("textbox", name="Unit Type Required").click()
        self.frame.get_by_role("option", name=unit_type).click()

        self.frame.get_by_role("textbox", name="Safety Features Required").click()
        self.frame.get_by_role("option", name=safety_features).click()
        self.frame.get_by_role("textbox", name="Garaged Required").click()
        self.wait_for_text_and_click(garaged, exact=True)
        self.frame.get_by_role("textbox", name="Anti-Theft Required").click()
        self.frame.get_by_role("option", name=anti_theft).click()
        self.frame.get_by_role("button", name="Copy  Emphasized").click()
        print(f"Vehicle details set -> Safety: {safety_features}, Anti-Theft: {anti_theft}")

    def rebate_percentage(self):
        # Open Premium tab
        premium_tab = self.frame.get_by_role("tab", name="Premium")
        premium_tab.wait_for(state="visible", timeout=30000)
        premium_tab.click()

        self.page.wait_for_timeout(2000)
        # Rebate Percentage field
        rebate_field = self.frame.get_by_role("textbox", name="Rebate as Percentage")
        rebate_field.wait_for(state="visible", timeout=30000)
        rebate_field.scroll_into_view_if_needed()
        # Enter 10%
        rebate_field.click()
        rebate_field.fill("10")
        rebate_field.press("Enter")
        self.page.wait_for_timeout(2000)
        print("Rebate Percentage : 10%")

        # Complete Business Transaction
        self.frame.get_by_role("button", name="Complete Business Transaction").click()
        self.page.wait_for_timeout(3000)
        print("Business Transaction completed successfully.")

    # =====================================================
    # Coverage selection
    # =====================================================
    def select_coverage(self, coverage_name="Comprehensive"):
        self.page.wait_for_timeout(2000)
        coverage = self.frame.get_by_text(coverage_name, exact=True).first
        coverage.scroll_into_view_if_needed()
        coverage.dblclick()
        self.page.wait_for_timeout(1000)
        # Locate again after the tree refreshes
        coverage = self.frame.get_by_text(coverage_name, exact=True).first
        coverage.dblclick()
        print(f"Coverage selected: {coverage_name}")

    # =====================================================
    # Clause
    # =====================================================
    def add_clause(self, clause_type="Named Driver", clause_name="Name"):


        self.frame.get_by_role("tab", name="Clause").click()
        self.frame.get_by_role("button", name="Add").click()

        self.frame.get_by_role("textbox", name="Clause").click()
        self.frame.get_by_role("option", name=clause_type).click()
        self.frame.get_by_role("button", name="Create").click()
        #self.page.pause()

        self.frame.locator("[id=\"grid#C1202#1,2#if\"]").click()
        self.frame.get_by_role("group", name="Clause").get_by_role("textbox").fill(clause_name)

        self.frame.get_by_role("button", name="Complete Business Transaction").click()

        print(f"Clause added: {clause_type} ({clause_name})")

