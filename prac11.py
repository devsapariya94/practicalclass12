
import numpy as np

def calc_interest(interest ,years , loan_value ):
   annual_rate = interest/100.0
   monthly_rate = annual_rate/12
   number_month = years * 12
   monthly_payment = abs(np.pmt(monthly_rate, number_month, loan_value))

   print("your monthly installment= ",round(monthly_payment,2),"₹")

int_rate=float(input("enter intrest rate: "))
yer=float(input("enter time in year: "))
loan_amt=float(input("enter Loan amount: "))
calc_interest(int_rate,yer,loan_amt)
