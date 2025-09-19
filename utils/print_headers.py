import os

def print_header(title):
    string = f"| -> {title.capitalize()} <- |"
    size = len(string) - 2
    print("+" + ("-" * size) + "+")
    print(f"{string}")
    print("+" + ("-" * size) + "+")
