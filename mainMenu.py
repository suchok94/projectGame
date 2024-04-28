import GUI
import game

def welcome():
    GUI.welcome()
    main_menu()
    GUI.exit()

def main_menu():
    while True:
        data = GUI.main_menu_input().lower()
        if data == 'exit':
            check_exit = GUI.check_exit().lower()
            if check_exit == 'y' or check_exit == 'yes':
                return
            if check_exit == 'n' or check_exit == 'no':
                continue
            else:
                GUI.incorrect_data()
        if data == 'new game':
            print('new game')
            path, world = game.create_new_game()
        elif data == 'load game':
            print('load game')
