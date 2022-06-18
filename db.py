import psycopg2
import psycopg2.extras as extras



def execute_values(df, table):
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="password",
        port=5432
    )

    # mycursor.execute("CREATE TABLE managers(Manager varchar(30), EmpId integer)")

    tuples = [tuple(x) for x in df.to_numpy()]

    cols = ','.join(list(df.columns))
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
       # conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    cursor.close()



