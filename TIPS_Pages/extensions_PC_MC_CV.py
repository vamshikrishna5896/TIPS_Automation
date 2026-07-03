# =====================================================
# PC Motor Extensions Class
# Handles Extension Coverage for Private Car (PC) only:
#   - Comprehensive
#   - TP Fire & Theft (TPFT)
#   - Third Party → No extensions (not handled here)
#   PCExtensions.comprehensive_extension(page)
#   PCExtensions.tpft_extension(page)
# =====================================================

class PCExtensions:

    # =====================================================
    # Comprehensive Extensions
    # Call: PCExtensions.comprehensive_extension(page)
    # =====================================================
    @staticmethod
    def comprehensive_extension(page):

        print("Executing PC Comprehensive Extensions")

        # Open Extension Coverage panel
        page.get_by_role("button", name="Extension Coverage").click()

        # Select Motor Shield package
        page.locator("#mat-select-value-11").click()
        page.get_by_text("Motor Shield").click()

        # Check first extension and fill Sum Insured
        page.get_by_role("button", name="check").nth(1).click()
        page.locator("mat-form-field").filter(has_text="Sum Insured *MYR").locator("#sumInsured").fill("5000")

        # Select 7th child extension
        page.locator(
            "div:nth-child(7) > .additional-benefit > .additional-benefit-wrapper > .additional-benefit-label > div > .material-icons"
        ).click()

        # Fill Sum Insured for that extension
        page.locator("#sumInsured").nth(5).fill("6000")

        # Check second extension
        page.get_by_role("button", name="check").nth(2).click()

        # Select radio option
        page.locator(".mat-radio-outer-circle").first.click()

        # Check fourth extension
        page.get_by_role("button", name="check").nth(4).click()

        print("PC Comprehensive Extensions Done")

    # =====================================================
    # TP Fire & Theft Extensions
    # Call: PCExtensions.tpft_extension(page)
    # =====================================================
    @staticmethod
    def tpft_extension(page):

        print("Executing PC TPFT Extensions")

        # Open Extension Coverage panel
        page.get_by_role("button", name="Extension Coverage").click()

        # Select Autobuddy package
        page.locator("#mat-select-value-11").click()
        page.get_by_text("Autobuddy").click()

        # Select Plan B
        page.locator(".mat-select-placeholder").first.click()
        page.get_by_text("PLAN B").click()

        # Select Extension to Kalimantan
        page.get_by_text("Extension to Kalimantan and").click()

        print("PC TPFT Extensions Done")


# =====================================================
# MC Motor Extensions Class
# Handles Extension Coverage for Motorcycle (MC) only:
#   - Comprehensive
#   - Third Party
#   MCExtensions.comprehensive_extension(page)
#   MCExtensions.third_party_extension(page)
# =====================================================

class MCExtensions:

    # =====================================================
    # Comprehensive Extensions
    # Call: MCExtensions.comprehensive_extension(page)
    # =====================================================
    @staticmethod
    def comprehensive_extension(page):

        print("Executing MC Comprehensive Extensions")

        # Open Extension Coverage panel
        page.get_by_role("button", name="Extension Coverage").click()

        # --- Package Type Selection ----
        page.get_by_text("NAPackage Type").click()
        page.wait_for_timeout(1000)
        page.get_by_role("option", name="Motorcyclist PA").click()
        page.wait_for_timeout(1000)

        selected_package = page.locator("#mat-select-value-11 span.mat-select-min-line").inner_text()
        print("Selected Package:", selected_package)

        if "Motorcyclist PA" in selected_package:
            page.locator(".mat-select-placeholder").first.click()
            page.get_by_role("option", name="PLAN A").click()
            print("Plan Type: PLAN A")
        else:
            print("Motorcyclist PA not selected → skipping PLAN selection")

        # ---- Extensions ----
        extensions = [
            "All Riders",
            "Inclusion of Special Perils",
            "Legal Liability to Pillion",
            "Accessories fixed to motorcycle",
            "Ferry Transit to and / or from Sabah and Labuan",
            "Strike Riot and Civil Commotion",
        ]

        for extension_name in extensions:
            page.locator("span").filter(has_text=extension_name).get_by_role("button").click()

            if extension_name == "Accessories fixed to motorcycle":
                container = page.locator(".additional-benefit-wrapper").filter(has_text=extension_name)
                container.locator("input#sumInsured").fill("800")

            print(f"{extension_name} selected successfully")

        print("MC Comprehensive Extensions Done")

    # =====================================================
    # Third Party Extensions
    # Call: MCExtensions.third_party_extension(page)
    # =====================================================
    @staticmethod
    def third_party_extension(page):

        print("Executing MC Third Party Extensions")

        # Open Extension Coverage panel
        page.get_by_role("button", name="Extension Coverage").click()

        # --- Package Type Selection ----
        page.get_by_text("NAPackage Type").click()
        page.wait_for_timeout(1000)
        page.get_by_role("option", name="Motorcyclist PA").click()
        page.wait_for_timeout(1000)

        selected_package = page.locator("#mat-select-value-11 span.mat-select-min-line").inner_text()
        print("Selected Package:", selected_package)

        if "Motorcyclist PA" in selected_package:
            page.locator(".mat-select-placeholder").first.click()
            page.get_by_role("option", name="PLAN A").click()
            print("Plan Type: PLAN A")
        else:
            print("Motorcyclist PA not selected → skipping PLAN selection")

        # ---- Extensions ----
        extensions = [
            "All Riders",
        ]

        for extension_name in extensions:
            page.locator("span").filter(has_text=extension_name).get_by_role("button").click()
            print(f"{extension_name} selected successfully")

        print("MC Third Party Extensions Done")


# =====================================================
# CV Motor Extensions Class
# Handles Extension Coverage for Commercial Vehicle (CV) only:
#   - Comprehensive
#   - TP Fire & Theft (TPFT)
#   - Third Party
#   CVExtensions.comprehensive_extension(page)
#   CVExtensions.tpft_extension(page)
#   CVExtensions.third_party_extension(page)
# =====================================================

class CVExtensions:

    # =====================================================
    # Comprehensive Extensions
    # Call: CVExtensions.comprehensive_extension(page)
    # =====================================================
    @staticmethod
    def comprehensive_extension(page):

        print("Executing CV Comprehensive Extensions")

        # Open Extension Coverage panel
        page.get_by_role("button", name="Extension Coverage").click()

        # --- Package Type Selection ----
        page.get_by_text("NAPackage Type").click()
        page.wait_for_timeout(1000)
        page.get_by_role("option", name="Motorist PA").click()
        page.wait_for_timeout(1000)

        selected_package = page.locator("#mat-select-value-11 span.mat-select-min-line").inner_text()
        print("Selected Package:", selected_package)

        if "Motorist PA" in selected_package:
            page.locator(".mat-select-placeholder").first.click()
            page.get_by_role("option", name="PLAN D").click()
            print("Plan Type: PLAN D")
        else:
            print("Motorist PA not selected → skipping PLAN selection")

        # ---- Extensions ----
        extensions = [
            "Windscreen Damage",
            "Strike riot and civil commotion",
            "Ferry Transit to and / or from Sabah and Labuan",
            "Inclusion of Special Perils",
            "Passenger Risk",
            "Passenger Risk-Employees of the Insured-good carrying vehicle only",
        ]

        for extension_name in extensions:
            page.locator("span").filter(has_text=extension_name).get_by_role("button").click()

            if extension_name == "Windscreen Damage":
                page.locator("mat-form-field").filter(has_text="Sum Insured").locator("#sumInsured").fill("800")

            print(f"{extension_name} selected successfully")

        print("CV Comprehensive Extensions Done")

    # =====================================================
    # TP Fire & Theft Extensions
    # Call: CVExtensions.tpft_extension(page)
    # =====================================================
    @staticmethod
    def tpft_extension(page):

        print("Executing CV TPFT Extensions")

        # Open Extension Coverage panel
        page.get_by_role("button", name="Extension Coverage").click()

        # --- Package Type Selection ----
        page.get_by_text("NAPackage Type").click()
        page.wait_for_timeout(1000)
        page.get_by_role("option", name="Motorist PA").click()
        page.wait_for_timeout(1000)

        selected_package = page.locator("#mat-select-value-11 span.mat-select-min-line").inner_text()
        print("Selected Package:", selected_package)

        if "Motorist PA" in selected_package:
            page.locator(".mat-select-placeholder").first.click()
            page.get_by_role("option", name="PLAN D").click()
            print("Plan Type: PLAN D")
        else:
            print("Motorist PA not selected → skipping PLAN selection")

        # ---- Extensions ----
        extensions = [
            "Passenger Risk",
            "Passenger Risk-Employees of the Insured-good carrying vehicle only",
        ]

        for extension_name in extensions:
            page.locator("span").filter(has_text=extension_name).get_by_role("button").click()
            print(f"{extension_name} selected successfully")

        print("CV TPFT Extensions Done")

    # =====================================================
    # Third Party Extensions
    # Call: CVExtensions.third_party_extension(page)
    # =====================================================
    @staticmethod
    def third_party_extension(page):

        print("Executing CV Third Party Extensions")

        # Open Extension Coverage panel
        page.get_by_role("button", name="Extension Coverage").click()

        # ---- Extensions ----
        extensions = [
            "Passenger Risk",
            "Passenger Risk-Employees of the Insured-good carrying vehicle only",
        ]

        for extension_name in extensions:
            page.locator("span").filter(has_text=extension_name).get_by_role("button").click()
            print(f"{extension_name} selected successfully")

        print("CV Third Party Extensions Done")