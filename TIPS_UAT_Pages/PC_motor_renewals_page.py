
from playwright.sync_api import Page, expect


class MotorRenewalPage:

    def __init__(self, page: Page):
        self.page = page

        # ---------------- QMS Tile ----------------#
        self.qms_tile = self.page.get_by_text("QMS Quotation", exact=False).click()

        # Renewal search
        self.policy_number_field = page.locator("#dx-input-0").nth(1).click()

        self.search_button = page.get_by_role("button", name="search Search Policy")

        # Renewal record
        self.edit_button = page.get_by_role("button", name="edit")

        # Confirmation
        self.confirm_policy_text = page.get_by_text("Confirm this is the Policy to be Renewed",
                                                    exact=False)

    # =====================================================
    # 1. Search Policy Using Policy Number
    # =====================================================
    def search_policy(self, policy_number: str):

        self.policy_number_field.fill(str(policy_number))
        self.search_button.click()

        expect(self.edit_button.first).to_be_visible(
            timeout=30000
        )

        print(f"Policy searched: {policy_number}")

    # =====================================================
    # 2. Open Renewal Record
    # =====================================================
    def open_policy_for_renewal(self):

        self.edit_button.first.click()

        expect(self.page).to_have_url("**/qms/newrenewal/motor-renewal/policy-confirmation**", timeout=60000)

        expect(self.confirm_policy_text).to_be_visible(timeout=30000)

        print("Renewal policy details opened")

    # =====================================================
    # 3. Confirm Policy
    # =====================================================
    def confirm_renewal_policy(self):

        expect(self.confirm_policy_text).to_be_visible(
            timeout=30000
        )

        # Click the confirmation only if it is not already selected.
        checkbox = self.page.locator(
            "input[type='checkbox']"
        ).filter(
            has=self.confirm_policy_text
        )

        if checkbox.count() > 0:
            if not checkbox.first.is_checked():
                checkbox.first.check()
        else:
            # Fallback for a custom checkbox UI.
            self.confirm_policy_text.click()

        print("Policy confirmation completed")

    # =====================================================
    # 4. Optional Policy Change
    # =====================================================
    def process_optional_change(self, data):

        reason = str(
            data.get("Change Reason") or ""
        ).strip()

        # No change requested: skip this section.
        if reason.lower() in (
            "", "none", "no change", "n/a"
        ):
            print("No policy changes requested")
            print("Skipping optional policy-change section")
            return

        # Select the requested reason.
        reason_buttons = {
            "Update Place of Use": "Update Place of Use",
            "Update Vehicle Spec.": "Update Vehicle Spec.",
            "Update Policyholder Details":
                "Update Policyholder Details",
        }

        if reason not in reason_buttons:
            raise ValueError(
                f"Invalid Change Reason: {reason}. "
                f"Allowed values: {list(reason_buttons)}"
            )

        reason_button = self.page.get_by_role(
            "button",
            name=reason_buttons[reason],
            exact=True
        )

        expect(reason_button).to_be_visible(timeout=30000)
        reason_button.click()

        print(f"Selected change reason: {reason}")

        # Fill the relevant form using its accessible labels.
        # These labels must match the actual form in your UAT app.
        if reason == "Update Place of Use":

            place = str(
                data.get("New Place of Use") or ""
            ).strip()

            if not place:
                raise ValueError(
                    "New Place of Use is required for this change"
                )

            self._select_dropdown_value(
                label="Place of Use",
                value=place
            )

        elif reason == "Update Vehicle Spec.":

            engine_number = str(
                data.get("New Engine Number") or ""
            ).strip()

            engine_capacity = str(
                data.get("New Engine Capacity") or ""
            ).strip()

            if engine_number:
                self.page.get_by_label(
                    "Engine Number", exact=False
                ).fill(engine_number)

            if engine_capacity:
                self.page.get_by_label(
                    "Engine Capacity", exact=False
                ).fill(engine_capacity)

            if not engine_number and not engine_capacity:
                raise ValueError(
                    "Provide a new engine number or capacity"
                )

        elif reason == "Update Policyholder Details":

            address = str(
                data.get("New Address") or ""
            ).strip()

            registration_id = str(
                data.get("New Registration ID") or ""
            ).strip()

            if address:
                self.page.get_by_label(
                    "Address", exact=False
                ).fill(address)

            if registration_id:
                self.page.get_by_label(
                    "Registration ID", exact=False
                ).fill(registration_id)

            if not address and not registration_id:
                raise ValueError(
                    "Provide a new address or registration ID"
                )

        print("Requested change fields entered")
        print(
            "Save the change using the form's actual Save/Apply "
            "button before continuing."
        )

    # =====================================================
    # Helper: Select Dropdown Value
    # =====================================================
    def _select_dropdown_value(self, label: str, value: str):

        field = self.page.get_by_label(label, exact=False)

        expect(field).to_be_visible(timeout=15000)
        field.click()

        option = self.page.get_by_text(value, exact=True)

        expect(option).to_be_visible(timeout=15000)
        option.click()

        print(f"{label} selected: {value}")

    # =====================================================
    # 5. Continue Renewal
    # =====================================================
    def click_save_to_proceed(self):

        button = self.page.get_by_text("Save to Proceed", exact=True)

        expect(button).to_be_visible(timeout=30000)
        button.click()

        print("Clicked Save to Proceed")

    def click_save_and_next(self):

        button = self.page.get_by_text("Save & Next", exact=True)

        expect(button).to_be_visible(timeout=30000)
        button.click()

        print("Clicked Save & Next")
