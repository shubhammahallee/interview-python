string = input("Enter: ")
vowel_indices = []
count = 0

for i, char in enumerate(string.lower()):
    if char in "aeiou":
        vowel_indices.append(i)   # Store the index
        count += 1

print("Original string:", string)
print("Vowel count:", count)
print("Vowel indices:", vowel_indices)