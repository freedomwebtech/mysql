import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
       host= "",
       username="",
       password="",
       database=""

)

print (mydb)
now = datetime.now()
datetime = now.strftime("%H:%M:%S")
a = mydb.cursor()
a.execute("DROP TABLE Distance")
#a.execute("CREATE TABLE Distance (DateTime VARCHAR(255), Distance VARCHAR(255))")
#sql = ("INSERT INTO Distance(DateTime,Distance) VALUE(%s,%s)") 
#data= (datetime,"23")

#a.execute(sql,data)
#mydb.commit()
