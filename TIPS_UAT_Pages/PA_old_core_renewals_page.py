
from pathlib import Path
from playwright.sync_api import Page, expect


class RenewalPage:

    def __init__(self, page: Page):
        self.page = page

        # ---------------- QMS Tile ----------------#
        self.qms_tile = self.page.get_by_text("QMS Quotation", exact=False)

        # ---------------- Renewal Menu ----------------#
        self.renewal_menu = self.page.get_by_role("link", name="autorenew Renewal")

        # ---------------- Search Policy Button ----------------#
        self.search_policy_button = self.page.get_by_role("button", name="search Search Policy")

        # ---------------- Personal Accident / Travel Category ----------------
        self.pa_travel_category = self.page.get_by_text("Personal Accident, Travel & Health", exact=False)

    # =====================================================
    # Open QMS Module
    # =====================================================
    def open_qms(self):

        # Wait until the QMS tile is visible
        expect(self.qms_tile).to_be_visible(timeout=30000)

        # Click QMS Quotation
        self.qms_tile.click(timeout=30000)

        print("QMS Quotation tile selected successfully")

    # =====================================================
    # Open Renewal Module
    # =====================================================
    def open_renewal(self):

        # Wait until Renewal menu is visible
        expect(self.renewal_menu).to_be_visible(timeout=30000)

        # Click Renewal
        self.renewal_menu.click(timeout=30000)

        # Wait for Renewal list page
        self.page.wait_for_url("**/qms/newrenewal/list", timeout=60000)

        # Verify Search Policy button
        expect(self.search_policy_button).to_be_visible(timeout=30000)

        print("Renewal page opened successfully")

    # =====================================================
    # Select Personal Accident / Travel Category
    # =====================================================
    def select_pa_travel_category(self):

        expect(self.pa_travel_category).to_be_visible(timeout=30000)

        self.pa_travel_category.click()

        print("Personal Accident / Travel category selected")

    # =====================================================
    # Inspect Renewal Search Form
    # =====================================================
    def inspect_search_form(self):

        # Open Search Policy form
        self.search_policy_button.click(timeout=30000)

        # Wait for the form to render
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1500)

        # ---------------- Print Visible Input Fields ----------------
        inputs = self.page.locator("input:visible, textarea:visible")

        print("\n========== RENEWAL SEARCH FIELDS ==========")

        for index in range(inputs.count()):
            field = inputs.nth(index)

            print(
                f"Field {index + 1}: "
                f"placeholder={field.get_attribute('placeholder')!r}, "
                f"aria-label={field.get_attribute('aria-label')!r}, "
                f"value={field.input_value()!r}"
            )

        # ---------------- Print Visible Labels ----------------
        labels = self.page.locator("label:visible")

        print("\n========== RENEWAL SEARCH LABELS ==========")

        for index in range(labels.count()):
            print(
                f"Label {index + 1}: "
                f"{labels.nth(index).inner_text().strip()}"
            )

        # ---------------- Print Visible Buttons ----------------
        buttons = self.page.get_by_role("button")

        print("\n========== VISIBLE BUTTONS ==========")

        for index in range(buttons.count()):
            button = buttons.nth(index)

            if button.is_visible():
                print(
                    f"Button {index + 1}: "
                    f"{button.inner_text().strip()!r}"
                )

        # ---------------- Save Screenshot ----------------
        screenshot_folder = Path("screenshots")
        screenshot_folder.mkdir(exist_ok=True)

        self.page.screenshot(
            path=str(
                screenshot_folder / "renewal_search_form.png"
            ),
            full_page=True
        )

        print("\nSearch form details printed")
        print("Screenshot: screenshots/renewal_search_form.png")
