class DMS:

    def __init__(self, page):
        self.page = page

    def navigate_to_dms(self):
        self.page.get_by_text("Document Management System", exact=True).click(timeout=60000)

        self.page.get_by_text("Workspaces", exact=True).click()

    def quote(self):
        self.page.get_by_role("heading", name="Quote").click()
        self.page.wait_for_timeout(2000)
        self.page.get_by_text("Quotation").click()


    def policy(self):
        self.page.get_by_role("heading", name="Policy").click()

