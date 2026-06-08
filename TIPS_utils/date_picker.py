from datetime import datetime, timedelta


class DatePicker:

    @staticmethod
    def get_date(option):

        if option.lower() == "today":
            return datetime.today()

        elif option.lower() == "tomorrow":
            return datetime.today() + timedelta(days=1)

        elif option.lower() == "day_after_tomorrow":
            return datetime.today() + timedelta(days=2)

        elif option.lower() == "after_5_days":
            return datetime.today() + timedelta(days=5)

        else:
            raise Exception("Invalid date option")

    @staticmethod
    def select_date(page, option):

        required_date = DatePicker.get_date(option)

        print(f"Selecting Date: {required_date}")

        # Angular Material calendar format
        aria_date = required_date.strftime("%B %d, %Y").replace(" 0", " ")

        print(f"Aria Date: {aria_date}")

        page.wait_for_timeout(2000)

        page.get_by_role("gridcell", name=aria_date).click(force=True)

        print(f"Selected Date: {required_date.strftime('%d-%m-%Y')}")