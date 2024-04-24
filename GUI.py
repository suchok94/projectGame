def welcome():
    print(f'Добро пожаловать в игру "Название игры"')

def main_menu_text():
    print("New game")
    print("Continue")
    print("Load game")
    print("Exit")

def main_menu_input():
    main_menu_text()
    print('Введите команду для продолжения...')
    return input()

def check_exit():
    print('Вы уверены что хотите выйти?')
    print('Y/N')
    return input()


def incorrect_data():
    print('Вы ввели неправильные данные')


def exit():
    print('GoodBye!')

# def input_player():





    # data = input("Введите свой выбор: ")
    # while data:
    #     if data == "New game":
    #         return 1
    #     elif data == "Continue":
    #         return 1
    #     elif data == "Load game":
    #         return 1
    #     elif data == "Exit":
    #         return 1
    #     else:
    #         print("Вы ввели неправильное значение: ")
    #         return True
