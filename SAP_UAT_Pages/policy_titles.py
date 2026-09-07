class HeaderPage:

    def __init__(self, page):
        self.page = page
        self.frame = page.locator("iframe[title='Application']").content_frame

    def select_policy_title(self, policy_title):

        title = self.frame.get_by_role("textbox", name="Policy Title Required")
        title.click()
        self.frame.get_by_text(policy_title, exact=True).click()

        print(f"Policy Title : {policy_title}")

    def select_pa_policy_title(self, policy_title):
        title = self.frame.get_by_role("textbox", name="Policy Title Required")
        title.click()
        self.frame.get_by_text(policy_title, exact=True).click()

        print(f"Policy Title : {policy_title}")