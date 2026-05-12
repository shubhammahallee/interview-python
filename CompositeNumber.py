n = int(input("Enter Number: "))

def Composite_Number(n):

    if n <= 1:
        return False

    count = 0

    for i in range(1, n + 1):

        if n % i == 0:
            count += 1

    return count > 2

print("More than 2 divisors")
print(Composite_Number(n))