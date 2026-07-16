class ReleasePage:

    def __init__(self, page):
        self.page = page
        self.frame = page.locator("iframe[title='Application']").content_frame

    def release_application(self):
        """Runs the final checks and releases the policy application."""

        self.frame.get_by_role("textbox", name="Policy Number").click()
        self.frame.get_by_role("button", name="Complete Business Transaction").click()

        self.frame.get_by_role("button", name="Check").click()
        self.frame.get_by_role("button", name="Calculate Application").click()
        self.frame.get_by_role("button", name="Release Application").click()

        # SAP asks for confirmation twice before the release actually goes through
        self.frame.get_by_role("button", name="Continue Release").click()
        self.frame.get_by_role("button", name="Continue Release").click()

        print("Application released successfully")