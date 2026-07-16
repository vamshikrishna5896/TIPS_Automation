import allure
from pathlib import Path

class MotorPCNVPage:

    def __init__(self,page):
        self.page = page

    def create_motor_policy(self, mykad, customer_name, sum_insured):

        # Motor Product
        self.page.get_by_role("heading", name="Motor").click()
        self.page.wait_for_timeout(1000)
        # New registration button
        self.page.get_by_role("heading", name="New Registration").click()
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("button", name="Next").click()
        self.page.wait_for_timeout(2000)

        # Product selection
        self.page.get_by_role("button", name="Private Motor Car").click()
        self.page.wait_for_timeout(2000)
        # State
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.get_by_role("option", name="Kedah").click()
        self.page.wait_for_timeout(2000)

        # --------Vehicle Use-------------#
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.get_by_role("option", name="Private Use (Drive to Work /").click()
        # Engine Number
        self.page.locator("mat-form-field").filter(has_text="Engine # *").locator("#engineNo").click()
        self.page.locator("mat-form-field").filter(has_text="Engine # *").locator("#engineNo").fill("356457457")

        # ==============Chassis NO ==================#
        self.page.locator("mat-form-field").filter(has_text="Chassis # *").locator("#chassisNo").click()
        self.page.locator("mat-form-field").filter(has_text="Chassis # *").locator("#chassisNo").fill("46354645745")
        self.page.wait_for_timeout(2000)
        # ==============Vehicle Make ==============#
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.get_by_role("option", name="HONDA").click()

        # ============Vehicle Model ============ #
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.get_by_role("option", name="CRX").click()

        # Vehicle Year
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.get_by_role("option", name="2025").click()

        # Variant
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.get_by_role("option", name="NA").click()
        self.page.wait_for_timeout(2000)
        #self.page.pause()

        # Engine capacity
        self.page.locator("mat-form-field").filter(has_text="Engine Capacity *").locator("#cc").click()
        self.page.locator("mat-form-field").filter(has_text="Engine Capacity *").locator("#cc").fill("1220")
        self.page.wait_for_timeout(2000)

        self.page.locator(".mat-select-placeholder.mat-select-min-line.ng-tns-c176-105").click()
        self.page.get_by_role("option", name="CONVERTIBLE").click()

        self.page.locator("mat-form-field").filter(has_text="Seating Capacity *").locator("#seatCapacity").click()
        self.page.locator("mat-form-field").filter(has_text="Seating Capacity *").locator("#seatCapacity").fill("4")

        self.page.get_by_role("button", name="Save Vehicle Info").click()
        self.page.wait_for_timeout(4000)

        # Sum Insured
        sum_insured_field = (self.page.locator("mat-form-field").filter(has_text="Vehicle Sum Insured").locator("input#sumInsured"))
        sum_insured_field.click()
        sum_insured_field.clear()
        sum_insured_field.fill(str(sum_insured))
        sum_insured_field.press("Tab")
        print(f"Sum Insured Entered : {sum_insured}")
        # # Sum Insured Field
        # sum_insured_field = (self.page.locator("mat-form-field").filter(has_text="Vehicle Sum Insured").locator("input#sumInsured"))
        # sum_insured_field.click()
        # sum_insured_field.fill(str(sum_insured))
        #
        # # Press Enter to trigger recalculation
        # sum_insured_field.press("Enter")
        # self.page.wait_for_timeout(2000)

        #Remove Agreed value
        #self.page.get_by_text("Agreed Value", exact=True).click()

        #MyKad ID
        self.page.locator("mat-form-field").filter(has_text="ID # * help").locator("#id").click()
        self.page.locator("mat-form-field").filter(has_text="ID # * help").locator("#id").fill(mykad)
        #Name
        self.page.locator("mat-form-field").filter(has_text="Name as per ID *").locator("#legalName").click()
        self.page.locator("mat-form-field").filter(has_text="Name as per ID *").locator("#legalName").fill(customer_name)

        #save & next button
        self.page.get_by_role("button", name="Save & Next").click()
        self.page.wait_for_timeout(15000)

        # Driver experience
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.locator(".item").first.click()
        self.page.wait_for_timeout(3000)

        # -----yes or edit button----#
        # ---- CHECK IF YES BUTTON EXISTS AND IS ENABLED ----
        yes_button = self.page.get_by_role("button", name="Yes").first

        if yes_button.is_visible():
            yes_button.click()
            self.page.wait_for_timeout(5000)

       # ---- CHECK IF ADDRESS ALREADY EXISTS ----#
       #  add_button = self.page.locator("button[name='Add'], button:has-text('Add')").first
       #  if add_button.is_visible():
       #      add_button.click()
       #      self.page.wait_for_timeout(1000)
        else:
            # ---- STATE ---- (runs for both cases)
            self.page.locator(".mat-select-placeholder").first.click()
            self.page.get_by_role("option", name="Johor").click()
            self.page.wait_for_timeout(3000)

            # ---- PINCODE ----
            self.page.locator(".mat-select-placeholder").first.click()
            self.page.get_by_role("option", name="81100").click()
            self.page.wait_for_timeout(2000)

            # ---- STREET ADDRESS ----
            self.page.get_by_role("combobox", name="Address Line").click()
            self.page.get_by_role("option", name="Taman Desa Harmoni", exact=True).click()
            self.page.wait_for_timeout(2000)

            # ---- SAVE BUTTON (if address is added) ----
            address_save = self.page.locator("button#save")
            if address_save.is_visible():
                address_save.click()
        self.page.wait_for_timeout(3000)
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.get_by_role("option", name="Locked Garage", exact=True).click()
        self.page.wait_for_timeout(1000)
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.get_by_role("option", name="No Alarm(WITHOUT MECHANICAL").click()
        self.page.wait_for_timeout(1000)
        self.page.locator(".mat-select-placeholder").click()
        self.page.get_by_role("option", name="Driver’s Side Airbags (1)").click()
        self.page.wait_for_timeout(1000)
        self.page.get_by_text("We respect your privacy and").click()
        self.page.get_by_text("I hereby confirm that I have").click()
        self.page.wait_for_timeout(1000)

        # ==========================================
        # Get Quote Number
        # ==========================================

        quote_number = self.get_quote_number()

        self.page.wait_for_timeout(2000)

        # TPM Button
        tpm_button = self.page.get_by_role("button", name="Submit for TPM Staff Approval")

        # ==========================================
        # Check if NSTP already
        # ==========================================

        is_nstp = False

        try:

            if (
                    tpm_button.count() > 0
                    and tpm_button.is_visible()
                    and tpm_button.is_enabled()
            ):
                is_nstp = True

        except:
            pass

        # ==========================================
        # If TPM not enabled yet
        # Try Upload Later
        # ==========================================

        if not is_nstp:

            try:

                upload_later = self.page.locator("#isUploadLater-desktop").nth(1)

                if upload_later.is_visible():

                    upload_later.click(force=True)

                    self.page.wait_for_timeout(2000)

                    # Remarks

                    remarks = self.page.locator("#dx-input-textarea-0").nth(1)

                    if remarks.is_visible():
                        remarks.fill("Upload later")

                    self.page.wait_for_timeout(3000)

                    print("Upload Later Selected")

            except Exception as e:

                print(f"Upload Later not available : {e}")

        # ==========================================
        # Recheck TPM Button
        # ==========================================

        try:

            if (
                    tpm_button.count() > 0
                    and tpm_button.is_visible()
                    and tpm_button.is_enabled()
            ):
                is_nstp = True

        except:
            pass

        # ==========================================
        # NSTP FLOW
        # ==========================================

        if is_nstp:

            print("NSTP Case")

            tpm_button.click()

            print("Submitted for TPM Approval")

            self.page.wait_for_timeout(15000)

            browser = self.page.context.browser

            manager_context = browser.new_context(viewport=None)

            manager_page = manager_context.new_page()

            manager_page.set_viewport_size({"width": 1520, "height": 1000})

            manager_page.goto(f"https://agent-uat.tuneinsurance.com/#/qms/quote/motor/nreg/review?quoteNr={quote_number}")

            manager_page.get_by_role("textbox", name="Username or email").fill("rahul@serole.com")

            manager_page.get_by_role("textbox", name="Password").fill("Serole@123")

            manager_page.get_by_role("button", name="Login").click()

            manager_page.wait_for_timeout(30000)

            manager_page.get_by_role("button", name="Accept & Process").click()

            manager_page.wait_for_timeout(10000)

            manager_page.close()

            self.page.reload()

            self.page.wait_for_load_state("networkidle")

            self.page.wait_for_timeout(15000)

        # ==========================================
        # STP FLOW
        # ==========================================

        else:

            print("STP Case")

        # ==========================================
        # COMMON FLOW
        # ==========================================

        self.page.get_by_role("button", name="Generate Quote").click()

        self.page.wait_for_timeout(5000)

        self.page.get_by_role("button", name="Submit").click()

        self.page.wait_for_timeout(5000)

        hold_cover_btn = self.page.get_by_role("button", name="Proceed to Hold Cover")

        self.page.wait_for_timeout(5000)

        hold_cover_btn.click()

        self.page.wait_for_timeout(5000)

        self.page.get_by_role("button", name="Issue Hold Cover").click()

        self.page.wait_for_timeout(25000)

        self.page.get_by_role("button", name="View Generated Hold Cover").click()

        self.page.wait_for_timeout(3000)

        self.page.get_by_role("button", name="Submit").click()

        self.page.wait_for_timeout(15000)

    def get_quote_number(self):
        quote_number = (
            self.page.locator("text=Quote Reference #").locator("xpath=following-sibling::*").inner_text().strip())

        return quote_number

    def get_policy_number(self):
        policy_number = (
            self.page.locator("text=Policy #:").text_content().replace("Policy #:", "").strip())

        return policy_number