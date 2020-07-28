
import datetime
from App.BackEnd.Exceptions import UnprocessableEntityException
from typing import NoReturn


class Date:

    _date: datetime.date

    def __init__(self, day: str, month: str, year: str):
        self.set_date(day, month, year)
        self.check_is_future_date()

    def set_date(self, day: str, month: str, year: str) -> NoReturn:
        try:
            self._date = datetime.date(int(year), int(month), int(day))

        except ValueError:
            raise UnprocessableEntityException("Invalid Date")

    def get_date(self):
        return self._date

    def check_is_future_date(self) -> NoReturn:
        actual_date = datetime.date.today()

        if self._date > actual_date:
            raise UnprocessableEntityException("Invalid Date")
