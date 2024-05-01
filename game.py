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
    hp = 100
    armor = 1000
    attack_character = 10
    character = {'name': name,
                 'race': race,
                 'class': class_character,
                 'attack': attack_character,
                 'hp': hp,
                 'armor': armor}
    return character

def choice_name():
    # сделать проверку на числа?
    name_character = GUI.choice_name()
    return name_character

def choice_race():
    life = True
    race = ''
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
    class_character = ''
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
    name_world = ''
    while life == True:
        name_world = GUI.choice_world()
        if os.path.isdir(name_world):
            life = False
        else:
            GUI.incorrect_data()
    return name_world

def game(character, world, room = 'start.txt'):
    """
    главное ядро самой игры
    :param character:
    :param world:
    :return:
    """
    # цикл ходов и боёв
    GUI.welcome_new_game(character['name'], world, room)
    step = GUI.input_step(room)
    check_step(step)
    load_world(world, room)

    step_by_world()
    event()

# def check_step(step):
#     if step.lower() == 'вперёд' or step.lower() == 'вперед':


def load_world(world, room):
    """
    подгружает мир для игры
    :param world:
    :param room:
    :return:
    """
    path = os.path.join(world, room)
    file = open(path, 'r')
    data = file.read()
    file.close()

    return data

def step_by_world():
    '''
    передаёт шаг игрока
    :return:
    '''
    pass

def event():
    '''
    запускает событие в комнате
    :return:
    '''
    pass