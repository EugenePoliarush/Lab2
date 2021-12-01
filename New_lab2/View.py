tables = {
    1: 'Apartment',
    2: 'Building',
    3: 'Company',
    4: 'Person',
}

class View:
    def __init__(self, table):
        self.table = table

    @staticmethod
    def list():
        print('''
        1 -> Apartment
        2 -> Building
        3 -> Company
        4 -> Person
        ''')

    @staticmethod
    def attribute_list(table):
        if table == 1:
            print('''
            1 -> id_apartment
            2 -> floor
            3 -> number
            4 -> number_of_rooms
            5 -> id_person
            6 -> id_building
            ''')
        elif table == 2:
            print('''
            1 -> id_building
            2 -> adress
            3 -> number_of_apartments
            4 -> number_of_floors
            5 -> Company_name
            ''')
        elif table == 3:
            print('''
            1 -> Company_name
            2 -> adress
            3 -> phone
            ''')
        elif table == 4:
            print('''
            1 -> id_person
            2 -> name
            3 -> surname
            4 -> patronymic
            5 -> phone
            6 -> Company_name
            ''')

    @staticmethod
    def Print_SQL_query(show):
        print("SQL query -> ", show)
        print('')

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
    def showOneTable(table_name, printtable):
        print(table_name)
        print(printtable)
        print('')

    @staticmethod
    def insert_table1():
        id_apartment = input("id_apartment = ")
        floor = input("floor = ")
        number = input("number = ")
        number_of_rooms = input('number_of_rooms = ')
        id_person = input('id_person = ')
        id_building = input('id_building = ')
        return id_apartment, floor, number, number_of_rooms, id_person, id_building

    @staticmethod
    def insert_table2():
        id_building = input('id_building = ')
        adress = "'" + input('adress = ') + "'"
        number_of_apartments = input('number_of_apartments = ')
        number_of_floors = input('number_of_floors = ')
        Company_name = "'" + input('Company_name = ') + "'"
        return id_building, adress, number_of_apartments, number_of_floors, Company_name

    @staticmethod
    def insert_table3():
        Company_name = "'" + input('Company_name = ') + "'"
        adress = "'" + input('adress = ') + "'"
        phone = "'" + input('phone = ') + "'"
        return Company_name, adress, phone


    @staticmethod
    def insert_table4():
        id_person = input('id_person = ')
        name = "'" + input('name = ') + "'"
        surname = "'" + input('surname = ') + "'"
        patronymic = "'" + input('patronymic = ') + "'"
        phone = "'" + input('phone = ') + "'"
        Company_name = "'" + input('Company_name = ') + "'"
        return id_person, name, surname, patronymic, phone, Company_name

    @staticmethod
    def delete_table1():
        id_apartment = input("id_apartment of row for deletion = ")
        return id_apartment

    @staticmethod
    def delete_table2():
        id_building = input("id_building of row for deletion = ")
        return id_building

    @staticmethod
    def delete_table3():
        Company_name = "'" + input("Company_name of row for deletion = ") + "'"
        return Company_name

    @staticmethod
    def delete_table4():
        id_person = input("id_person of row for deletion = ")
        return id_person

    @staticmethod
    def update_table1():
        id_apartment = "'" + input('id_apartment of row to update = ') + "'"
        View.attribute_list(1)
        flag = True
        while flag:
            num = input('Number of attribute ->')
            value = "'" + input('New value of attribute = ') + "'"
            if num == '1':
                set = '"id_apartment"= {}'.format(value)
                flag = False
            elif num == '2':
                set = '"floor"= {}'.format(value)
                flag = False
            elif num == '3':
                set = '"number"= {}'.format(value)
                flag = False
            elif num == '4':
                set = '"number_of_rooms"= {}'.format(value)
                flag = False
            elif num == '5':
                set = '"id_person"= {}'.format(value)
                flag = False
            elif num == '6':
                set = '"id_building"= {}'.format(value)
                flag = False
            else:
                print('\nWrong number, choose again.')
        return set, id_apartment

    @staticmethod
    def update_table2():
        id_building = "'" + input('id_building of row to update = ') + "'"
        View.attribute_list(2)
        flag = True
        while flag:
            num = input('Number of attribute =>')
            value = "'" + input('New value of attribute = ') + "'"
            if num == '1':
                set = '"id_building"= {}'.format(value)
                flag = False
            elif num == '2':
                set = '"adress"= {}'.format(value)
                flag = False
            elif num == '3':
                set = '"number_of_apartments"= {}'.format(value)
                flag = False
            elif num == '4':
                set = '"number_of_floors"= {}'.format(value)
                flag = False
            elif num == '5':
                set = '"Company_name"= {}'.format(value)
                flag = False
            else:
                print('\nWrong number, choose again.')
        return set, id_building

    @staticmethod
    def update_table3():
        Company_name = "'" + input('Company_name of row to update = ') + "'"
        View.attribute_list(3)
        flag = True
        while flag:
            num = input('Number of attribute =>')
            value = "'" + input('New value of attribute = ') + "'"
            if num == '1':
                set = '"Company_name"= {}'.format(value)
                flag = False
            elif num == '2':
                set = '"adress"= {}'.format(value)
                flag = False
            elif num == '3':
                set = '"phone"= {}'.format(value)
                flag = False
            else:
                print('\nWrong number, choose again.')
        return set, Company_name

    @staticmethod
    def update_table4():
        id_person = input('id_person of row to update = ')
        View.attribute_list(4)
        flag = True
        while flag:
            num = input('Number of attribute =>')
            value = "'" + input('New value of attribute = ') + "'"
            if num == '1':
                set = '"id_person"= {}'.format(value)
                flag = False
            elif num == '2':
                set = '"name"= {}'.format(value)
                flag = False
            elif num == '3':
                set = '"surname"= {}'.format(value)
                flag = False
            elif num == '4':
                set = '"patronymic"= {}'.format(value)
                flag = False
            elif num == '5':
                set = '"phone"= {}'.format(value)
                flag = False
            elif num == '6':
                set = '"Company_name"= {}'.format(value)
                flag = False
            else:
                print('\nWrong number, choose again.')
        return set, id_person

    @staticmethod
    def random_table():
        flag = True
        while flag:
            num = input('How many rows to random? -> ')
            if num.isdigit():
                flag = False
            else:
                print('\nWrong number, choose again.')
        return num

    @staticmethod
    def search():
        num_table = input('Enter numbers of tables for search from 2 to 4-> ')
        num = input('Enter numbers of atribute for search -> ')

        table1 = None
        table2 = None
        table3 = None
        table4 = None

        if num_table == '2':
            View.list()
            print('Choose number of first table.')
            table1 = View.CheckTable()
            print('Choose number of second table.')
            table2 = View.CheckTable()
        elif num_table == '3':
            View.list()
            print('Choose number of first table.')
            table1 = View.CheckTable()
            print('Choose number of second table.')
            table2 = View.CheckTable()
            print('Choose number of third table.')
            table3 = View.CheckTable()
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
            search = 'select * from public."{}"'.format(tables[table1]) + ' as one inner join public."{}"'.format(
                tables[table2]) + ' as two using({})'.format(key1) + ' where '
        elif num_table == '3':
            search = 'select * from public."{}"'.format(tables[table1]) + ' as one inner join public."{}"'.format(
                tables[table2]) + ' as two using({})'.format(key1) + ' inner join public."{}"'.format(
                tables[table3]) + ' as three using({})'.format(key2) + ' where '
        elif num_table == '4':
            search = 'select * from public."{}"'.format(tables[table1]) + ' as one inner join public."{}"'.format(
                tables[table2]) + ' as two using({})'.format(key1) + ' inner join public."{}"'.format(
                tables[table3]) + ' as three using({})'.format(key2) + ' inner join public."{}"'.format(
                tables[table4]) + ' as four using({})'.format(key3) + ' where '

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
                search += '{}<{} and {}<{}'.format(num1, atribute, atribute, num2)
            elif type_atribute == '2':
                atribute = input('Enter name of first atribute in form table.artibute -> ')
                num1 = "'" + input('Text = ') + "'"
                search += '{} LIKE {}'.format(atribute, num1)
            if i != (int(num) - 1):
                search += ' and '
        return search

    @staticmethod
    def mainmenu():
        print('''
                Menu
        1 -> Show one table
        2 -> Show all table
        3 -> Insert data
        4 -> Delete data
        5 -> Update data
        6 -> Randomize data
        7 -> Search data
        8 -> Exit''')

        choice = input('\nSelect from 1 to 8 -> ')

        if (not choice.isdigit() or int(choice)<1 or int(choice)>8):
            print('\nWrong number, choose again.')
        else:
            return choice