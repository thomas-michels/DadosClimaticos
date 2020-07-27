
from App.Date import Date
from App.Exceptions import UnprocessableEntityException
from App.Date import Date


class DateManager:

    _days_list = []

    def __init__(self, initial_date: Date, final_date: Date):
        self._initial_date = initial_date
        self._final_date = final_date
        self._check_dates()
        self._generate_days_list()

    def _check_dates(self):
        if self._initial_date.get_date() > self._final_date.get_date():
            raise UnprocessableEntityException()

    def _get_difference_days(self):

        difference_days = 0

        if self._initial_date.get_date().month == self._final_date.get_date().month:
            difference_days = self._final_date.get_date().day - self._initial_date.get_date().day

        elif self._initial_date.get_date().month != self._final_date.get_date().month:
            pass

        return difference_days

    def _generate_days_list(self):

        if self._initial_date.get_date().month == self._final_date.get_date().month and\
                self._initial_date.get_date().year == self._final_date.get_date().year:

            day = self._final_date.get_date().day

            while day != (self._initial_date.get_date().day - 1):
                self._days_list.append(Date(day, self._final_date.get_date().month, self._final_date.get_date().year))
                day -= 1

        elif self._initial_date.get_date().month != self._final_date.get_date().month and\
                self._initial_date.get_date().year == self._final_date.get_date().year:
            pass

        else:
            raise UnprocessableEntityException("Over a very big period")