def is_year_leap(year):
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    thirty = [4,6,9,11]
    thirty_one = [1,3,5,7,8,10,12]
    if result_leap_year == True and month == 2:
        return 29
    elif result_leap_year == False and month == 2:
        return 28
    for i in thirty:
        if i == month:
            return 30
    for i in thirty_one:
        if i == month:
            return 31

def day_of_year(year, month, day):
    days_in_month_no_leap = [31,28,31,30,31,30,31,31,30,31,30,31]
    days_in_month_leap = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = 0
#add up the number of days in the previous months and add day variable to it
    if result_leap_year == False:
        for i in range(month - 1):
            days = days + days_in_month_no_leap[month - 1]
    if result_leap_year == True:
        for i in range(month - 1):
            days = day + days_in_month_leap[month - 1]
    print(days)



result_leap_year = is_year_leap(2000)
number_of_days_in_month = days_in_month(2000, 12)
day_of_year(2000,12,31)
