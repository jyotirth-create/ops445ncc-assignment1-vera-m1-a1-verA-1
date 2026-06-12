#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py
Author: "Jyotirth Oza"
Seneca Username: "joza2"
Semester: "Summer 2026"

The python code in this file (assignment1.py) is original work written by
"Jyotirth Oza". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys


def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3,
              7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}

    if month < 3:
        year -= 1

    num = (year + year // 4 - year // 100 + year // 400
           + offset[month] + date) % 7

    return days[num]


def mon_max(month: int, year: int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    if month == 2:
        if leap_year(year):
            return 29
        return 28

    month_days = {
        1: 31,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return month_days[month]


def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')  # split the date into year, month, and day
    year = int(str_year)                            # convert year so it can be used for math
    month = int(str_month)                          # convert month so it can be checked
    day = int(str_day)                              # convert day so one day can be added

    tmp_day = day + 1  # move forward by one day first

    if tmp_day > mon_max(month, year):
        to_day = 1  # if the date passed the month limit, restart at day 1
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    if tmp_month > 12:
        to_month = 1  # after December, the next month becomes January
        year = year + 1
    else:
        to_month = tmp_month

    next_date = f'{year}-{to_month:02}-{to_day:02}'

    return next_date


def usage():
    "Print a usage message to the user"
    print('Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD')
    sys.exit(1)


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    if len(date) != 10:
        return False

    if date[4] != '-' or date[7] != '-':
        return False

    str_year, str_month, str_day = date.split('-')

    # These checks stop the program from crashing when letters are entered.
    if not str_year.isdigit():
        return False

    if not str_month.isdigit():
        return False

    if not str_day.isdigit():
        return False

    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    if month < 1 or month > 12:
        return False

    # This catches bad dates like 2023-02-31 or 2023-04-31.
    if day < 1 or day > mon_max(month, year):
        return False

    return True

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    weekend_days = 0
    current_date = start_date

    while current_date <= stop_date:
        str_year, str_month, str_day = current_date.split('-')

        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        week_day = day_of_week(year, month, day)

        if week_day == 'sat' or week_day == 'sun':
            weekend_days = weekend_days + 1

        # after() is used here so the loop checks every date in the range.
        current_date = after(current_date)

    return weekend_days


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    first_date = sys.argv[1]
    second_date = sys.argv[2]

    if not valid_date(first_date) or not valid_date(second_date):
        usage()

    # YYYY-MM-DD dates can be compared as strings because the biggest part comes first.
    if first_date <= second_date:
        start_date = first_date
        stop_date = second_date
    else:
        start_date = second_date
        stop_date = first_date

    total_weekend_days = day_count(start_date, stop_date)

    print(f'The period between {start_date} and {stop_date} includes '
          f'{total_weekend_days} weekend days.')