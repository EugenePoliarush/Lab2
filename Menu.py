from Model import Model

class Menu:
    @staticmethod
    def mainmenu():
        exit = False
        while not exit:
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
            if choice == '1':
                Model.showOneTable()
            elif choice == '2':
                Model.showAllTables()
            elif choice == '3':
                end_flag = False
                while not end_flag:
                    Model.insert()
                    flag = True
                    while flag:
                        num = input('\nInsert again?\n 1 - Yes;\n 2 - No ->')
                        if num == '2':
                            end_flag = True
                            flag = False
                        elif num == '1':
                            flag = False
                            pass
                        else:
                            print('\nWrong number, choose again.')
            elif choice == '4':
                end_delete = False
                while not end_delete:
                    Model.delete()
                    incorrect = True
                    while incorrect:
                        num = input('\nContinue deletion?\n 1 - Yes;\n 2 - No ->')
                        if num == '2':
                            end_delete = True
                            incorrect = False
                        elif num == '1':
                            incorrect = False
                            pass
                        else:
                            print('\nWrong number, choose again.')
            elif choice == '5':
                end_update = False
                while not end_update:
                    Model.update()
                    incorrect = True
                    while incorrect:
                        num = input('\nContinue updation?\n 1 - Yes;\n 2 - No ->')
                        if num == '2':
                            end_update = True
                            incorrect = False
                        elif num == '1':
                            incorrect = False
                            pass
                        else:
                            print('\nWrong number, choose again.')
            elif choice == '6':
                end_random = False
                while not end_random:
                    Model.random()
                    incorrect = True
                    while incorrect:
                        num = input('\nContinue randomizition?\n 1 - Yes;\n 2 - No ->')
                        if num == '2':
                            end_random = True
                            incorrect = False
                        elif num == '1':
                            incorrect = False
                        else:
                            print('\nWrong number, choose again.')
            elif choice == '7':
                end_search = False
                while not end_search:
                    Model.search()
                    incorrect = True
                    while incorrect:
                        num = input('\nContinue search?\n 1 - Yes;\n 2 - No ->')
                        if num == '2':
                            end_search = True
                            incorrect = False
                        elif num == '1':
                            incorrect = False
                        else:
                            print('\nWrong number, choose again.')
            elif choice == '8':
                exit = True
            else:
                print('\nWrong number, choose again.')
            incorrect = True
            while incorrect:
                end = input('\nContinue work with DB?\n 1 - Yes;\n 2 - No ->')
                if end == '2':
                    incorrect = False
                    exit = True
                elif end == '1':
                    incorrect = False
                else:
                    print('\nWrong number, choose again.')
