from datetime import datetime, timedelta


class DatePicker:

    @staticmethod
    def get_date(option):

        if option.lower() == "today":
            return datetime.today()

        elif option.lower() == "tomorrow":
            return datetime.today() + timedelta(days=1)

        elif option.lower() == "after_5_days":
            return datetime.today() + timedelta(days=5)

        else:
            raise Exception("Invalid date option")

    @staticmethod
    def select_date(page, option):

        required_date = DatePicker.get_date(option)

        day = str(required_date.day)

        print(f"Selecting Day = {day}")

        page.wait_for_timeout(2000)

        page.get_by_role("button",name=day,exact=True).click(force=True)