import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test "
)

db_cursor = db.cursor()
# db_cursor.execute("create table Person (name varchar(50), age int ,personID int primary key AUTO_INCREMENT) ")
db_cursor.execute("INSERT INTO Person (name,age) VALUES ( %s,%s ) ", (""))
db.commit()
# for i in db_cursor:
#     print(i)

