num=int(input("Enter number: "))
prime='yes'
for i in range (2, num):
    if num%i==0:
        prime="no"
        break
    else:
        pass
if prime=="yes":
    print("The number given is pime.")
else:
    print("The number given is not prime")
