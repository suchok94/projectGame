import os.path

import GUI
def create_new_game():
    GUI.info()

    character = create_character()
    world = name_world()
    return character, world

def create_character():
    """
    создаёт словарь-character
    :return:
    """
    name = choice_name()
    race = choice_race()
    class_character = choice_class_character()
    character = {'name': name,
                 'race': race,
                  'class': class_character}
    return character

def choice_name():
    # сделать проверку на числа?
    name_character = GUI.choice_name()
    return name_character

def choice_race():
    life = True
    while life == True:
        race = GUI.choice_race()
        if race.lower() == 'человек':
            life = False
        elif race.lower() == 'эльф':
            life = False
        elif race.lower() == 'гном':
            life = False
        else:
            GUI.incorrect_data()
    return race

def choice_class_character():
    life = True
    while life == True:
        class_character = GUI.choice_class_character()
        if class_character.lower() == 'воин':
            life = False
        elif class_character.lower() == 'маг':
            life = False
        elif class_character.lower() == 'лучник':
            life = False
        else:
            GUI.incorrect_data()
    return class_character

def name_world()-> str:
    """
    выбор мира из предложенных папок
    :return: название папки
    """
    GUI.list_world() # показывает список миров
    name_world = choice_world()
    return name_world
    # показать какие папки есть
    # предоставить выбор
    # вернуть название выбранной папки

def choice_world():
    life = True
    while life == True:
        name_world = GUI.choice_world()
        if os.path.isdir(f'World\{name_world}'):
            life = False

    return name_world

def game(character, world):
    """
    принимает перса и мир для игры
    :param path:
    :param world:
    :return:
    """

    # цикл ходов и боёв

    pass