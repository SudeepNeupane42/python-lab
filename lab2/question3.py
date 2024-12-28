str = input("Enter a string: ")
str2 = str.replace(" ", "")
if str2 == str2[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
