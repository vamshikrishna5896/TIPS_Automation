from datetime import datetime, timedelta


class DatePicker:

    @staticmethod
    def get_date(option):

        option = str(option).strip().lower()

        if option == "today":
            return datetime.today()

        elif option == "tomorrow":
            return datetime.today() + timedelta(days=1)

        elif option == "day_after_tomorrow":
            return datetime.today() + timedelta(days=2)

        # DD.MM.YYYY (e.g. 20.08.2025)
        try:
            return datetime.strptime(option, "%d.%m.%Y")
        except ValueError:
            pass

        # YYYY-MM-DD (e.g. 2025-08-20)
        try:
            return datetime.strptime(option, "%Y-%m-%d")
        except ValueError:
            pass

        raise Exception(f"Invalid date option: {option}")

    @staticmethod
    def select_date(frame, option="today"):

        target_date = DatePicker.get_date(option)

        # SAP's own calendar field uses DD.MM.YYYY, e.g. "20.08.2025"
        formatted_date = target_date.strftime("%d.%m.%Y")

        #print(f"SAP Date -> typing: {formatted_date}")

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
