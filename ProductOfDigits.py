num = 1
temp = num
pro = 1
if num == 0:
    pro = 0
else:
    while num >0:
        temp = num % 10
        pro *= temp
        num //= 10
print(pro)
