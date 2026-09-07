
class LoginPage:

    USERNAME = "playwright.test@serole.com"
    PASSWORD = "Serole@4355"

    def __init__(self, page):
        self.page = page

    def login(self):

        self.page.goto("https://agent-uat.tuneinsurance.com/")

        self.page.get_by_role("textbox", name="Username or email").fill(LoginPage.USERNAME)

        self.page.get_by_role("textbox", name="Password").fill(LoginPage.PASSWORD)

        self.page.get_by_role("button", name="Login").click()

        self.page.wait_for_url("**/home**")


