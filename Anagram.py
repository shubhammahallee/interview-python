str1 = input("Enter String: ").lower()
str2 = input("Enter String: ").lower()

def anagram(str1, str2):

    return sorted(str1) == sorted(str2)
 
print(anagram(str1,str2))

------------------------------------------------------------------------



num = 153
temp = num
count = 0

while temp > 0:
    count += 1
    temp //= 10

temp = num
arm_sum = 0

while temp > 0:
    digit = temp % 10
    arm_sum += digit ** count
    temp //= 10

if arm_sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
