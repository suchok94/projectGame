import GUI
def create_new_game():
    GUI.info()

    path = create_character()
    world = choice_world()
    return path, world

def create_character():
    # записать в файл данные
    race = choice_race()
    class_character = choice_class_character()

    # path_to_file =
    # return path_to_file
    pass

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
def choice_world()-> str:
    """
    выбор мира из предложенных папок
    :return: название папки
    """
    # показать какие папки есть
    # предоставить выбор
    # вернуть название выбранной папки
    pass

def game(path, world):
    """
    принимает перса и мир для игры
    :param path:
    :param world:
    :return:
    """
    # цикл ходов и боёв

    pass