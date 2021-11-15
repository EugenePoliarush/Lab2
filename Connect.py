import psycopg2

def makeConnect():
    return psycopg2.connect(
        user="postgres",
        password="1",
        host="localhost",
        port="5432",
        database="Database1",
    )

def closeConnect(connection):
    connection.commit()
    connection.close()
