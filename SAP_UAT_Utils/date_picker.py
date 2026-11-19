from datetime import datetime, timedelta


class DatePicker:

    # ------------------------------------------------------------------
    # CHANGE THE DATE HERE.
    # This is the single place that controls which date gets typed into
    # SAP for every product (PC, MC, BI, PA ...), as long as the test does
    # not pass its own date_type.
    #
    # Accepted values:
    #   "today", "tomorrow", "day_after_tomorrow"
    #   "DD.MM.YYYY"  (e.g. "20.11.2025")
    #   "YYYY-MM-DD"  (e.g. "2025-11-20")
    # ------------------------------------------------------------------
    DEFAULT_DATE = "today"

    @staticmethod
    def get_date(option=None):

        # Nothing was passed by the caller -> use the date configured above
        if option is None:
            option = DatePicker.DEFAULT_DATE

        option = str(option).strip().lower()

        if option == "today":
            return datetime.today()

        elif option == "tomorrow":
            return datetime.today() + timedelta(days=1)

        elif option == "day_after_tomorrow":
            return datetime.today() + timedelta(days=2)

        # DD.MM.YYYY (e.g. 20.11.2025)
        try:
            return datetime.strptime(option, "%d.%m.%Y")
        except ValueError:
            pass

        # YYYY-MM-DD (e.g. 2025-11-20)
        try:
            return datetime.strptime(option, "%Y-%m-%d")
        except ValueError:
            pass

        raise Exception(f"Invalid date option: {option}")

    @staticmethod
    def select_date(frame, option=None):

        # option=None -> DatePicker.DEFAULT_DATE is used
        target_date = DatePicker.get_date(option)

        # SAP's own calendar field uses DD.MM.YYYY, e.g. "20.11.2025"
        formatted_date = target_date.strftime("%d.%m.%Y")

        calendar_dialog = frame.get_by_role("dialog", name="Calendar")
        date_input = calendar_dialog.locator("input").first

        date_input.click()
        date_input.fill(formatted_date)   # fill() clears the old value and types the new one

        date_input.press("Enter")

        try:
            calendar_dialog.wait_for(state="hidden", timeout=10_000)
        except Exception:
            pass

        print(f"SAP Date -> selected: {formatted_date}")