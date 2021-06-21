def is_year_leap(year):
    if(year>1582):
        ly=0
        if year%4==0:
            ly=1
        if year%100==0:
            ly=0
        if year%400==0:
            ly=1
        if ly==0:
            return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    m_d_31=[1,3,5,7,8,10,12]
    if(month in m_d_31):
        return 31
    elif month==2:
        return is_year_leap(year) and 29 or 28
    elif month > 12:
        return -1
    else:
        return 30

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
