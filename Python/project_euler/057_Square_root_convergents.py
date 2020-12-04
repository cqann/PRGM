

num = 3
dem = 2
count = 0
for i in range(999):
    num, dem = dem*2 + num, dem + num

    if len(str(num)) > len(str(dem)):
        count += 1

print(count)





