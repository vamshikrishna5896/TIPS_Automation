import allure
from datetime import datetime
from TIPS_utils.date_picker import DatePicker

class MotorPCPage:

    def __init__(self,page):
        self.page = page

   #@allure.step("Create Motor Policy")
    def create_motor_policy(self,reg_no,mykad,customer_name, coverage_type, date_type):

        # Motor Product
        self.page.get_by_role("heading",name="Motor").click()

        self.page.get_by_role("button",name="Next").click()

        # Vehicle Number
        self.page.get_by_role("textbox").fill(reg_no)

        # State
        self.page.locator(".mat-select-placeholder").click()

        self.page.get_by_role("option",name="Kedah").click()

        # Click on vehicle search button
        self.page.get_by_role("button",name="search Vehicle Search").click()

        self.page.wait_for_timeout(5000)

        self.page.get_by_role("button",name="Save Vehicle Info").click()

        # ------Inception Date Calendar---------#
        self.page.locator("mat-form-field").filter(has_text="Inception Date").get_by_label("Open calendar").click()
        self.page.wait_for_timeout(1000)
        # Select Date
        DatePicker.select_date(self.page, date_type)
        #self.page.pause()

        # ---------- Coverage Type ----------
        print("Coverage Type:", coverage_type)

        # =====================================================
        # COMPREHENSIVE & TPFT
        # =====================================================
        if coverage_type.lower() in ["comprehensive", "tp fire & theft"]:

            # ---------- Sum Insured Validation ----------
            sum_insured_field = (self.page.locator("mat-form-field").filter(has_text="Vehicle Sum Insured").locator("#sumInsured"))

            current_value = sum_insured_field.input_value()
            current_value = current_value.replace(",", "").strip()

            try:
                current_sum = float(current_value)

                if current_sum < 5000:

                    sum_insured_field.click()
                    sum_insured_field.press("Control+A")
                    sum_insured_field.fill("5000")
                    sum_insured_field.press("Tab")

                    print("Sum Insured updated to 5000")

                else:

                    print(f"Sum Insured is {current_sum}, no update required")

            except Exception:

                sum_insured_field.click()
                sum_insured_field.fill("5000")
                sum_insured_field.press("Tab")

                print("Sum Insured was empty. Updated to 5000")

            self.page.wait_for_timeout(3000)

            # ---------- Agreed Value ----------
            try:

                agreed_value = self.page.get_by_label("Agreed Value", exact=True)

                if not agreed_value.is_checked():
                    agreed_value.check(force=True)
                    print("Agreed Value Checked")

                    # self.page.get_by_text("Adjust Agreed Value").click()
                    #
                    # self.page.locator("mat-form-field").filter(has_text="Agreed Value % *percent Edit").locator("#agreedValue").fill("20")

            except Exception as e:

                print(f"Agreed Value not available: {e}")

            # =====================================================
            # COMPREHENSIVE EXTENSIONS
            # =====================================================
            # if coverage_type.lower() == "comprehensive":
            #
            #     print("Executing Comprehensive Extensions")
            #
            #     self.page.get_by_role("button", name="Extension Coverage").click()
            #
            #     self.page.locator("#mat-select-value-11").click()
            #
            #     self.page.get_by_text("Motor Shield").click()
            #
            #     self.page.get_by_role("button", name="check").nth(1).click()
            #
            #     self.page.locator("mat-form-field").filter(has_text="Sum Insured *MYR").locator("#sumInsured").fill("5000")

                # self.page.locator(
                #     "div:nth-child(7) > .additional-benefit > .additional-benefit-wrapper > .additional-benefit-label > div > .material-icons"
                # ).click()
                #
                # self.page.locator("#sumInsured").nth(5).fill("6000")
                #
                # self.page.get_by_role("button", name="check").nth(2).click()
                #
                # self.page.locator(".mat-radio-outer-circle").first.click()
                #
                # self.page.get_by_role("button", name="check").nth(4).click()

            # =====================================================
            # TPFT EXTENSIONS
            # =====================================================
            # elif coverage_type.lower() == "tp fire & theft":
            #
            #     print("Executing TPFT Extensions")
            #
            #     self.page.get_by_role("button", name="Extension Coverage").click()
            #
            #     self.page.locator("#mat-select-value-11").click()
            #
            #     self.page.get_by_text("Autobuddy").click()
            #
            #     self.page.locator(".mat-select-placeholder").first.click()
            #
            #     self.page.get_by_text("PLAN B").click()
            #
            #     self.page.get_by_text("Extension to Kalimantan and").click()

        # =====================================================
        # THIRD PARTY
        # =====================================================
        # else:
        #
        #     print("Third Party Policy - Skipping Sum Insured, Agreed Value and Extensions")

        #--------------- MyKad ------------#
        self.page.locator("mat-form-field").filter(has_text="ID #").locator("#id").fill(mykad)

        # Name
        self.page.locator("mat-form-field").filter(has_text="Name as per ID").locator("#legalName").fill(customer_name)

        # Validate button
        self.page.get_by_role("button", name="search Validate Owner as per").click()
        self.page.wait_for_timeout(3000)

        # Save & next button
        self.page.get_by_role("button", name="Save & Next").click()
        self.page.wait_for_timeout(5000)

        # Proposer Details
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.locator(".item").first.click()
        # -------------------------------
        # Address Handling
        # -------------------------------

        # Click Yes popup if displayed
        try:
            yes_button = self.page.get_by_role("button", name="Yes").first

            if yes_button.is_visible(timeout=3000):
                yes_button.click()
                self.page.wait_for_timeout(3000)

        except:
            pass

        # Check if Add button exists
        try:
            add_button = self.page.get_by_role("button", name="Add")

            if add_button.is_visible(timeout=5000):
                print("No address found. Creating new address.")

                add_button.click()

                self.page.wait_for_timeout(5000)

                # STATE
                self.page.locator("mat-select").nth(0).click()
                self.page.get_by_text("Johor", exact=True).click()

                self.page.wait_for_timeout(2000)

                # PINCODE
                self.page.locator("mat-select").nth(1).click()
                self.page.get_by_text("81100", exact=True).click()

                self.page.wait_for_timeout(2000)

                # ADDRESS
                self.page.get_by_role("combobox", name="Address Line").click()
                self.page.get_by_role("option", name="Taman Desa Harmoni", exact=True).click()
                self.page.wait_for_timeout(2000)

                # SAVE ADDRESS POPUP
                self.page.locator("#save").click()
                self.page.wait_for_timeout(5000)

        except Exception as e:

            print(f"Address section skipped: {e}")

        self.page.wait_for_timeout(3000)
        # ---- Garage Types ----#
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.wait_for_timeout(2000)
        self.page.get_by_role("option", name="Public Road").click()
        self.page.wait_for_timeout(2000)
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.wait_for_timeout(2000)
        self.page.get_by_role("option", name="No Alarm(WITHOUT MECHANICAL").click()
        self.page.wait_for_timeout(2000)
        self.page.locator(".mat-select-placeholder").click()
        self.page.wait_for_timeout(2000)
        self.page.get_by_role("option", name="Driver’s Side Airbags (1)").click()
        self.page.wait_for_timeout(2000)


        # ---- DECLARATION STATEMENTS ----#
        self.page.get_by_text("We respect your privacy and").click()
        self.page.get_by_text("I hereby confirm that I have").click()
        self.page.wait_for_timeout(10000)

        if self.page.get_by_role("button", name="Generate Quote").is_visible():
            self.page.get_by_role("button", name="Generate Quote").click()
            self.page.get_by_role("button", name="Submit").click()
        else:
            pass

            # get Quote Number
            quote_text = self.page.locator("text=Quote Reference #").locator("xpath=following-sibling::*").inner_text()

            quote_number = quote_text.strip()

            #print(f"Quote Number : {quote_number}")

        self.page.wait_for_timeout(5000)

        # Get Quote Number
        quote_number = self.get_quote_number()

        # Check NSTP / STP
        tpm_button = self.page.get_by_role("button", name="Submit for TPM Staff Approval")

        try:
            tpm_button.wait_for(state="visible", timeout=5000)
            is_nstp = True

        except:
            is_nstp = False

        # ==========================
        # NSTP FLOW
        # ==========================
        if is_nstp:

            print("NSTP Case Detected")

            # Upload Later (Optional)
            try:

                upload_later = self.page.locator(
                    "#isUploadLater-desktop .mat-checkbox-inner-container"
                )

                if upload_later.count() > 0:
                    upload_later.click(force=True)

                    self.page.wait_for_timeout(2000)

                    print("Upload Later Checked")

                    try:

                        remarks = self.page.locator("dx-evidence-upload input")

                        if remarks.is_visible(): remarks.fill("Will Upload Later")

                    except:
                        pass

                    print("Upload Later selected")

                else:

                    print("Upload Later checkbox not displayed")

            except Exception as e:

                print(f"Upload Later skipped : {e}")

            # Submit for TPM Approval
            tpm_button.click()

            self.page.wait_for_timeout(15000)

            # ==========================
            # Branch Manager Approval
            # ==========================
            browser = self.page.context.browser

            manager_context = browser.new_context()

            manager_page = manager_context.new_page()

            manager_page.goto(f"https://agent-uat.tuneinsurance.com/#/qms/quote/motor/reg/cover-details?edit=true&quoteNr={quote_number}")

            manager_page.get_by_role("textbox", name="Username or email").fill("rahul@serole.com")

            manager_page.get_by_role("textbox", name="Password").fill("Serole@123")

            manager_page.get_by_role("button", name="Login").click()

            manager_page.wait_for_timeout(30000)

            manager_page.get_by_role("button", name="Accept & Process").click()

            manager_page.wait_for_timeout(10000)

            manager_page.close()

            # Back to Agent Session
            self.page.reload()

            self.page.wait_for_load_state("networkidle")

        # ==========================
        # STP FLOW
        # ==========================
        else:

            print("STP Case Detected")

        # ==========================
        # COMMON FLOW
        # ==========================
        self.page.get_by_role("button", name="Proceed to Policy Issuance").click()

        self.page.wait_for_timeout(5000)

        self.page.get_by_role("button", name="Issue Policy").click()

        self.page.wait_for_timeout(30000)

        self.page.get_by_role("button", name="Download & e-mail Policy").click()

        self.page.wait_for_timeout(5000)

        self.page.get_by_role("button", name="Submit").click()

        self.page.wait_for_timeout(15000)

    def get_quote_number(self):

        quote_number = (self.page.locator("text=Quote Reference #").locator("xpath=following-sibling::*").inner_text().strip())

        return quote_number

    def get_policy_number(self):

        policy_text = self.page.locator("text=Policy #:").text_content()

        policy_number = (policy_text.replace("Policy #:", "").strip())

        return policy_number