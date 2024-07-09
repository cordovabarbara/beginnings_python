### DATES ### 

from datetime import datetime

now = datetime.now()
print(now.year)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

year_2024 = datetime(2024, 7, 9)

print_date(year_2024)

from datetime import time

current_time = time(5, 40, 0)

print(current_time.hour)

from datetime import date

current_date = date.today()
    
print(current_date.year)
print(current_date.month)
print(current_date.day)



current_date = date(2024, 7, 9)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)





