class LoginPage:

    URL = "https://tus4appuat.tuneprotect.com:44303/sap/bc/ui2/flp#Shell-home"
    USERNAME = "VSWAPNA"
    PASSWORD = "Quality@12345"

    def __init__(self, page):
        self.page = page

    def login(self):

        self.page.goto(LoginPage.URL)

        # ---- Screen 1: IDP login ----
        self.page.get_by_role("textbox", name="User *").fill(LoginPage.USERNAME)
        self.page.get_by_role("textbox", name="Password *").fill(LoginPage.PASSWORD)
        self.page.get_by_role("button", name="Log On").click()

        # ---- Screen 2: SAP application login ----
        self.page.get_by_role("textbox", name="User").fill(LoginPage.USERNAME)
        self.page.get_by_role("textbox", name="Password").fill(LoginPage.PASSWORD)
        self.page.get_by_role("button", name="Log On").click()