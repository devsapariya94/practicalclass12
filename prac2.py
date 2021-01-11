def comp_intrest(p,r,n):
    '''this is the function for calculating compound intrest'''
    ci=p*((1+(r/100))**n)
    return ci

principle=float(input("principle: "))
rate=float(input("intrest rate: "))
time=float(input("time in year: "))

print("your compund intrest is ", end="")
print(comp_intrest(principle, rate, time))
