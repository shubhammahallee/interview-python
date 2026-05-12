string = input("Enter: ")
consonant_indices = []
count = 0

for i, char in enumerate(string.lower()):
    if char not in "aeiou":
        consonant_indices.append(i)   
        count += 1

print("Original string:", string)
print("consonant count:", count)
print("consonant indices:", consonant_indices)