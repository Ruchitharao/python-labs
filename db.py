import psycopg2

#connect to the database

db = psycopg2.connect(
    host = "localhost",
    user= "postgres",
    password="password",
    port=5432
)


#cursor and table creation
mycursor = db.cursor()

#mycursor.execute("CREATE TABLE managers(Manager varchar(30), EmpId integer)")

#mycursor.execute("SHOW")
mycursor.execute("SELECT * FROM managers")
#connection close
db.close()