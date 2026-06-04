import os
import pytest
import allure
from playwright.sync_api import sync_playwright

from TIPS_Pages.login_page import LoginPage
from TIPS_Pages.logout_page import LogoutPage


@pytest.fixture(scope="function")
def page():

    playwright = sync_playwright().start()

    browser = playwright.firefox.launch(headless=False,args=["--start-maximized"])

    context = browser.new_context(viewport=None)

    page = context.new_page()

    login = LoginPage(page)

    login.login(
        "playwright.test@serole.com",
        "Serole@321"
    )

    try:
        page.wait_for_load_state(
            "networkidle",
            timeout=60000
        )
    except:
        pass

    yield page

    print("Test Finished - Starting Teardown")

    try:
        logout = LogoutPage(page)
        logout.logout()
    except Exception as e:
        print(f"Logout Error: {e}")

    try:
        context.close()
    except Exception as e:
        print(f"Context Close Error: {e}")

    try:
        browser.close()
    except Exception as e:
        print(f"Browser Close Error: {e}")

    try:
        playwright.stop()
    except Exception as e:
        print(f"Playwright Stop Error: {e}")


# ==========================================
# Pytest Hook
# ==========================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        "rep_" + report.when,
        report
    )


# ==========================================
# Screenshot + Allure Attachment
# ==========================================

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):

    yield

    if hasattr(request.node, "rep_call"):

        if request.node.rep_call.failed:

            os.makedirs(
                "screenshots",
                exist_ok=True
            )

            screenshot_path = (
                f"screenshots/{request.node.name}.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )