from datetime import date, timedelta
import math

LAST_MONTH_OF_YEAR = 1
LAST_DAY_OF_YEAR = 31

QUARTER_1 = 1
QUARTER_2 = 2
QUARTER_3 = 3
QUARTER_4 = 4

FOUR_WEEK_MONTHS = [2, 5, 8, 11]
FIVE_WEEK_MONTHS = [3, 6, 9, 12]

def end_of_year(year):
    year_end = date(year+1, LAST_MONTH_OF_YEAR, LAST_DAY_OF_YEAR)
    week_day = (year_end.weekday() + 2) % 7

    if week_day > 3:
        return year_end + timedelta((7 - week_day))
    else:
        return year_end - timedelta(week_day)

def start_of_year(year):
    return end_of_year(year - 1) + timedelta(1)

def start_of_month(year, merch_month):
    start = start_of_year(year) + timedelta((int((merch_month - 1) / 3) * 91))

    if merch_month in FOUR_WEEK_MONTHS:
        start = start + timedelta(28)
    if merch_month in FIVE_WEEK_MONTHS:
        start = start + timedelta(63)

    return start

def end_of_month(year, merch_month):
    if merch_month == 12:
        return end_of_year(year)
    else:
        return start_of_month(year, merch_month + 1) - timedelta(1)

def start_of_week(year, month, merch_week):
    return start_of_month(year, month) + timedelta((merch_week - 1) * 7)

def end_of_week(year, month, merch_week):
    return start_of_month(year, month) + timedelta(6 + ((merch_week - 1) * 7))

def start_of_quarter(year, quarter):
    if quarter == QUARTER_1:
        return start_of_month(year, 1)
    if quarter == QUARTER_2:
        return start_of_month(year, 4)
    if quarter == QUARTER_3:
        return start_of_month(year, 7)
    if quarter == QUARTER_4:
        return start_of_month(year, 10)
    raise ValueError('Invalid quarter. Expected 1 - 4')

def end_of_quarter(year, quarter):
    if quarter == QUARTER_1:
        return end_of_month(year, 3)
    if quarter == QUARTER_2:
        return end_of_month(year, 6)
    if quarter == QUARTER_3:
        return end_of_month(year, 9)
    if quarter == QUARTER_4:
        return end_of_month(year, 12)
    raise ValueError('Invalid quarter. Expected 1 - 4')

def season(merch_month):
    if merch_month in [1,2,3,4,5,6]:
        return 1
    if merch_month in [7,8,9,10,11,12]:
        return 2
    raise ValueError('Invalid month')

def start_of_season(year, merch_season):
    if merch_season == 1:
        return start_of_year(year)
    if merch_season == 2:
        return start_of_month(year, 7)
    else:
        raise ValueError('Invalid season. 1 = Spring/Summer, 2 = Fall/Holiday (Autumn/Winter)')

def end_of_season(year, merch_season):
    if merch_season == 1:
        return end_of_quarter(year, 2)
    if merch_season == 2:
        return end_of_year(year)
    else:
        raise ValueError('Invalid season. 1 = Spring/Summer, 2 = Fall/Holiday (Autumn/Winter)')

def weeks_in_year(year):
    return int((start_of_year(year + 1) - start_of_year(year)).days / 7)

def year(julian_date):
    date_start_of_year = start_of_year(julian_date.year)
    if julian_date < date_start_of_year:
        return julian_date.year - 1
    else:
        return julian_date.year

def month(julian_date):
    merch_year = year(julian_date)
    m = 1
    while m < 13:
        if end_of_month(merch_year, m) >= julian_date and \
        julian_date >= start_of_month(merch_year, m):
            return m
        m += 1
    raise Exception

def weeks_in_month(year, merch_month):
    month_start = start_of_month(year, merch_month)
    month_end = end_of_month(year, merch_month)
    return int((month_end - month_start + timedelta(1)).days / 7)

def week_of_year(julian_date):
    merch_year = year(julian_date)
    return math.ceil((julian_date - start_of_year(merch_year) + timedelta(1)).days / 7.0)

def week_of_month(julian_date):
    merch_month = month(julian_date)
    merch_year = year(julian_date)
    return math.ceil((julian_date - start_of_month(merch_year, merch_month) + timedelta(1)).days / 7.0)

def to_julian_month(merch_month):
    if merch_month > 12 or merch_month <= 0:
        raise ValueError('Unexpected month. Expected 1 - 12')
    if merch_month == 12:
        return 1
    else:
        return merch_month + 1
