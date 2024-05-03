import calendar

year = 2024
month = 3
cal = calendar.monthcalendar(year, month)
print("Mon Tue Wed Thu Fri Sat Sun")
for week in cal:
    for day in week:
        if day == 0:
            print(" ", end=" ")
        else:
            print(f"{day: 0}", end=" ")
    print()
