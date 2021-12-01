import Controller
import psycopg2

try:
    connection = psycopg2.connect(user="postgres", password="1", host="localhost", port="5432",
                                  database="Database1", )
    cursor = connection.cursor()
    Controller.mainmenu()
except (Exception, psycopg2.Error) as error:
    print("PostgreSQL connection Error: ", error)
finally:
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")