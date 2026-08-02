num = 1289

sml = num % 10
num //= 10

while num > 0:
    digit = num % 10
    sml = min(sml, digit)
    num //= 10

print("Smallest digit:", sml)
