import psycopg2
import psycopg2.extras as extras
import logging

#create and configure logging

logging.basicConfig(filename = "C://Users//tumul//PycharmProjects//python-labs//test_datatrans.log",
                    format='%(asctime)s %(message)s',
                    filemode = 'w',
                    level = logging.DEBUG)
logging.getLogger('data.transpose').disabled= True
logger = logging.getLogger(__name__)



def execute_values(df,table):
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="password",
        port=5432
    )

    #mycursor = conn.cursor()
    #mycursor.execute("CREATE TABLE managers(Manager varchar(30), EmpId integer)")
    logger.info("Created table managers")
    #conn.commit()
    tuples = [tuple(x) for x in df.to_numpy()]

    cols = ','.join(list(df.columns))
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        logger.debug("functional call for data transpose")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        logger.exception(error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    logger.info("successfully inserted a dataframe into db")
    cursor.close()


#execute_values()
