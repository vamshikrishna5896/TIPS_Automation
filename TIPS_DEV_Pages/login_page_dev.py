
class LoginPage:

    USERNAME = "muralimohan.pagadala@serole.com"
    PASSWORD = "Serole@123"

    def __init__(self, page):
        self.page = page

    def login(self):

        self.page.goto("https://tune.dev.indigit.io/")

        self.page.get_by_role("textbox", name="Username or email").fill(LoginPage.USERNAME)

        self.page.get_by_role("textbox", name="Password").fill(LoginPage.PASSWORD)

        self.page.get_by_role("button", name="Login").click()

        self.page.wait_for_url("**/home**")

    def navigate_to_new_quote(self):

        self.page.wait_for_load_state("networkidle")

        self.page.get_by_text("QMS Quotation").click(timeout=60000)

        #self.page.get_by_role("button",name="New Quote").click(timeout=60000)
