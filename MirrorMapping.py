'''Given a string and a number N, we need to mirror the characters from the N-th position up to the length of the string in alphabetical order. In mirror operation, we change 'a' to 'z', 'b' to 'y' and so on.'''



input_string = input("Enter String: ")
n = int(input("Enter N: "))

alpha = "abcdefghijklmnopqrstuvwxyz"
reverse = alpha[::-1]

# Create mirror mapping
mirror_map = dict(zip(alpha, reverse))

# Split string
prefix = input_string[:n-1]
suffix = input_string[n-1:]

# Mirror remaining characters
mirror = ""
for ch in suffix:
    mirror += mirror_map[ch]

# Final result
print(prefix + mirror)
