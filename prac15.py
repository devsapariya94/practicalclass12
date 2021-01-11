import mysql.connector as sqlcon
mycon=sqlcon.connect(host="localhost", user="root", password="942003", database="dev")
cur=mycon.cursor()
cur.execute("select * from school")
data=cur.fetchall()
count=cur.rowcount
print("no. of row are: ",count)
for row in data:
          print(row)
mycon.close()