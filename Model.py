import Connect
import time
from View import View
from prettytable import from_db_cursor

tables = {
    1: 'Apartment',
    2: 'Building',
    3: 'Company',
    4: 'Person',
}

class Model:
    @staticmethod
    def CheckTable():
        flag = True
        while flag:
            table = input('Choose number of table -> ')
            if table.isdigit():
                table = int(table)
                if table >= 1 and table <= 4:
                    flag = False
                else:
                    print('Wrong number, choose again.')
            else:
                print('Wrong number, choose again.')
        return table

    @staticmethod
    def showOneTable():
        View.list()
        connect = Connect.makeConnect()
        cursor = connect.cursor()

        table = Model.CheckTable()

        table_name = '''"''' + tables[table] + '''"'''
        print(tables[table])

        show = 'select * from public.{}'.format(table_name)

        print("SQL query -> ", show)
        print('')
        cursor.execute(show)
        printtable = from_db_cursor(cursor)
        records = cursor.fetchall()
        obj = View(table, records, printtable)
        obj.show()
        cursor.close()
        Connect.closeConnect(connect)

    @staticmethod
    def showAllTables():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        for table in range(1, 5):
            table_name = '''"''' + tables[table] + '''"'''
            print(tables[table])

            show = 'select * from public.{}'.format(table_name)

            print("SQL query -> ", show)
            print('')
            cursor.execute(show)
            printtable = from_db_cursor(cursor)
            records = cursor.fetchall()
            obj = View(table, records, printtable)
            obj.show()
        cursor.close()
        Connect.closeConnect(connect)

    @staticmethod
    def insert():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        flag = True
        while flag:
            View.list()
            table = Model.CheckTable()
            if table == 1:
                id_apartment = input("id_apartment = ")
                floor = input("floor = ")
                number = input("number = ")
                number_of_rooms = input('number_of_rooms = ')
                id_person = input('id_person = ')
                id_building = input('id_building = ')

                insert = 'insert into "Apartment" ("id_apartment", "floor", "number", "number_of_rooms", "id_person", "id_building") values ({}, {}, {}, {}, {}, {})'.format(
                    id_apartment, floor, number, number_of_rooms, id_person, id_building)

                flag = False
            elif table == 2:
                id_building = input('id_building = ')
                adress = "'" + input('adress = ') + "'"
                number_of_apartments = input('number_of_apartments = ')
                number_of_floors = input('number_of_floors = ')
                Company_name = "'" + input('Company_name = ') + "'"

                insert = 'insert into "Building" ("id_building", "adress", "number_of_apartments", "number_of_floors", "Company_name") values ({}, {}, {}, {}, {})'.format(
                    id_building, adress, number_of_apartments, number_of_floors, Company_name)

                flag = False
            elif table == 3:
                Company_name = "'" + input('Company_name = ') + "'"
                adress = "'" + input('adress = ') + "'"
                phone = "'" + input('phone = ') + "'"

                insert = 'insert into "Company" ("Company_name", "adress", "phone") values ({}, {}, {})'.format(
                    Company_name, adress, phone)

                flag = False
            elif table == 4:
                id_person = input('id_person = ') + "'"
                name = "'" + input('name = ') + "'"
                surname = "'" + input('surname = ') + "'"
                patronymic = "'" + input('patronymic = ') + "'"
                phone = "'" + input('phone = ') + "'"
                Company_name = "'" + input('Company_name = ') + "'"

                insert = 'insert into "Person" ("id_person", "name", "surname", "patronymic", "phone", "Company_name") values ({}, {}, {}, {}, {}, {})'.format(
                    id_person, name, surname, patronymic, phone, Company_name)

                flag = False
            else:
                print('\nWrong number, choose again.')
        print(tables[table])
        print('SQl query -> ', insert)
        cursor.execute(insert)
        connect.commit()
        print('Data added successfully!')
        cursor.close()
        Connect.closeConnect(connect)

    @staticmethod
    def delete():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        flag = True
        while flag:
            View.list()
            table = Model.CheckTable()

            if table == 1:
                id_apartment = input('Enter "id_apartment" to delete = ')
                delete = 'delete from "Apartment" where "id_apartment"= {}'.format(id_apartment)
                flag = False
            elif table == 2:
                id_building = input('Enter "id_building" to delete = ')
                delete = 'delete from "Building" where "id_building"=  {}'.format(id_building)
                flag = False
            elif table == 3:
                Company_name = "'" + input('Enter "Company_name" to delete = ') + "'"
                delete = 'delete from "Company" where "Company_name"= {}'.format(Company_name)
                flag = False
            elif table == 4:
                id_person = input('Enter "id_person" to delete = ')
                delete = 'delete from "Person" where "id_person"= {}'.format(id_person)
            else:
                print('\nWrong number, choose again.')
        print(tables[table])
        print("SQL query -> ", delete)
        cursor.execute(delete)
        connect.commit()
        print('Data deleted successfully!')
        cursor.close()
        Connect.closeConnect(connect)

    @staticmethod
    def update():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        flag = True
        while flag:
            View.list()
            table = Model.CheckTable()
            if table == 1:
                id_apartment = "'" + input('id_apartment of row to update = ') + "'"
                View.attribute_list(1)
                second_flag = True
                while second_flag:
                    num = input('Number of attribute ->')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_apartment"= {}'.format(value)
                        second_flag = False
                    elif num == '2':
                        set = '"floor"= {}'.format(value)
                        second_flag = False
                    elif num == '3':
                        set = '"number"= {}'.format(value)
                        second_flag = False
                    elif num == '4':
                        set = '"number_of_rooms"= {}'.format(value)
                        second_flag = False
                    elif num == '5':
                        set = '"id_person"= {}'.format(value)
                        second_flag = False
                    elif num == '6':
                        set = '"id_building"= {}'.format(value)
                        second_flag = False
                    else:
                        print('\nWrong number, choose again.')
                update = 'update "Apartment" set {} where "id_apartment"= {}'.format(set, id_apartment)
                flag = False
                pass
            elif table == 2:
                id_building = "'" + input('id_building of row to update = ') + "'"
                View.attribute_list(2)
                second_flag = True
                while second_flag:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_building"= {}'.format(value)
                        second_flag = False
                    elif num == '2':
                        set = '"adress"= {}'.format(value)
                        second_flag = False
                    elif num == '3':
                        set = '"number_of_apartments"= {}'.format(value)
                        second_flag = False
                    elif num == '4':
                        set = '"number_of_floors"= {}'.format(value)
                        second_flag = False
                    elif num == '5':
                        set = '"Company_name"= {}'.format(value)
                        second_flag = False
                    else:
                        print('\nWrong number, choose again.')
                update = 'update "Building" set {} where "id_building"= {}'.format(set, id_building)
                flag = False
                pass
            elif table == 3:
                Company_name = "'" + input('Company_name of row to update = ') + "'"
                View.attribute_list(3)
                second_flag = True
                while second_flag:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"Company_name"= {}'.format(value)
                        second_flag = False
                    elif num == '2':
                        set = '"adress"= {}'.format(value)
                        second_flag = False
                    elif num == '3':
                        set = '"phone"= {}'.format(value)
                        second_flag = False
                    else:
                        print('\nWrong number, choose again.')
                update = 'update "Company" set {} where "Company_name"= {}'.format(set, Company_name)
                flag = False
                pass
            elif table == 4:
                id_person = input('id_person of row to update = ')
                View.attribute_list(4)
                second_flag = True
                while second_flag:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_person"= {}'.format(value)
                        second_flag = False
                    elif num == '2':
                        set = '"name"= {}'.format(value)
                        second_flag = False
                    elif num == '3':
                        set = '"surname"= {}'.format(value)
                        second_flag = False
                    elif num == '4':
                        set = '"patronymic"= {}'.format(value)
                        second_flag = False
                    elif num == '5':
                        set = '"phone"= {}'.format(value)
                        second_flag = False
                    elif num == '6':
                        set = '"Company_name"= {}'.format(value)
                        second_flag = False
                    else:
                        print('\nWrong number, choose again.')
                update = 'update "Person" set {} where "id_person"= {}'.format(set, id_person)
                flag = False
                pass
            else:
                print('\nWrong number, choose again.')
        print(tables[table])
        print("SQL query -> ", update)
        cursor.execute(update)
        connect.commit()
        print('Data updeted successfully!')
        cursor.close()
        Connect.closeConnect(connect)
        pass

    @staticmethod
    def random():
        connect = Connect.makeConnect()
        cursor = connect.cursor()

        flag = True
        while flag:
            View.list()
            table = Model.CheckTable()
            num = input('How many rows to random? -> ')
            if num.isdigit():
                flag = False
                for i in range(int(num)):
                    random = ''
                    if table == 1:
                        random = 'insert into "Apartment" select (select max(id_apartment)+1 from "Apartment"),ceil((RANDOM()*10)),ceil((RANDOM()*10)),ceil((RANDOM()*3)),(select ceil(RANDOM()*max(id_person)) from "Person"),(select ceil(RANDOM()*max(id_building)) from "Building")'
                    elif table == 2:
                        random = 'insert into "Building" select (select max(id_building)+1 from "Building"),array_to_string(ARRAY(select chr((97 + round(random()*25))::integer) From generate_series(1,floor(RANDOM()*(25-10)+10)::integer)),\' \'),ceil((RANDOM()*10)),ceil((RANDOM()*10)),(SELECT "Company_name" FROM "Company" ORDER BY RANDOM() LIMIT 1)'
                    elif table == 3:
                        random = 'insert into "Company" select array_to_string(ARRAY(select chr((97 + round(random()*25))::integer) From generate_series(1,floor(RANDOM()*(25-10)+10)::integer)),\' \'),array_to_string(ARRAY(select chr((97 + round(random()*25))::integer) From generate_series(1,floor(RANDOM()*(25-10)+10)::integer)),\' \'),array_to_string(ARRAY(select chr((48 + round(random()*9))::integer) From generate_series(1,floor(RANDOM()*(10-8)+8)::integer)),\' \')'
                    elif table == 4:
                        random = 'insert into "Person" select (select max(id_Person)+1 from "Person"),array_to_string(ARRAY(select chr((97 + round(random()*25))::integer) From generate_series(1,floor(RANDOM()*(25-10)+10)::integer)),\' \'),array_to_string(ARRAY(select chr((97 + round(random()*25))::integer) From generate_series(1,floor(RANDOM()*(25-10)+10)::integer)),\' \'),array_to_string(ARRAY(select chr((97 + round(random()*25))::integer) From generate_series(1,floor(RANDOM()*(25-10)+10)::integer)),\' \'),array_to_string(ARRAY(select chr((48 + round(random()*9))::integer) From generate_series(1,floor(RANDOM()*(10-8)+8)::integer)),\' \'),(SELECT "Company_name" FROM "Company" ORDER BY RANDOM() LIMIT 1)'
                    print("SQL query -> ", random)
                    cursor.execute(random)
                    connect.commit()   
            else:
                print('\nWrong number, choose again.')

        print('Data randomed successfully!')
        cursor.close()
        Connect.closeConnect(connect)

    #select * from public."Person" as one inner join public."Apartment" as two USING ("id_person") where 2<two.id_apartment and two.id_apartment<10 and one.Name LIKE 'Name2'
    #select * from public."Person" as one inner join public."Apartment" as two USING ("id_person") inner join public."Building" as three USING ("id_building") where 2<two.id_apartment and two.id_apartment<10 and one.Name LIKE 'Name2' and 3<three.number_of_floors and three.number_of_floors<10
    #select * from public."Person" as one inner join public."Company" as four USING("Company_name") inner join public."Apartment" as two USING ("id_person") inner join public."Building" as three USING ("id_building") where 2<two.id_apartment and two.id_apartment<10 and one.Name LIKE 'Name2' and 3<three.number_of_floors and three.number_of_floors<10 and four."Company_name" LIKE 'Comp name'
    @staticmethod
    def search():
        connect = Connect.makeConnect()
        cursor = connect.cursor()

        flag = True
        while flag:
            num_table = input('Enter numbers of tables for search from 2 to 4-> ')
            num = input('Enter numbers of atribute for search -> ')

            table1 = None
            table2 = None
            table3 = None
            table4 = None

            if num_table == '2':
                View.list()
                print('Choose number of first table.')
                table1 = Model.CheckTable()
                print('Choose number of second table.')
                table2 = Model.CheckTable()
            elif num_table == '3':
                View.list()
                print('Choose number of first table.')
                table1 = Model.CheckTable()
                print('Choose number of second table.')
                table2 = Model.CheckTable()
                print('Choose number of third table.')
                table3 = Model.CheckTable()
            elif num_table == '4':
                table1 = 4
                table2 = 3
                table3 = 2
                table4 = 1

            if num_table == '2':
                print(tables[table1])
                View.attribute_list(table1)
                print(tables[table2])
                View.attribute_list(table2) 
            elif num_table == '3':
                print(tables[table1])
                View.attribute_list(table1)
                print(tables[table2])
                View.attribute_list(table2) 
                print(tables[table3])
                View.attribute_list(table3) 
            elif num_table == '4':
                print(tables[table1])
                View.attribute_list(table1)
                print(tables[table2])
                View.attribute_list(table2) 
                print(tables[table3])
                View.attribute_list(table3) 
                print(tables[table4])
                View.attribute_list(table4)

            key1 = None
            key2 = None
            key3 = None

            if num_table == '2':
                key1 = input('Enter key1 -> ')
            elif num_table == '3':
                key1 = input('Enter key1 -> ')
                key2 = input('Enter key2 -> ')
            elif num_table == '4':
                key1 = input('Enter key1 -> ')
                key2 = input('Enter key2 -> ')
                key3 = input('Enter key3 -> ')
            search = ''
            if num_table == '2':
                search = 'select * from public."{}"'.format(tables[table1]) + ' as one inner join public."{}"'.format(tables[table2]) + ' as two using({})'.format(key1) + ' where '
            elif num_table == '3':
                search = 'select * from public."{}"'.format(tables[table1]) + ' as one inner join public."{}"'.format(tables[table2]) + ' as two using({})'.format(key1) + ' inner join public."{}"'.format(tables[table3]) + ' as three using({})'.format(key2) + ' where '
            elif num_table == '4':
                search = 'select * from public."{}"'.format(tables[table1]) + ' as one inner join public."{}"'.format(tables[table2]) + ' as two using({})'.format(key1)  + ' inner join public."{}"'.format(tables[table3]) + ' as three using({})'.format(key2)  + ' inner join public."{}"'.format(tables[table4]) + ' as four using({})'.format(key3) + ' where '

            for i in range(int(num)):
                if num_table == '2':
                    print(tables[table1])
                    View.attribute_list(table1)
                    print(tables[table2])
                    View.attribute_list(table2) 
                elif num_table == '3':
                    print(tables[table1])
                    View.attribute_list(table1)
                    print(tables[table2])
                    View.attribute_list(table2) 
                    print(tables[table3])
                    View.attribute_list(table3) 
                elif num_table == '4':
                    print(tables[table1])
                    View.attribute_list(table1)
                    print(tables[table2])
                    View.attribute_list(table2) 
                    print(tables[table3])
                    View.attribute_list(table3) 
                    print(tables[table4])
                    View.attribute_list(table4)
                type_atribute = input('Choose type of atribute\n 1 -> numeric\n 2 -> string ')
                if type_atribute == '1':
                    atribute = input('Enter name of first atribute in form table.artibute -> ')
                    num1 = input('min = ')
                    num2 = input('max = ')
                    search += '{}<{} and {}<{}'.format(num1,atribute,atribute,num2) 
                elif  type_atribute == '2':
                    atribute = input('Enter name of first atribute in form table.artibute -> ')
                    num1 = "'" + input('Text = ') + "'"
                    search += '{} LIKE {}'.format(atribute,num1) 
                if i != (int(num)-1):
                    search += ' and '
                    
            start = time.time()
            print("SQL query -> ", search)
            end = time.time()
            print("Time: ",end - start)
            cursor.execute(search)
            printtable = from_db_cursor(cursor)
            records = cursor.fetchall()
            obj = View(1, records, printtable)
            obj.show()
            connect.commit()   
            flag = False

        print('Data search successfully!')
        cursor.close()
        Connect.closeConnect(connect)