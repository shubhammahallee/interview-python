'''Given a string and a number N, we need to mirror the characters from the N-th position up to the length of the string in alphabetical order. In mirror operation, we change 'a' to 'z', 'b' to 'y' and so on.'''

input_string = input("EnterString: ")
n = int(input("Enter n: "))

alpha = 'abcdefghijklmnopqrstuvwxyz'
reverse = alpha[::-1]
dict1 = dict(zip(alpha,reverse))











