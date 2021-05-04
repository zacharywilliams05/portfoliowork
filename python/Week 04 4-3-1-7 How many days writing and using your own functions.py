#!/usr/bin/env python3
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
    if leap_result == True and month == 2:
        return 29
    elif leap_result == False and month == 2:
        return 28
    for i in thirty:
        if i == month:
            return 30
    for i in theirty_one:
        if i == month:
            return 31


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	leap_result = is_year_leap(yr)
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")