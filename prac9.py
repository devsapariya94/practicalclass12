import random
num=int(input("enter your lottery number: "))
won=random.randint(1,6)
if won==num:
          print("you won")
else:
          print("you loss")
          print("the winning number is ", won)