num = 123
temp = num
sum = 0
while num >0:
    temp = num % 10
    sum += temp
    num //= 10
print(sum)
