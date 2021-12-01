import psycopg2
import time
from prettytable import from_db_cursor

tables = {
    1: 'Apartment',
    2: 'Building',
    3: 'Company',
    4: 'Person',
}

class Model:
    @staticmethod
    def makeConnect():
        return psycopg2.connect(user="postgres", password="1", host="localhost", port="5432", database="Database1", )

    @staticmethod
    def closeConnect(connection):
        connection.commit()
        connection.close()

    @staticmethod
    def showOneTable(table):
        connect = Model.makeConnect()
        cursor = connect.cursor()

        table_name = '''"''' + tables[table] + '''"'''
        show = 'select * from public.{}'.format(table_name)

        cursor.execute(show)
        printtable = from_db_cursor(cursor)
        cursor.close()
        Model.closeConnect(connect)
        return table_name, show, printtable

    @staticmethod
    def insert_table1(id_apartment, floor, number, number_of_rooms, id_person, id_building):
        connect = Model.makeConnect()
        cursor = connect.cursor()
        insert = 'insert into "Apartment" ("id_apartment", "floor", "number", "number_of_rooms", "id_person", "id_building") values ({}, {}, {}, {}, {}, {})'.format(id_apartment, floor, number, number_of_rooms, id_person, id_building)
        cursor.execute(insert)
        cursor.close()
        Model.closeConnect(connect)
        return insert

    @staticmethod
    def insert_table2(id_building, adress, number_of_apartments, number_of_floors, Company_name):
        connect = Model.makeConnect()
        cursor = connect.cursor()
        insert = 'insert into "Building" ("id_building", "adress", "number_of_apartments", "number_of_floors", "Company_name") values ({}, {}, {}, {}, {})'.format(id_building, adress, number_of_apartments, number_of_floors, Company_name)
        cursor.execute(insert)
        cursor.close()
        Model.closeConnect(connect)
        return insert

    @staticmethod
    def insert_table3(Company_name, adress, phone):
        connect = Model.makeConnect()
        cursor = connect.cursor()
        insert = 'insert into "Company" ("Company_name", "adress", "phone") values ({}, {}, {})'.format(Company_name, adress, phone)
        cursor.execute(insert)
        cursor.close()
        Model.closeConnect(connect)
        return insert

    @staticmethod
    def insert_table4(id_person, name, surname, patronymic, phone, Company_name):
        connect = Model.makeConnect()
        cursor = connect.cursor()
        insert = 'insert into "Person" ("id_person", "name", "surname", "patronymic", "phone", "Company_name") values ({}, {}, {}, {}, {}, {})'.format(id_person, name, surname, patronymic, phone, Company_name)
        cursor.execute(insert)
        cursor.close()
        Model.closeConnect(connect)
        return insert

    @staticmethod
    def delete_table1(id_apartment):
        connect = Model.makeConnect()
        cursor = connect.cursor()
        delete = 'delete from "Apartment" where "id_apartment"= {}'.format(id_apartment)
        cursor.execute(delete)
        cursor.close()
        Model.closeConnect(connect)
        return delete

    @staticmethod
    def delete_table2(id_building):
        connect = Model.makeConnect()
        cursor = connect.cursor()
        delete = 'delete from "Building" where "id_building"=  {}'.format(id_building)
        cursor.execute(delete)
        cursor.close()
        Model.closeConnect(connect)
        return delete

    @staticmethod
    def delete_table3(Company_name):
        connect = Model.makeConnect()
        cursor = connect.cursor()
        delete = 'delete from "Company" where "Company_name"= {}'.format(Company_name)
        cursor.execute(delete)
        cursor.close()
        Model.closeConnect(connect)
        return delete

    @staticmethod
    def delete_table4(id_person):
        connect = Model.makeConnect()
        cursor = connect.cursor()
        delete = 'delete from "Person" where "id_person"= {}'.format(id_person)
        cursor.execute(delete)
        cursor.close()
        Model.closeConnect(connect)
        return delete

    @staticmethod
    def update_table1(set, id_apartment):
        connect = Model.makeConnect()
        cursor = connect.cursor()
        update = 'update "Apartment" set {} where "id_apartment"= {}'.format(set, id_apartment)
        cursor.execute(update)
        cursor.close()
        Model.closeConnect(connect)
        return update

    @staticmethod
    def update_table2(set, id_building):
        connect = Model.makeConnect()
        cursor = connect.cursor()
        update = 'update "Building" set {} where "id_building"= {}'.format(set, id_building)
        cursor.execute(update)
        cursor.close()
        Model.closeConnect(connect)
        return update

    @staticmethod
    def update_table3(set, Company_name):
        connect = Model.makeConnect()
        cursor = connect.cursor()
        update = 'update "Company" set {} where "Company_name"= {}'.format(set, Company_name)
        cursor.execute(update)
        cursor.close()
        Model.closeConnect(connect)
        return update

    @staticmethod
    def update_table4(set, id_person):
        connect = Model.makeConnect()
        cursor = connect.cursor()
        update = 'update "Person" set {} where "id_person"= {}'.format(set, id_person)
        cursor.execute(update)
        cursor.close()
        Model.closeConnect(connect)
        return update

    @staticmethod
    def random_table1():
        connect = Model.makeConnect()
        cursor = connect.cursor()
        random = 'insert into "Apartment" select (select max(id_apartment)+1 from "Apartment"),ceil((RANDOM()*10)),ceil((RANDOM()*10)),ceil((RANDOM()*3)),(select ceil(RANDOM()*max(id_person)) from "Person"),(select ceil(RANDOM()*max(id_building)) from "Building")'
        cursor.execute(random)
        cursor.close()
        Model.closeConnect(connect)
        return random

    @staticmethod
    def random_table2():
        connect = Model.makeConnect()
        cursor = connect.cursor()
        random = 'insert into "Building" select (select max(id_building)+1 from "Building"),array_to_string(ARRAY(select chr((97 + round(random()*25))::integer) From generate_series(1,floor(RANDOM()*(25-10)+10)::integer)),\' \'),ceil((RANDOM()*10)),ceil((RANDOM()*10)),(SELECT "Company_name" FROM "Company" ORDER BY RANDOM() LIMIT 1)'
        cursor.execute(random)
        cursor.close()
        Model.closeConnect(connect)
        return random

    @staticmethod
    def random_table3():
        connect = Model.makeConnect()
        cursor = connect.cursor()
        random = 'insert into "Company" select array_to_string(ARRAY(select chr((97 + round(random()*25))::integer) From generate_series(1,floor(RANDOM()*(25-10)+10)::integer)),\' \'),array_to_string(ARRAY(select chr((97 + round(random()*25))::integer) From generate_series(1,floor(RANDOM()*(25-10)+10)::integer)),\' \'),array_to_string(ARRAY(select chr((48 + round(random()*9))::integer) From generate_series(1,floor(RANDOM()*(10-8)+8)::integer)),\' \')'
        cursor.execute(random)
        cursor.close()
        Model.closeConnect(connect)
        return random

    @staticmethod
    def random_table4():
        connect = Model.makeConnect()
        cursor = connect.cursor()
        random = 'insert into "Person" select (select max(id_Person)+1 from "Person"),array_to_string(ARRAY(select chr((97 + round(random()*25))::integer) From generate_series(1,floor(RANDOM()*(25-10)+10)::integer)),\' \'),array_to_string(ARRAY(select chr((97 + round(random()*25))::integer) From generate_series(1,floor(RANDOM()*(25-10)+10)::integer)),\' \'),array_to_string(ARRAY(select chr((97 + round(random()*25))::integer) From generate_series(1,floor(RANDOM()*(25-10)+10)::integer)),\' \'),array_to_string(ARRAY(select chr((48 + round(random()*9))::integer) From generate_series(1,floor(RANDOM()*(10-8)+8)::integer)),\' \'),(SELECT "Company_name" FROM "Company" ORDER BY RANDOM() LIMIT 1)'
        cursor.execute(random)
        cursor.close()
        Model.closeConnect(connect)
        return random

    #select * from public."Person" as one inner join public."Apartment" as two USING ("id_person") where 2<two.id_apartment and two.id_apartment<10 and one.Name LIKE 'Name2'
    #select * from public."Person" as one inner join public."Apartment" as two USING ("id_person") inner join public."Building" as three USING ("id_building") where 2<two.id_apartment and two.id_apartment<10 and one.Name LIKE 'Name2' and 3<three.number_of_floors and three.number_of_floors<10
    #select * from public."Person" as one inner join public."Company" as four USING("Company_name") inner join public."Apartment" as two USING ("id_person") inner join public."Building" as three USING ("id_building") where 2<two.id_apartment and two.id_apartment<10 and one.Name LIKE 'Name2' and 3<three.number_of_floors and three.number_of_floors<10 and four."Company_name" LIKE 'Comp name'
    @staticmethod
    def search(search):
        connect = Model.makeConnect()
        cursor = connect.cursor()

        start = time.time()
        cursor.execute(search)
        end = time.time()
        #print("Time: ", end - start)
        printtable = from_db_cursor(cursor)

        cursor.close()
        Model.closeConnect(connect)
        return printtable