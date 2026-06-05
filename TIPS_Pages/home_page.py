class HomePage:

    def __init__(self, page):
        self.page = page

    def navigate_to_new_quote(self):

        self.page.wait_for_load_state("networkidle")

        self.page.get_by_text("QMS Quotation").click(timeout=60000)

        self.page.get_by_role("button",name="New Quote").click(timeout=60000)

        def navigate_to_endorsement(self):
            self.page.get_by_text("approval Policy Servicing").click()

            self.page.wait_for_timeout(3000)