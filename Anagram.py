str1 = input("Enter String: ").lower()
str2 = input("Enter String: ").lower()

def anagram(str1, str2):

    return sorted(str1) == sorted(str2)

print(anagram(str1,str2))