num = 12
temp = num 
count = 0
if num == 0:
    count = 1
else:
    while num > 0:
        temp = num % 10
        count += 1
        num //= 10
print(count)
