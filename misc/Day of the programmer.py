"""
What is the Day of the programmer is in a given year in Russia?

The Day of the Programmer (the 256th day of the year) during a year in the inclusive range from 1700 to 2700.

From 1700 to 1917, Russia's official calendar was the Julian calendar;
since 1919 they used the Gregorian calendar system. The transition from the
Julian to Gregorian calendar system occurred in 1918, when the next day after
January 31 was February 14. This means that in 1918, February 14 was the 32 day
of the year in Russia.

2017 -> 13.09.2017
2016 -> 12.09.2016
"""

def is_leap_year(year, calendar='Gregorian'):
    if calendar == 'Gregorian':
        return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))
    elif calendar == 'Julian':
        return year % 4 == 0
    else:
        return 'Calendar {} is not supported'.format(calendar)


def days_in_month(month, year, calendar='Gregorian'):
    days_month = {
        12: 31, 1: 31, 2: 28,  # winter
        3: 31, 4: 30, 5: 31,   # spring
        6: 30, 7: 31, 8: 31,   # summer
        9: 30, 10: 31, 11: 30  # autumn
    }
    if month == 2:
        return 29 if is_leap_year(year, calendar) else 28
    else:
        return days_month[month]


def calendar_used_in_russia(year):
    if 1700 <= year <= 1917: return 'Julian'
    elif year >= 1919: return 'Gregorian'
    else: return 'Pagan'


def day_to_date(day, year):
    calendar = calendar_used_in_russia(year)
    month = 1
    while day > days_in_month(month, year, calendar):
        day -= days_in_month(month, year, calendar)
        month += 1
    return day, month, year


def solve(year):

    if year = 1918:
        return '26.09.1918'

    calendar = calendar_used_in_russia(year)
    if is_leap_year(year, calendar):
        return '12.09.' + str(year)
    else:
        return '13.09.' + str(year)


print(solve(2017))

print(day_to_date(256, 2017))
