import allure
from datetime import datetime, timedelta
from TIPS_utils.date_picker import DatePicker

class CVPolicyPage:

    def __init__(self, page):
        self.page = page

    #@allure.step("Create Commercial Vehicle Policy")
    def create_cv_policy(self, reg_no, business_reg_no, customer_name, date_type, carryingcapacity, approval_type):

        # =============================== PRODUCT SELECTION===============================#
        self.page.get_by_role("heading",name="Motor").click()
        self.page.get_by_role("heading", name="Reg. Commercial Vehicle").click()

        self.page.get_by_role("button", name="Next").click()

        self.page.wait_for_timeout(3000)

        # ============================ VEHICLE DETAILS ===============================#

        self.page.get_by_role("textbox").first.fill(reg_no)

        print(f"Registration No : {reg_no}"); self.page.locator(".mat-select-placeholder").click()
        # State
        self.page.get_by_role("option", name="Kedah").click()
        # vehicle search
        self.page.get_by_role("button", name="search Vehicle Search").click()

        self.page.wait_for_timeout(5000)
        # vehicle type
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.get_by_role("option", name="Commercial Vehicle").click()
        # vehicle class
        self.page.locator(".mat-select-placeholder").first.click()
        self.page.get_by_role("option", name="C permit").click()

        # Engine No
        self.page.locator("mat-form-field").filter(has_text="Engine # *").locator("#engineNo").click()
        self.page.locator("mat-form-field").filter(has_text="Engine # *").locator("#engineNo").fill("45621388")
        # Chassis No
        self.page.locator("mat-form-field").filter(has_text="Chassis # *").locator("#chassisNo").click()
        self.page.locator("mat-form-field").filter(has_text="Chassis # *").locator("#chassisNo").fill("84562125555")

        # Make
        self.page.locator(".mat-select-placeholder").nth(2).click()
        self.page.get_by_role("option", name="VOLVO").click()
        self.page.wait_for_timeout(1000)
        #self.page.pause()
        # Model
        self.page.locator(".mat-select-placeholder.mat-select-min-line.ng-tns-c176-72").click()
        self.page.get_by_role("option", name="F16").click()

        self.page.wait_for_timeout(2000)

        # Year
        self.page.locator(".mat-select-placeholder.mat-select-min-line.ng-tns-c176-74").click()
        self.page.get_by_role("option", name="2023").click()

        self.page.wait_for_timeout(2000)

        # Variant
        self.page.locator(".mat-select-placeholder.mat-select-min-line.ng-tns-c176-76").click()
        self.page.get_by_role("option", name="NA").click()
        self.page.wait_for_timeout(1000)

        # seating capacity
        self.page.locator("mat-form-field").filter(has_text="Seating Capacity *").locator("#seatCapacity").click()
        self.page.locator("mat-form-field").filter(has_text="Seating Capacity *").locator("#seatCapacity").fill("5")

        # Carrying capacity
        self.page.locator("mat-form-field").filter(has_text="Carrying Capacity *").locator("#carryingCapacity").click()
        self.page.locator("mat-form-field").filter(has_text="Carrying Capacity *").locator("#carryingCapacity").fill(carryingcapacity)
        self.page.wait_for_timeout(1000)
        # KG
        self.page.locator(".mat-select-placeholder.mat-select-min-line.ng-tns-c176-84").click()
        self.page.get_by_role("option", name="Kg").click()

        # Vehicle Use
        self.page.locator(".mat-select-placeholder.mat-select-min-line.ng-tns-c176-86").click()
        self.page.get_by_role("option", name="General Cargo").click()

        self.page.get_by_role("button", name="Save Vehicle Info").click()

        self.page.wait_for_timeout(5000)

        # =============================== COVER DETAILS  =============================== #

        # ------Inception Date Calendar---------#
        self.page.locator("mat-form-field").filter(has_text="Inception Date").get_by_label("Open calendar").click()
        self.page.wait_for_timeout(1000)
        # Select Date
        DatePicker.select_date(self.page, date_type)

        self.page.wait_for_timeout(2000)

        self.page.get_by_role("region", name="Coverage").locator("input[type='text']").fill("25000")

        self.page.locator("mat-form-field").filter(has_text="Business Registration # *").locator("#id").fill(business_reg_no)
        #self.page.locator("#id").fill(business_reg_no)

        print(f"Business Reg No : {business_reg_no}")
        self.page.locator("dx-input").filter(has_text="* Name as per ID / Legal Name").locator("#legalName").fill(customer_name)
        #self.page.locator("#legalName").fill(customer_name)

        print(f"Customer Name : {customer_name}")

        self.page.get_by_role("button", name="search Validate Owner as per").click()

        self.page.wait_for_timeout(5000)

        self.page.get_by_role("button", name="Save & Next").click()

        self.page.wait_for_timeout(5000)

        # =============================== PROPOSER DETAILS =============================== #
        # ====================================
        # CHECK YES / ADD / EDIT BUTTON
        # ====================================

        popup_found = False

        # Yes Button
        try:
            self.page.get_by_role("button", name="Yes").click()
            # yes_button = self.page.get_by_role("button", name="Yes").first
            # yes_button.wait_for(state="visible", timeout=5000)
            # yes_button.click()
            self.page.wait_for_timeout(5000)

            popup_found = True
            print("Yes button clicked")

        except:
            print("Yes button not visible")

        # ====================================
        # IF NO POPUP FOUND → FILL PROPOSER DETAILS
        # ====================================

        if not popup_found:

            print("No Yes/Add/Edit popup found. Filling proposer details.")

            #State
            self.page.locator(".mat-select-placeholder").first.click()
            self.page.get_by_role("option", name="Kedah").click()

            self.page.wait_for_timeout(2000)
            # Postcode
            self.page.locator(".mat-select-placeholder").click()
            self.page.get_by_role("option", name="05500").click()

            self.page.wait_for_timeout(2000)

            # Address Line
            self.page.get_by_role("combobox", name="Address Line").click()
            self.page.get_by_text("DYMM Sultan Kedah").click()

            self.page.wait_for_timeout(2000)

            self.page.wait_for_timeout(1000)

            # Save button if available
            try:
                save_btn = self.page.get_by_role("button", name="Save")
                if save_btn.is_visible():
                    save_btn.click()
                    print("Address saved")
            except:
                pass

        else:
            print("Existing proposer details found. Skipping proposer details entry.")

        # Declaration Checkbox
        self.page.get_by_text("We respect your privacy and").click()
        self.page.get_by_text("I hereby confirm that I have").click()

        # get Quote Number
        quote_text = self.page.locator("text=Quote Reference #").locator("xpath=following-sibling::*").inner_text()

        quote_number = quote_text.strip()

        print(f"Quote Number : {quote_number}")

        # ============= NSTP Flow ==================#
        if approval_type.upper() == "NSTP":

            print("NSTP Flow Started")

            # Upload Later Checkbox
            # self.page.locator("#isUploadLater-desktop > .mat-checkbox-layout > .mat-checkbox-inner-container").click()

            # self.page.locator("dx-evidence-upload").get_by_role("textbox").fill("Will Upload later")

            self.page.get_by_role("button", name="Submit for TPM Staff Approval").click()

            self.page.wait_for_timeout(20000)

            # Manager Approval
            browser = self.page.context.browser

            manager_context = browser.new_context()

            manager_page = manager_context.new_page()

            manager_page.goto(f"https://agent-uat.tuneinsurance.com/#/qms/quote/motor/rcv/cover-details?edit=true&quoteNr={quote_number}")

            manager_page.get_by_role("textbox", name="Username or email").fill("rahul@serole.com")

            manager_page.get_by_role("textbox", name="Password").fill("Serole@123")

            manager_page.get_by_role("button", name="Login").click()

            manager_page.wait_for_timeout(30000)

            manager_page.get_by_role("button", name="Accept & Process").click()
            print("Manager Approved the Quote")

            # self.page.get_by_text("rahul@serole.com", exact=True).click()
            # self.page.wait_for_timeout(1000)
            #
            # self.page.get_by_text("Sign Out", exact=True).click()
            # self.page.wait_for_timeout(2000)

            manager_page.close()

            self.page.wait_for_timeout(10000)

            self.page.reload()

            self.page.wait_for_load_state("networkidle")

            self.page.get_by_role("button", name="Issue Policy").click()

            self.page.wait_for_timeout(18000)

        else:

            print("STP Flow Started")

            self.page.get_by_role("button", name="Generate Quote").click()

            self.page.wait_for_timeout(5000)

            with self.page.expect_download():

                self.page.get_by_role("button", name="Submit").click()

            self.page.wait_for_timeout(5000)

            self.page.get_by_role("button", name="Proceed to Policy Issuance").click()

            self.page.wait_for_timeout(5000)

            self.page.get_by_role("button", name="Issue Policy").click()

            self.page.wait_for_timeout(25000)

    # ====================================
    # GET QUOTE NUMBER
    # ====================================
    def get_quote_number(self):

        quote_number = (self.page.locator("text=Quote Reference #").locator("xpath=following-sibling::*").inner_text().strip())

        print(f"Quote Number : {quote_number}")

        return quote_number
    # ====================================
    # GET POLICY NUMBER
    # ====================================

    def get_policy_number(self):

        self.page.wait_for_selector("text=Policy #:", timeout=120000)

        policy_text = self.page.locator("text=Policy #:").text_content()

        policy_number = (policy_text.replace("Policy #:", "").strip())

        print(f"Policy Number : {policy_number}")

        return policy_number


