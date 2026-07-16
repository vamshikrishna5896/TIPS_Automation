
class LoginPage:

    USERNAME = "playwright.test@serole.com"
    PASSWORD = "Serole@321"

    def __init__(self, page):
        self.page = page

    def login(self):

        self.page.goto("https://agent-uat.tuneinsurance.com/")

        self.page.get_by_role("textbox", name="Username or email").fill(LoginPage.USERNAME)

        self.page.get_by_role("textbox", name="Password").fill(LoginPage.PASSWORD)

        self.page.get_by_role("button", name="Login").click()

        self.page.wait_for_url("**/home**")

# class LoginPage:
#
#     def __init__(self, page):
#         self.page = page
#
#     def login(self):
#
#          # =========== UAT URL============#
#         self.page.goto("https://agent-uat.tuneinsurance.com/")
#
#          # ===== UAT login cred's=========== #
#         username = "playwright.test@serole.com"
#         self.page.get_by_role("textbox", name="Username or email").fill(username)
#
#         password = "Serole@321"
#         self.page.get_by_role("textbox", name="Password").fill(password)
#
#
#     # Click login and wait for the app to redirect to the agent home page.
#         self.page.get_by_role("button", name="Login").click()
#
#         try:
#             self.page.wait_for_url("**/home**", timeout=60000)
#         except Exception:
#
#             try:
#                 self.page.wait_for_selector("text=request_quote", timeout=60000)
#             except Exception:
#                 # Let the original failure surface in tests if login didn't complete.
#                 pass

