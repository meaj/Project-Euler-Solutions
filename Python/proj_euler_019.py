"""
This program finds the number of Sundays on the first of the month in the 20th century
By Kevin Moore
"""

lst_month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def calculate(int_start_year, int_stop_year):
    int_num_sundays = 0
    int_num_days = 1 # start on day 1 since the year does not start on day 0
    for year in range(int_start_year, int_stop_year):
        for month in lst_month_lengths:
            # Calculates total number of days passed
            int_num_days += month
            # Handles leap years
            if year % 4 == 0 and month == 28:
                # Handles century case
                if year % 100 == 0 and year % 400 != 0:
                    int_num_days -= 1
                int_num_days += 1
            # If the number of days at this point in the calcluation evenly
            # divides into 7,the first day of the month is a Sunday
            if int_num_days % 7 == 0:
                int_num_sundays += 1
    return int_num_sundays


def main():
    print(calculate(1901, 2000))


main()