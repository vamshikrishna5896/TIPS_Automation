class LogoutPage:

    def __init__(self, page):
        self.page = page

    def logout(self):

        try:

            print("Attempting Logout...")
            print("Current URL:", self.page.url)

            self.page.wait_for_timeout(2000)

            self.page.get_by_text("playwright.test@serole.com", exact=True).click()

            self.page.get_by_text("Sign Out").click(timeout=5000)

            print("Logout Successful")

        except Exception as e:

            print(f"Logout Failed: {e}")