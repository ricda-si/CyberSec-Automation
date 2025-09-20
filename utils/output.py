def print_header(title):
    string = f"| -> {title.capitalize()} <- |"
    size = len(string) - 2
    print("+" + ("-" * size) + "+")
    print(f"{string}")
    print("+" + ("-" * size) + "+")

def print_menu_op():
    print("+-----------------------------------+")
    print("| 1.  Inicial Enumeration           |")
    print("|                                   |")
    print("| 2.  Post-Exploitation Enumeration |")
    print("|                                   |")
    print("| 3.  Post-Exploitation Attacks     |")
    print("|                                   |")
    print("| 99. Exit                          |")
    print("+----------------------------------+\n")

def print_inicial_enumeration_op(target, flag=False):
    if target == '' or flag == False:
        string = f"| Target: {target} |"
        size = len(string) - 2
        print("+" + ("-" * size) + "+")
        print(f"{string}")
        print("+" + ("-" * size) + "+")

    else:
        string = f"| Target: {target} |"
        size = len(string) - 2
        print("+" + ("-" * size) + "+")
        print(f"{string}")
        print("+" + ("-" * size) + "+")

        print("+---------------------------+")
        print("| 1.  Nmap Scan             |")
        print("|                           |")
        print("| 2.  Directory Enumeration |")
        print("|                           |")
        print("| 3.  SMB Enumeration       |")
        print("|                           |")
        print("| 4.  Target Info           |")
        print("|                           |")
        print("| 99. Exit                  |")
        print("+---------------------------+\n")

def print_nmap_scan_op():
    print("+-------------------+")
    print("| 1.  Simple Scan   |")
    print("|                   |")
    print("| 2.  Advanced Scan |")
    print("|                   |")
    print("| 3.  Custom Scan   |")
    print("|                   |")
    print("| 99. Exit          |")
    print("+-------------------+\n")
