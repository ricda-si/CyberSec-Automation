import os
from utils.print_headers import print_header, print_menu_options

def clear_screen():
    os.system("cls")

def menu(target='') -> None:
    clear_screen()
    print_header("menu")
    print_menu_options()

if __name__ == '__main__':
    menu()
