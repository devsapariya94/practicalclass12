char=input("enter the character: ")

if char.isalpha():
    print(char, " is alphabet")
elif char.isdigit():
    print(char, " is digit")
else:
    print(char, " is special character")
