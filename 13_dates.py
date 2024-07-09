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




