import psycopg2
import Connect
from Menu import Menu

try:
    connection = Connect.makeConnect()
    cursor = connection.cursor()
    Menu.mainmenu()

except (Exception , psycopg2.Error) as error :
        print ("PostgreSQL connection Error: ",error)
finally:
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
