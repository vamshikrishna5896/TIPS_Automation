from datetime import datetime, timedelta

class DatePicker:

    # ---- Step 1: turn a simple word into a real date ----
    @staticmethod
    def get_date(option):

        option = option.lower()

        if option == "today":
            return datetime.today()

        elif option == "tomorrow":
            return datetime.today() + timedelta(days=1)

        elif option == "day_after_tomorrow":
            return datetime.today() + timedelta(days=2)

        else:
            raise Exception(f"Invalid date option: {option}")

    # ---- Step 2: click the matching day on the SAP calendar ----
    @staticmethod
    def select_date(frame, option="today"):

        target_date = DatePicker.get_date(option)

        # Build the label exactly the way SAP writes it, e.g. "July 2026 15 Wednesday Week"
        month_and_year = target_date.strftime("%B %Y")   # "July 2026"
        day_number = target_date.day                     # 15 (no leading zero)
        weekday_name = target_date.strftime("%A")         # "Wednesday"

        day_label = f"{month_and_year} {day_number} {weekday_name} Week"

        print(f"SAP Date -> selecting: {day_label}")

        frame.get_by_label(day_label).get_by_text(str(day_number), exact=True).click()