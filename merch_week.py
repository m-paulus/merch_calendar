import merch_calendar
from datetime import date, timedelta
import calendar


class MerchWeek:
    def __init__(self, year, month, week):
        try:
            self._date = merch_calendar.start_of_week(year, month, week)
        except:
            raise

    @classmethod
    def from_date(cls, date):
        year = merch_calendar.year(date)
        month = merch_calendar.month(date)
        week = merch_calendar.week_of_month(date)
        return cls(year, month, week)

    @classmethod
    def from_year_week(cls, year, week):
        if week < 1 or week > merch_calendar.weeks_in_year(year):
            raise ValueError('Week number out of range')
        return cls(year, 1, week)

    @property
    def year(self):
        return merch_calendar.year(self._date)

    @property
    def month(self):
        return merch_calendar.month(self._date)

    @property
    def week_of_month(self):
        return merch_calendar.week_of_month(self._date)

    @property
    def week_of_year(self):
        return merch_calendar.week_of_year(self._date)

    @property
    def month_abbr(self):
        return calendar.month_abbr[merch_calendar.to_julian_month(self.month)]

    @property
    def month_name(self):
        return calendar.month_name[merch_calendar.to_julian_month(self.month)]

    @property
    def start_date(self):
        return self._date

    @property
    def end_date(self):
        return self._date + timedelta(6)

    def __repr__(self):
        return "<MerchWeek: "+str(self.year)+" WK"+"{n:02d}".format(n=self.week_of_year)+">"
