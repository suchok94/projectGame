import os
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


def info():
    print('!!info!!')

def choice_race():
    print("Выберите расу: Человек, Эльф, Гном: ")

    return input("")

def choice_class_character():
    print("Выберите класс: Воин, Маг, Лучник")
    return input()

def choice_name():
    print('введите имя своего персонажа')
    return input()

def list_world():
    path = r'Worlds'
    info()
    if os.path.isdir(path) == True:
        os.chdir(path)
        print('список миров')
        print(os.listdir())
    else:
        print('нет созданных миров')

def choice_world():
    print("напиишите название мира для выбора")
    return input()


def welcome_new_game(name, world):
    '''
    выводит информацию о мире в который попал игрок
    :return:
    '''
    print(f'Hello, {name}, ti popal v {world}')


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
