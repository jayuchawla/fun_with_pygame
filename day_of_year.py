m_d_31=[1,3,5,7,8,10,12]
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
    if(month in m_d_31):
        return 31
    elif month==2:
        return is_year_leap(year) and 29 or 28
    elif month > 12:
        return -1
    else:
        return 30

def day_of_year(year, month, day):
    if(day<=0 or day>31 and month in m_d_31):
        return None
    elif month==2 and day>29:
        return None
    elif day>30:
        return None
    day_of_year=0
    for i in range(12):
        if(i+1<month):
            day_of_year+=days_in_month(year, i+1)
    return day_of_year+day
    
print(day_of_year(2000, 12, 31))
