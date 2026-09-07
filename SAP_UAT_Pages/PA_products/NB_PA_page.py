
class PersonalAccident:

    def __init__(self, page):
        self.page = page
        self.frame = page.locator("iframe[title='Application']").content_frame

    # =====================================================
    # Nature of Risk + Address
    # =====================================================
    def fill_plan_details(self,risk_class,):

        self.page.wait_for_timeout(2000)
        risk_item = self.frame.get_by_text("Personal Accident", exact=True)
        risk_item.wait_for(timeout=10000)
        risk_item.dblclick()
        self.page.wait_for_timeout(2000)
        expanded = self.frame.get_by_label("Level 2 Expanded")
        expanded.wait_for(timeout=10000)
        expanded.get_by_text("Personal Accident", exact=True).dblclick()
        print("Personal Accident opened successfully.")

        # =========================
        # Risk Class 
        # ========================
        self.page.wait_for_timeout(2000)
        self.frame.get_by_role("textbox", name="Risk Class Required").click()
        self.frame.get_by_text(risk_class, exact=True).click()
        self.page.keyboard.press("Enter")
        #self.page.pause()
        print("Risk class selected successfully.")

        # =======================
        # Plan 
        # ========================
        self.page.wait_for_timeout(2000)
        plan_field = self.frame.get_by_role("textbox", name="Plan")
        plan_field.wait_for(state="visible", timeout=30000)
        plan_field.scroll_into_view_if_needed()
        plan_field.click()
        #self.page.pause()
        self.page.wait_for_timeout(1000)
        self.frame.get_by_text("100,000", exact=True).click()
        #self.frame.get_by_text(plan, exact=True).click()
        #print(f"Plan selected successfully: {plan}")

        # ============================
        # Open Risk tab 
        # =============================
    def fill_risk_details(self,bp):
        self.frame.get_by_role("tab", name="Risk").click()
        self.frame.locator(".urST5SCMetricInner").click()
        self.frame.get_by_role("button", name="Detail").click()

        
        # ==============================
        #Coverage Details
        # ==============================
    def adpd_coverage_details(self,):
        self.page.wait_for_timeout(2000)
        self.frame.get_by_title("Expand Node").click()
        self.frame.get_by_text("Renewal Bonus").dblclick()
        self.page.wait_for_timeout(2000)
        self.frame.get_by_text("Personal Liability", exact=True).dblclick()
        
        
        # Add_coverage = self.frame.get_by_text("Personal Liability", exact=True)
        # Add_coverage.wait_for(timeout=10000)
        # Add_coverage.dblclick()
        # self.page.wait_for_timeout(2000)
        # expanded = self.frame.get_by_label("Level 2 Expanded")
                        
        print("plan selected successfully")
