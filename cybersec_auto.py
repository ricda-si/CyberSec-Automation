import os
from utils.print_headers import print_header

def clear_screen():
    os.system("clear")

def menu(target='') -> None:
    clear_screen()
    print_header("menu")

if __name__ == '__main__':
    menu()
