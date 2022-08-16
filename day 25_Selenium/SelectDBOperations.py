# mysql insert, delete, update
import mysql.connector



try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    curs = con.cursor()  # Create Cursor
    curs.execute("select * from student")  # execute query through cursor
    for row in curs:
        print(row[0],row[1],row[2])

    con.close() #Close Connection
except:
    print("Connection Unsuccessful")

print("DB Operation Finished......")