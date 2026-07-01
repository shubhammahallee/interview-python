'''Given a string and a number N, we need to mirror the characters from the N-th position up to the length of the string in alphabetical order. In mirror operation, we change 'a' to 'z', 'b' to 'y' and so on.'''

input_string = input("EnterString: ")
n = int(input("Enter n: "))

alpha = 'abcdefghijklmnopqrstuvwxyz'
reverse = alpha[::-1]
dict1 = dict(zip(alpha,reverse))

prefix = input_string[0:n-1]
suffix = input_string[n-1:]

mirror = ""
for i in range(0,len(suffix)):
  mirror = mirror + dict1[suffix[i]]

res = prefix + mirror
print(res)













