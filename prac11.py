# import numpy as np
# int_rate=float(input("enter intrest rate: "))
# yer=float(input("enter time in year: "))
# loan_amt=float(input("enter Loan amount: "))
# total_month=yer*12
# emi_val=np.pmt(int_rate/12, total_month, loan_amt)
# p=np.ppmt(int_rate/12,1, total_month,loan_amt)
# i=np.ipmt(int_rate/12,1,total_month,loan_amt)
# print("principle amount= ",abs(p))
# print("intrest amount= ",abs(i))
# print("EMI amount= ",abs(emi_val))
# print("EMI amount= ",abs(p+i))

import numpy as np
# assume annual interest of 7.5%
def calc_interest(interest ,years , loan_value ):
   annual_rate = interest/100.0
   monthly_rate = annual_rate/12
   number_month = years * 12
   monthly_payment = abs(np.pmt(monthly_rate, number_month, loan_value))
#    sf1 = "Paying off a loan of ₹{:,} over {} years at"
#    sf2 = "{}% interest, your monthly payment will be ₹{:,.2f}"
   print("your monthly installment= ",round(monthly_payment,2),"₹")

int_rate=float(input("enter intrest rate: "))
yer=float(input("enter time in year: "))
loan_amt=float(input("enter Loan amount: "))
calc_interest(int_rate,yer,loan_amt)