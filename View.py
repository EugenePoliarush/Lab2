import Connect

class View:
    def __init__(self, table, records, printtable):
        self.table = table
        self.records = records
        self.printtable = printtable

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

    def show(self):
        print(self.printtable)