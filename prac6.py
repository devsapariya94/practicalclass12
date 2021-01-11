file=open("mytext.txt", "r")

string=file.read()
file.close()
vowel=0

for i in string:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowel+=1
    else:
        pass
print("the total number of vowel is ",vowel)
