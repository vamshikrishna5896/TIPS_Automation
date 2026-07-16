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




# class LogoutPage:
#
#     def __init__(self, page):
#         self.page = page
#
#     def logout(self):
#
#         try:
#             print("Attempting Logout...")
#
#             self.page.wait_for_timeout(2000)
#
#             # Click profile
#             self.page.get_by_text("playwright.test@serole.com", exact=True).click()
#
#             # Click Sign Out
#             self.page.get_by_text("Sign Out", exact=True).click()
#
#             # Wait until login page appears
#             self.page.wait_for_url("**login**", timeout=30000)
#
#             print("Logout Successful")
#
#         except Exception as e:
#             print(f"Logout Failed: {e}")


