week_days = [False,False,False,False,False,False,True]
index = 1
count = 0

for year in range(1901,2001):
    
    for month in range(12):

        if month == 1:
            if year%4 == 0:
                if year % 100 == 0:
                    if year%400 == 0:
                        days = 29
                    else:
                        days = 28
                else:
                    days = 29
            else:
                days = 28
        elif month == 3 or month == 5 or month == 8 or month ==10:
            days = 30
        else:
            days = 31
        
        for day in range(days):
            if day == 0 and week_days[index%7]:
                count += 1
            index += 1

print(count)

