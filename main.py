from os import system
from sys import exit
from utils.output import print_header, print_menu_op
from classes.inicial_enum import InicialEnum

def clear_screen():
    system("cls")

def menu(target='') -> None:
    while True:
        clear_screen()
        print_header("menu")
        print_menu_op()
        usr = input("> ")
        match usr:
            case '1':
                IE.menu()
            case '99':
                exit()

if __name__ == '__main__':
    IE = InicialEnum()
    menu()
