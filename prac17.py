import mysql.connector as sqlcon
mycon=sqlcon.connect(host="localhost", user="root", password="pass", database="test")
cur=mycon.cursor()
t=int(input("enter number of record you have to enter: "))
for i in range (t):
          roll=int(input(f"enter roll no of {i+1} student: "))
          name=input(f"enter name of {i+1} student: ")
          gender=input(f"enter gender of {i+1} student: ")
          dob=input(f"enter DOB of {i+1} student in (yyyy-mm-dd): ")
          pro_sub=input(f"enter project subbmitted or not of {i+1} student: ")
          val=(roll , name, gender, dob, pro_sub)
          cmd='insert into school(roll_no,name,gender,DOB,project) VALUES(%s,%s,%s,%s,%s)'
          cur.execute(cmd,val)
          mycon.commit()
          print(f"Record of student {i+1} is Successfully Recorded")
mycon.close()
