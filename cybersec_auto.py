import os
from utils.print_headers import print_header, print_output

def clear_screen():
    os.system("clear")

def menu(target='') -> None:
    clear_screen()
    print_header("menu")
    print_output("""
                 1. Op1
                 2. Op2
                 """)

if __name__ == '__main__':
    menu()
