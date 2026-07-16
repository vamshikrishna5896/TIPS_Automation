class CommissionPage:

    def __init__(self, page):
        self.page = page
        self.frame = page.locator("iframe[title='Application']").content_frame

    def fill_commission(self, commission_contract):
        
        self.frame.get_by_role("tab", name="Commission").click()
        self.frame.get_by_role("button", name="Add").click()

        contract_field = self.frame.get_by_role("textbox", name="Comm. Contract No.")
        contract_field.click()
        contract_field.fill(str(commission_contract))
        contract_field.press("Enter")
        self.page.wait_for_timeout(2000)

        self.frame.get_by_role("button", name="Copy").click()
        self.page.wait_for_timeout(2000)
        self.frame.get_by_role("button", name="Complete Business Transaction").click()

        print(f"Commission Contract No: {commission_contract}")