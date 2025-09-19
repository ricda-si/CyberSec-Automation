import os

def print_header(title):
    string = f"| -> {title.capitalize()} <- |"
    size = len(string) - 2
    print("+" + ("-" * size) + "+")
    print(f"{string}")
    print("+" + ("-" * size) + "+")

def print_menu_options():
    print("+----------------------------------+")
    print("| 1. Inicial Enumeration           |")
    print("|                                  |")
    print("| 2. Post-Exploitation Enumeration |")
    print("|                                  |")
    print("| 3. Post-Exploitation Attacks     |")
    print("+----------------------------------+\n")
