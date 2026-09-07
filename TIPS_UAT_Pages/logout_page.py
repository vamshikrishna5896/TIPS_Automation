from TIPS_UAT_Pages.login_page import LoginPage

class LogoutPage:

    def __init__(self, page):
        self.page = page

    def logout(self):
        try:
            username = LoginPage.USERNAME

            self.page.get_by_text(username, exact=True).click()
            self.page.get_by_text("Sign Out").click()

        except Exception as e:
            print(f"Error occurred while trying to logout: {e}")



