import re
class PolicySummary:

    @staticmethod
    def motor_policy_summary(page):

        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(3000)

        details = {}


        # ---------------- Quote Number ----------------
        details["Quote Number"] = page.locator("text=Quote Reference #").locator("xpath=following-sibling::*").inner_text().strip()
        print("Quote number:", details["Quote Number"])

        # ---------------- Policy Number ----------------
        details["Policy Number"] = (page.locator("text=Policy #:").text_content().replace("Policy #:", "").strip())
        print("Policy number:", details["Policy Number"])

        # ---------------- Sum Insured ----------------
        sum_insured = page.locator("li").filter(has_text="Vehicle Sum Insured").locator(".summary-result-value").inner_text().strip()
        details["Sum Insured"] = PolicySummary.extract_myr(sum_insured)
        print("Sum Insured:", details["Sum Insured"])

        # ---------------- Act Premium ----------------
        act_prem = page.locator("li").filter(has_text="Act Premium").locator(".summary-result-value").inner_text().strip()
        details["Act Premium"] = PolicySummary.extract_myr(act_prem)
        print("Act prem:", details["Act Premium"])

        # ---------------- Basic Premium ----------------
        basic_prem = page.locator("li").filter(has_text="Basic Premium").locator(".summary-result-value").inner_text().strip()
        details["Basic Premium"] = PolicySummary.extract_myr(basic_prem)
        print("Basic Premium:", details["Basic Premium"])

        # ---------------- NCD ----------------
        ncd = page.locator("(//li[contains(.,'NCD')]//span[contains(@class,'summary-result-value')])[1]").inner_text().strip()
        details["NCD"] = PolicySummary.extract_myr(ncd)
        print("NCD:", details["NCD"])

        # ---------------- Premium After NCD ----------------
        prem_after_ncd = page.locator("li").filter(has_text="Premium after NCD").locator(".summary-result-value").inner_text().strip()
        details["Premium after NCD"] = PolicySummary.extract_myr(prem_after_ncd)
        print("Premium after NCD:", details["Premium after NCD"])

        # ---------------- Gross Premium ----------------
        gross_prem = page.locator("li").filter(has_text="Gross Premium").locator(".summary-result-value").inner_text().strip()
        details["Gross Premium"] = PolicySummary.extract_myr(gross_prem)
        print("Gross Premium:", details["Gross Premium"])

        # ---------------- SST ----------------
        sst = page.locator("li").filter(has_text="SST").locator(".summary-result-value").inner_text().strip()
        details["SST"] = PolicySummary.extract_myr(sst)
        print("SST:", details["SST"])

        # ---------------- Stamp Duty ----------------
        stamp_duty = (page.locator("li").filter(has_text="Stamp Duty").locator(".summary-result-value").inner_text().strip())
        details["Stamp Duty"] = PolicySummary.extract_myr(stamp_duty)
        print("Stamp Duty:",details["Stamp Duty"])

        # ---------------- Total Premium ----------------
        total_prem = page.locator("div").filter(has_text="Total Payable Premium").locator(".final-amount").inner_text().strip()
        details["Total Premium"] = PolicySummary.extract_myr(total_prem)
        print("Total Premium:",details["Total Premium"])

        return details

    @staticmethod
    def extract_myr(text: str) -> float:
        is_negative = "-" in text
        match = re.search(r"[\d,]+\.?\d*", text)
        value = float(match.group().replace(",", "")) if match else 0.0
        value = round(value, 2)  #
        return -value if is_negative else value

    @staticmethod
    def pa_policy_summary(page):

        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(3000)

        details = {}

        # ---------------- Quote Number ----------------
        details["Quote Number"] = page.locator("text=Quote Reference #").locator(
            "xpath=following-sibling::*").inner_text().strip()
        print("Quote number:", details["Quote Number"])


        # ---------------- PA Policy Number ----------------#
        page.locator("text=Policy #:").wait_for(state="visible", timeout=60000)
        policy_text = page.locator("text=Policy #:").text_content()
        details["Policy Number"] = policy_text.replace("Policy #:", "").strip()
        print("Policy Number:", details["Policy Number"])
       # ----------------  Dental Policy Number ----------------#
       #  details["Policy Number"] = page.locator("text=Policy #").locator(
       #      "xpath=following::span[contains(@class,'ng-star-inserted')][1]").inner_text().strip()
       #  print("Policy number:", details["Policy Number"])

        # ---------------- Sum Insured ----------------
        sum_insured = page.locator("li").filter(has_text="Sum Insured").locator(".summary-result-value").inner_text().strip()
        details["Sum Insured"] = PolicySummary.extract_myr(sum_insured)
        print("Sum Insured:", details["Sum Insured"])

        # ---------------- Gross Premium ----------------
        gross_prem = page.locator("li").filter(has_text="Gross Premium").locator(
            ".summary-result-value").inner_text().strip()
        details["Gross Premium"] = PolicySummary.extract_myr(gross_prem)
        print("Gross Premium:", details["Gross Premium"])

        # ---------------- SST ----------------
        sst = page.locator("li").filter(has_text="SST").locator(".summary-result-value").inner_text().strip()
        details["SST"] = PolicySummary.extract_myr(sst)
        print("SST:", details["SST"])

        # ---------------- Stamp Duty ----------------
        stamp_duty = (
            page.locator("li").filter(has_text="Stamp Duty").locator(".summary-result-value").inner_text().strip())
        details["Stamp Duty"] = PolicySummary.extract_myr(stamp_duty)
        print("Stamp Duty:", details["Stamp Duty"])

        # ---------------- Total Premium ----------------
        total_prem = page.locator("div").filter(has_text="Total Payable Premium").locator(
            ".final-amount").inner_text().strip()
        details["Total Premium"] = PolicySummary.extract_myr(total_prem)
        print("Total Premium:", details["Total Premium"])

        return details

    @staticmethod
    def dental_policy_summary(page):
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(3000)

        details = {}

        # ---------------- Quote Number ----------------
        details["Quote Number"] = page.locator("text=Quote Reference #").locator(
            "xpath=following-sibling::*").inner_text().strip()
        print("Quote number:", details["Quote Number"])


        #----------------  Dental Policy Number ----------------#
        details["Policy Number"] = page.locator("text=Policy #").locator(
             "xpath=following::span[contains(@class,'ng-star-inserted')][1]").inner_text().strip()
        print("Policy number:", details["Policy Number"])

        # ---------------- Gross Premium ----------------
        gross_prem = page.locator("li").filter(has_text="Gross Premium").locator(
            ".summary-result-value").inner_text().strip()
        details["Gross Premium"] = PolicySummary.extract_myr(gross_prem)
        print("Gross Premium:", details["Gross Premium"])

        # ---------------- SST ----------------
        sst = page.locator("li").filter(has_text="SST").locator(".summary-result-value").inner_text().strip()
        details["SST"] = PolicySummary.extract_myr(sst)
        print("SST:", details["SST"])

        # ---------------- Stamp Duty ----------------
        stamp_duty = (
            page.locator("li").filter(has_text="Stamp Duty").locator(".summary-result-value").inner_text().strip())
        details["Stamp Duty"] = PolicySummary.extract_myr(stamp_duty)
        print("Stamp Duty:", details["Stamp Duty"])

        # ---------------- Total Premium ----------------
        total_prem = page.locator("div").filter(has_text="Total Payable Premium").locator(
            ".final-amount").inner_text().strip()
        details["Total Premium"] = PolicySummary.extract_myr(total_prem)
        print("Total Premium:", details["Total Premium"])

        return details