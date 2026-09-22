def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

# returns the number of days for the given year-month pair
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(year < 1582 or month < 1 or month > 12):
        return None
    if(month == 2 and is_year_leap(year)):
        return 29
    else:
        return month_days[month - 1];

# returns the corresponding day of the year for the given day of the month
# ex:
def day_of_year(year, month, day):
    if(day < 1 or day > days_in_month(year, month)):
        return None
    else: 
        year_day = day

    for crt_month in range (1, month):
        crt_month_days = days_in_month(year, crt_month)
        if crt_month_days == None:
            return None
        else:
            year_day += crt_month_days
            
    return year_day

print(day_of_year(2000, 12, 31))