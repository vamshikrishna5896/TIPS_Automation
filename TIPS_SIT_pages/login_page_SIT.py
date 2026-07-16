
class LoginPageSIT:

    def __init__(self, page):
        self.page = page

    def login(self):
        #Navigate to the login page and perform login.
        self.page.goto("https://tune.sit.indigit.io/")

        username = "swapna.veguru@serole.com"
        self.page.get_by_role("textbox", name="Username or email").fill(username)

        password = "Serole@123"
        self.page.get_by_role("textbox", name="Password").fill(password)

        # Click login and wait for the app to redirect to the agent home page.
        self.page.get_by_role("button", name="Login").click()
        self.page.wait_for_timeout(6000)

        return username

    def navigate_to_ccm(self):
        self.page.get_by_text("Customer Communication Management", exact=True).click(timeout=60000)

    def navigate_to_dms(self):
        self.page.get_by_text("Document Management System", exact=True).click(timeout=60000)

