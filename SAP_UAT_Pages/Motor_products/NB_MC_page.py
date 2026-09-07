
class MotorcyclePage:

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
    #def open_risk_item(self, coverage_type="Third Party"):
        self.page.wait_for_timeout(2000)

        motorcycle = self.frame.get_by_text("Motorcycle", exact=True)
        motorcycle.nth(1).dblclick()
        self.page.wait_for_timeout(2000)
        motorcycle.nth(1).dblclick()
        self.frame.get_by_role("textbox", name="Coverage Type Required").click()
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
    def fill_vehicle_details(self, unit_type):

        self.frame.get_by_role("textbox", name="Unit Type Required").click()
        self.frame.get_by_role("option", name=unit_type).click()

        self.frame.get_by_role("button", name="Copy  Emphasized").click()
        self.frame.get_by_role("button", name="Complete Business Transaction").click()


    # =====================================================
    # Coverage selection
    # =====================================================
    def select_coverage(self, coverage_name="Comprehensive"):
    #def select_coverage(self, coverage_name="Third Party Liability"):
        self.page.wait_for_timeout(2000)
        coverage = self.frame.get_by_text(coverage_name, exact=True).first
        coverage.scroll_into_view_if_needed()
        coverage.dblclick()
        self.page.wait_for_timeout(1000)
        # Locate again after the tree refreshes
        coverage = self.frame.get_by_text(coverage_name, exact=True).first
        coverage.dblclick()
        print(f"Coverage selected: {coverage_name}")

