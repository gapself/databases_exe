import mysql.connector

mydb = mysql.connector.connect(
    user='root',
    password='password',
    host='localhost',
    database='testdb'
)
mycursor= mydb.cursor()

# DELETING
sql = "DROP TABLE IF EXISTS students"
# sql = "DELETE FROM students WHERE age=22"
mycursor.execute(sql)
mydb.commit()

# ORDERING QUERIES
sql = "SELECT * FROM students ORDER BY name DESC" #ORDERBY name,age etc=> A-Z, ORDERBY name DESC=> Z-A
mycursor.execute(sql)
myresult=mycursor.fetchall()
for result in myresult:
    print(result)

# UPDATING
sql="UPDATE students SET age=27 WHERE name='Gabi'"
mycursor.execute("SELECT * FROM students LIMIT 3 OFFSET 2") #starts counting after 2
myresult=mycursor.fetchall()
for result in myresult:
    print(result)

# SELECTING
# sql= "SELECT * FROM students WHERE name='Gabi'"
# sql= "SELECT * FROM students WHERE name LIKE 'J%'"
sql="SELECT * FROM students WHERE name=%s"
# mycursor.execute(sql)
mycursor.execute(sql,("Jacob", ))
myresult=mycursor.fetchall()
for result in myresult:
    print(result)


# SELECTING SPECIFIC COLUMN
mycursor.execute("SELECT age FROM STUDENTS")

# SELECTING ALL with (*)
mycursor.execute("SELECT * FROM STUDENTS")
myresult = mycursor.fetchall()#prints all rows #fetch (go for & bring back) last execute statement:
myresult = mycursor.fetchone() #prints first row
for row in myresult:
    print(row)



# POPULATING
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# %s placeholder
students = [("Gabi", 25),
            ("Jacob", 26),
            ("Janusz", 28),
            ("Avi", 34),
            ("Michelle", 32),
            ]

#EXECUTE_MANY!
mycursor.executemany(sqlFormula,students)
mydb.commit()
# mysql-> SELECT *| FROM students


# STUDENT_1
student1 = ("Rachel", 22)
mycursor.execute(sqlFormula, student1)
mydb.commit()


# TABLES
mycursor.execute("CREATE TABLE students(name VARCHAR(255), age INTEGER(10))")
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

# DATABASE
mycursor.execute("CREATE DATABASE testdb")
mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)