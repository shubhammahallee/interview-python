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
