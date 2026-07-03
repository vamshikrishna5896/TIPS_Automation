import allure
import os
from datetime import datetime
from TIPS_utils.date_picker import DatePicker
from TIPS_utils.policy_summary import PolicySummary
from TIPS_Pages.extensions_PC_MC_CV import MCExtensions

class MotorMCPage:

    def __init__(self,page):
        self.page = page

   #@allure.step("Create Motor Policy")
    def create_motor_mc_policy(self,reg_no,mykad,customer_name, date_type):

        # --------------Motor Product ----------------- #
        self.page.get_by_role("heading",name="Motor").click()

        self.page.get_by_role("button",name="Next").click()
        self.page.wait_for_timeout(2000)

        # ------------ Vehicle Number  ----------------- #
        self.page.get_by_role("textbox").fill(reg_no)

        # --------------State ----------------#
        self.page.locator(".mat-select-placeholder").click()
        self.page.get_by_role("option",name="Kedah").click()

        # ----------Click on vehicle search button ------------#
        self.page.get_by_role("button",name="search Vehicle Search").click()

        try:
            self.page.get_by_role("button",name="Save Vehicle Info").click()
        except:
            print("Save Vehicle Info button not found")

            # ---- COVERAGE TYPE (read default) ----
            self.page.wait_for_timeout(5000)
            selected_coverage = self.page.locator("#mat-select-value-9").inner_text().strip()
            print("Default Coverage type: ", selected_coverage)

            # # ---- COVERAGE TYPE ----
            # self.page.locator("#mat-select-value-9").click()
            # self.page.get_by_role("option", name="Comprehensive").click()

            # ------Inception Date Calendar---------#
            self.page.locator("mat-form-field").filter(has_text="Inception Date").get_by_label("Open calendar").click()
            self.page.wait_for_timeout(1000)
            # Select Date
            DatePicker.select_date(self.page, date_type)
            # self.page.pause()

            # === Print of Selected Coverage =====#
            selected_coverage = self.page.locator("#mat-select-value-9").inner_text().strip()
            print("Selected Coverage type: ", selected_coverage)

            # Save on self so it can be written to Excel column C later
            self.selected_coverage = selected_coverage

            # ===========================#
            # Extensions selection
            # #=========================#
            # if selected_coverage == "Comprehensive":
            #     MCExtensions.comprehensive_extension(self.page)
            # elif selected_coverage == "Third Party":
            #     MCExtensions.third_party_extension(self.page)

            #
            # =====================================================
            # Sum Insured
            # =====================================================
            # sum_insured_field = (self.page.locator("mat-form-field").filter(has_text="Vehicle Sum Insured").locator("#sumInsured"))
            #
            # current_value = sum_insured_field.input_value()
            # current_value = current_value.replace(",", "").strip()
            #
            # try:
            #     current_sum = float(current_value)
            #
            #     if current_sum < 5000:
            #         sum_insured_field.click()
            #         sum_insured_field.press("Control+A")
            #         sum_insured_field.fill("5000")
            #         sum_insured_field.press("Tab")
            #
            #         print("Sum Insured updated to 5000")
            #
            #     else:
            #         print(f"Sum Insured is {current_sum}, no update required")
            #
            # except Exception:
            #     sum_insured_field.click()
            #     sum_insured_field.fill("5000")
            #     sum_insured_field.press("Tab")
            #
            #     print("Sum Insured was empty. Updated to 5000")
            #
            #     self.page.wait_for_timeout(3000)


            # --------------- MyKad ------------#
            self.page.locator("mat-form-field").filter(has_text="ID #").locator("#id").fill(mykad)

            # ---------- Name --------
            self.page.locator("mat-form-field").filter(has_text="Name as per ID").locator("#legalName").fill(
                customer_name)

            # Validate button
            self.page.get_by_role("button", name="search Validate Owner as per").click()
            self.page.wait_for_timeout(3000)

            # Save & next button
            self.page.get_by_role("button", name="Save & Next").click()
            self.page.wait_for_timeout(5000)

            # ===========Driver experience   Details ============#
            self.page.locator(".mat-select-placeholder").first.click()
            self.page.locator(".item").first.click()

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

            # ------ Policy Holder Name -------
            ph_name = self.page.locator(".qms-canvas-card-title-wrapper .heading-6").first.inner_text().strip()
            print("Policy Holder name:", ph_name)

            self.ph_name = ph_name

            # ---- DECLARATION STATEMENTS ----#
            self.page.get_by_text("We respect your privacy and").click()
            self.page.get_by_text("I hereby confirm that I have").click()
            self.page.wait_for_timeout(2000)

            # =====================================================
            # "Upload Supporting documents later" checkbox
            # BEFORE Generate Quote is clicked.
            # =====================================================
            try:
                upload_later = self.page.get_by_text("Upload Supporting documents later").locator(
                    "xpath=preceding-sibling::*[1]"
                )

                if upload_later.count() == 0:
                    upload_later = self.page.locator("#isUploadLater-desktop input[type='checkbox']")

                if upload_later.count() > 0 and upload_later.is_visible():
                    upload_later.check(force=True)
                    self.page.wait_for_timeout(1000)

                    if upload_later.is_checked():
                        print("Upload Supporting documents later - Checked")

                        try:
                            remarks_box = self.page.locator("dx-evidence-upload").get_by_role("textbox")
                            remarks_box.wait_for(state="visible", timeout=5000)
                            remarks_box.fill("Will Upload later")
                            print("Remarks comment filled")
                        except Exception as e:
                            print(f"Remarks comment box not found/skipped: {e}")

                    else:
                        print("Warning: checkbox click did not register")
                else:
                    print("Upload Supporting documents later checkbox not displayed")

            except Exception as e:
                print(f"Upload Later checkbox skipped: {e}")

            self.page.wait_for_timeout(2000)

            # ---- GENERATE QUOTE ----#
            if self.page.get_by_role("button", name="Generate Quote").is_visible():
                self.page.get_by_role("button", name="Generate Quote").click()
                with self.page.expect_download() as download_info:
                    self.page.get_by_role("button", name="Submit").click()
                download = download_info.value
                download.save_as(os.path.join(r"Documents\PA_quote.pdf"))
                # self.page.get_by_text("close", exact=True).click()
                print("Quote PDF Generated successfully")

            else:
                pass

            self.page.wait_for_timeout(5000)

            # Get Quote Number from PolicySummary
            quote_number = (
                self.page.locator("text=Quote Reference #").locator("xpath=following-sibling::*").inner_text().strip())

            # ==========================
            # Check NSTP / STP
            # ==========================
            tpm_button = self.page.get_by_role("button", name="Submit for TPM Staff Approval")

            try:
                tpm_button.wait_for(state="visible", timeout=10000)
                is_nstp = True
            except Exception:
                is_nstp = False

            # ==========================
            # NSTP FLOW
            # ==========================
            if is_nstp:

                print("NSTP Case Detected")

                tpm_button.click()
                self.page.wait_for_timeout(15000)

                # ==========================
                # Branch Manager Approval
                # ==========================
                browser = self.page.context.browser
                manager_context = browser.new_context()
                manager_page = manager_context.new_page()

                manager_page.goto(
                    f"https://agent-uat.tuneinsurance.com/#/qms/quote/motor/reg/cover-details?edit=true&quoteNr={quote_number}")

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
                self.page.wait_for_timeout(5000)

                # =====================================================
                # After manager approval + reload, for NSTP the
                # "Proceed to Policy Issuance" step is SKIPPED entirely —
                # the page lands directly on "Issue Policy".
                # =====================================================
                print("NSTP post-approval: skipping 'Proceed to Policy Issuance' (not shown after reload)")

            # ==========================
            # STP FLOW
            # ==========================
            else:
                print("STP Case Detected")

            # ==========================
            # COMMON FLOW
            # ==========================
            proceed_button = self.page.get_by_role("button", name="Proceed to Policy Issuance")

            try:
                proceed_button.wait_for(state="visible", timeout=10000)
                proceed_button.click()
                self.page.wait_for_timeout(5000)
                print("Clicked 'Proceed to Policy Issuance'")
            except Exception:
                print("'Proceed to Policy Issuance' not shown (expected for NSTP after manager approval) - skipping")

            self.page.get_by_role("button", name="Issue Policy").click()
            self.page.wait_for_timeout(30000)

            self.page.get_by_role("button", name="Download & e-mail Policy").click()
            self.page.wait_for_timeout(5000)

            with self.page.expect_download() as download_info:
                self.page.get_by_role("button", name="Submit").click()
            download = download_info.value
            download.save_as(os.path.join(r"Documents\PA_policy.pdf"))
            print("Schedule Letter PDF Generated successfully")

            # Wait until Policy Number is displayed

            self.page.locator("text=Policy #:").wait_for(
                state="visible",
                timeout=120000)

            # =============== Read Policy Summary from TIPS=============#
            policy_details = PolicySummary.get_policy_summary(self.page)

            policy_details["Selected Coverage"] = self.selected_coverage
            policy_details["Policy Holder"] = self.ph_name

            return policy_details