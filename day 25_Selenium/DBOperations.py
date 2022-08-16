# mysql insert, delete, update
insert_query = "insert into student values(103,'Rajib',80)"
update_query = "update student set sname='Jamil' where sno=102"
delete_query = "delete from student where sno=103"


import mysql.connector
try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    curs = con.cursor()  # Create Cursor
    curs.execute(delete_query)  # execute query through cursor
    con.commit()  # commit transaction
    con.close()
except:
    print("Connection Unsuccessful")

print("DB Operation Finished......")