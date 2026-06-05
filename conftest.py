import os
import pytest
import allure

from playwright.sync_api import sync_playwright

from TIPS_Pages.login_page import LoginPage
from TIPS_Pages.logout_page import LogoutPage


# ==========================================
# PAGE FIXTURE
# ==========================================

@pytest.fixture(scope="function")
def page(request):

    playwright = sync_playwright().start()

    browser = playwright.firefox.launch(
        headless=False,
        args=["--start-maximized"]
    )

    context = browser.new_context(
        viewport=None
    )

    # Start Playwright Trace
    # context.tracing.start(
    #     screenshots=True,
    #     snapshots=True,
    #     sources=True
    # )

    page = context.new_page()

    # Login
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
    except Exception:
        pass

    yield page

    print("Test Finished - Starting Teardown")

    # Save trace only if test failed
    try:

        if hasattr(request.node, "rep_call"):

            if request.node.rep_call.failed:

                os.makedirs(
                    "traces",
                    exist_ok=True
                )

                context.tracing.stop(
                    path=f"traces/{request.node.name}.zip"
                )

                print("Trace Saved")

            else:

                context.tracing.stop()

    except Exception as e:

        print(f"Trace Error: {e}")

    # Logout
    try:

        logout = LogoutPage(page)

        logout.logout()

        print("Logout Successful")

    except Exception as e:

        print(f"Logout Error: {e}")

    # Close Context
    try:

        context.close()

    except Exception as e:

        print(f"Context Close Error: {e}")

    # Close Browser
    try:

        browser.close()

    except Exception as e:

        print(f"Browser Close Error: {e}")

    # Stop Playwright
    try:

        playwright.stop()

    except Exception as e:

        print(f"Playwright Stop Error: {e}")


# ==========================================
# PYTEST HOOK
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
# SCREENSHOT ON FAILURE
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

            print("Screenshot Captured")