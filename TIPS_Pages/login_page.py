class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, username, password):

        #Navigate to the login page and perform login.
        #self.page.goto("https://ath-uat.tuneinsurance.com/realms/tune/protocol/openid-connect/auth?response_type=code&client_id=1003&state=M3puV2xCQll2NVB3TkFVTzdNUzQ3NUJzNW5UNHVzMmwyM3V5cjhCSXkxelVw&redirect_uri=https%3A%2F%2Fagent-uat.tuneinsurance.com%2F%2Fhome%3Fiss%3Dhttps%253A%252F%252Fath-uat.tuneinsurance.com%252Frealms%252Ftune&scope=openid%20profile&code_challenge=_1sv3yv4lIl2_03iBRBMcCsr4dcYnc8maujnwS7c1w8&code_challenge_method=S256&nonce=M3puV2xCQll2NVB3TkFVTzdNUzQ3NUJzNW5UNHVzMmwyM3V5cjhCSXkxelVw")
        self.page.goto("https://agent-uat.tuneinsurance.com/")

        self.page.get_by_role("textbox", name="Username or email").fill(username)

        self.page.get_by_role("textbox", name="Password").fill(password)

        # Click login and wait for the app to redirect to the agent home page.
        self.page.get_by_role("button", name="Login").click()

        try:
            self.page.wait_for_url("**/home**", timeout=60000)
        except Exception:

            try:
                self.page.wait_for_selector("text=request_quote", timeout=60000)
            except Exception:
                # Let the original failure surface in tests if login didn't complete.
                pass