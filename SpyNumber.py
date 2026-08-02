num = 123
temp = num
sum = 0
pro = 1

while temp > 0:
    digit = temp % 10
    sum += digit
    pro *= digit
    temp //= 10


if sum == pro:
    print("Spy Number")
else:
    print("Not Spy Number") 
