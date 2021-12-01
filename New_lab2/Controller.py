from Model import Model
from View import View

def mainmenu():
    exit = False
    while not exit:
        choice = View.mainmenu()
        if choice == '1':
            showOneTable()
        elif choice == '2':
            showAllTables()
        elif choice == '3':
            View.list()
            table = View.CheckTable()
            if(table == 1):
                insert_table1()
            elif (table == 2):
                insert_table2()
            elif (table == 3):
                insert_table3()
            elif (table == 4):
                insert_table4()
        elif choice == '4':
            View.list()
            table = View.CheckTable()
            if(table == 1):
                delete_table1()
            elif (table == 2):
                delete_table2()
            elif (table == 3):
                delete_table3()
            elif (table == 4):
                delete_table4()
        elif choice == '5':
            View.list()
            table = View.CheckTable()
            if(table == 1):
                update_table1()
            elif (table == 2):
                update_table2()
            elif (table == 3):
                update_table3()
            elif (table == 4):
                update_table4()
        elif choice == '6':
            View.list()
            table = View.CheckTable()
            if(table == 1):
                random_table1()
            elif (table == 2):
                random_table2()
            elif (table == 3):
                random_table3()
            elif (table == 4):
                random_table4()
        elif choice == '7':
            search()
        elif choice == '8':
            exit = True

def showOneTable():
    View.list()
    table = View.CheckTable()
    table_name, show, printtable = Model.showOneTable(table)
    View.Print_SQL_query(show)
    View.showOneTable(table_name, printtable)

def showAllTables():
    for table in range(1, 5):
        table_name, show, printtable = Model.showOneTable(table)
        View.Print_SQL_query(show)
        View.showOneTable(table_name, printtable)

def insert_table1():
    id_apartment, floor, number, number_of_rooms, id_person, id_building = View.insert_table1()
    insert = Model.insert_table1(id_apartment, floor, number, number_of_rooms, id_person, id_building)
    View.Print_SQL_query(insert)

def insert_table2():
    id_building, adress, number_of_apartments, number_of_floors, Company_name = View.insert_table2()
    insert = Model.insert_table2(id_building, adress, number_of_apartments, number_of_floors, Company_name)
    View.Print_SQL_query(insert)

def insert_table3():
    Company_name, adress, phone = View.insert_table3()
    insert = Model.insert_table3(Company_name, adress, phone)
    View.Print_SQL_query(insert)

def insert_table4():
    id_person, name, surname, patronymic, phone, Company_name = View.insert_table4()
    insert = Model.insert_table4(id_person, name, surname, patronymic, phone, Company_name)
    View.Print_SQL_query(insert)

def delete_table1():
    id_apartment = View.delete_table1()
    delete = Model.delete_table1(id_apartment)
    View.Print_SQL_query(delete)

def delete_table2():
    id_building = View.delete_table2()
    delete = Model.delete_table2(id_building)
    View.Print_SQL_query(delete)

def delete_table3():
    Company_name = View.delete_table3()
    delete = Model.delete_table3(Company_name)
    View.Print_SQL_query(delete)

def delete_table4():
    id_person = View.delete_table4()
    delete = Model.delete_table4(id_person)
    View.Print_SQL_query(delete)

def update_table1():
    set, id_apartment = View.update_table1()
    update = Model.update_table1(set, id_apartment)
    View.Print_SQL_query(update)

def update_table2():
    set, id_building = View.update_table2()
    update = Model.update_table2(set, id_building)
    View.Print_SQL_query(update)

def update_table3():
    set, Company_name = View.update_table3()
    update = Model.update_table3(set, Company_name)
    View.Print_SQL_query(update)

def update_table4():
    set, id_person = View.update_table4()
    update = Model.update_table4(set, id_person)
    View.Print_SQL_query(update)

def random_table1():
    num = View.random_table()
    for i in range(int(num)):
        random = Model.random_table1()
        View.Print_SQL_query(random)

def random_table2():
    num = View.random_table()
    for i in range(int(num)):
        random = Model.random_table2()
        View.Print_SQL_query(random)

def random_table3():
    num = View.random_table()
    for i in range(int(num)):
        random = Model.random_table3()
        View.Print_SQL_query(random)

def random_table4():
    num = View.random_table()
    for i in range(int(num)):
        random = Model.random_table4()
        View.Print_SQL_query(random)

def search():
    search = View.search()
    printtable = Model.search(search)
    View.Print_SQL_query(search)
    View.showOneTable("Search_table", printtable)

