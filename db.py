import psycopg2

#connect to the database

db = psycopg2.connect(
    host = "localhost",
    user= "postgres",
    password="password",
    port=5432
)

print(db)

#connection close
db.close()