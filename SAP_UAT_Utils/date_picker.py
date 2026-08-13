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

        # DD.MM.YYYY (e.g. 25.07.2025)
        try:
            return datetime.strptime(option, "%d.%m.%Y")
        except ValueError:
            pass

        # YYYY-MM-DD (e.g. 2025-07-25)
        try:
            return datetime.strptime(option, "%Y-%m-%d")
        except ValueError:
            pass

        raise Exception(f"Invalid date option: {option}")

    # ---- Step 2: click the matching day on the SAP calendar ----
    @staticmethod
    def select_date(frame, option="today"):

        target_date = DatePicker.get_date(option)

        # Build the label exactly the way SAP writes it, e.g. "July 2026 15 Wednesday Week"
        month_and_year = target_date.strftime("%B %Y")   # "July 2026"
        day_number = target_date.day                     # 15 (no leading zero)
        weekday_name = target_date.strftime("%A")         # "Wednesday"

        day_label = f"{month_and_year} {day_number} {weekday_name}"

        print(f"SAP Date -> selecting: {day_label}")

        date_cell = frame.get_by_label(day_label).first
        date_cell.click()