import mysql.connector as sqlcon
mycon=sqlcon.connect(host="localhost", user="root", password="942003", database="dev")
cur=mycon.cursor()
cur.execute("create table school (roll_no int(2), name varchar(20), gender varchar(6),DOB date,project varchar(3))")
print("table created")

mycon.close()