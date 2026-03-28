import calendar

date = str(input('What are you looking for (day/month/year)? '))
print()

if date == 'day':
    y = int(input('Enter a year: '))
    m = int(input('Enter a month: '))
    d = int(input('Enter a day: '))
    if m <= 12:
        ded = calendar.weekday(y, m, d)
        if ded == 0:
            print("That day was Monday")
        elif ded == 1:
            print("That day was Tuesday")
        elif ded == 2:
            print("That day was Wednesday")
        elif ded == 3:
            print("That day was Thursday")
        elif ded == 4:
            print("That day was Friday")
        elif ded == 5:
            print("That day was Saturday")
        elif ded == 6:
            print("That day was Sunday")

    else:
        print("This month doesn't exist!")
    print()

elif date == 'month':
    y = int(input('Enter a year: '))
    m = int(input('Enter a month: '))
    print()
    if m <= 12:
        print(calendar.month(y, m))
    else:
        print("This month doesn't exist!")

elif date == 'year':
    y = int(input('Enter a year: '))
    print()
    print(calendar.calendar(y))

else:
    print("You need to choose: day, month or year - try again!")