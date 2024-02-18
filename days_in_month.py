def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
def days_in_month(year_wanted, month_wanted):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year_wanted) and month_wanted == 2:
    return 29
  else:
    return month_days[month_wanted - 1]
    
    
 
year = int(input("Which year would like to be? ")) # Enter a year
month = int(input("What about month? ")) # Enter a month
days = days_in_month(year, month)
print(f"The year you'd like to be in a year you'd like to be has {days}")
