# ####################################################
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
####################################################

# For convenience, let's number the days
# Start with Sunday as 0, up to Saturday as 6
# We'll also number the months, starting with January as 0

# Some basic counts
n_months = 12
n_days = 7

# The number of days per month
# (default in the case of February)
days_per_month = {
    0 : 31, # January
    1 : 28, # February
    2 : 31, # March
    3 : 30, # April
    4 : 31, # May
    5 : 30, # June
    6 : 31, # July
    7 : 31, # August
    8 : 30, # September
    9 : 31, # October
    10 : 30, # November
    11 : 31 # December
}

# Is the year a leap year?
def is_leap_year(year):
    if not year % 4 == 0:
        return False
    century = year % 100 == 0
    if century:
        return year % 400 == 0
    return True
   

# How many days in a given year?
# Useful from getting the starting date
def days_per_year(year):
    return 366 if is_leap_year(year) else 365


# Let's run over the years
total = 0
day = 1 + days_per_year(1900) % n_days
for year in range(1901, 2001):

    # Is the year a leap year?
    leap = is_leap_year(year)

    # Loop over each month
    for month in range(n_months):

        # Is the current day (i.e. the first of the month) a Sunday?
        # If so, add one to our total
        if day == 0:
            total += 1

        # Add the number of days to get to the first of next month
        day += days_per_month[month]
        if leap and month == 1:
            day += 1
        day %= n_days

print(total)