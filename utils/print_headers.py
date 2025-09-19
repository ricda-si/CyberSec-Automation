import os

def print_header(title):
    string = f"| -> {title} <- |"
    size = len(string)
    print("+" + ("-" * size) + "+")
    print(f"{string}")
    print("+" + ("-" * size) + "+")
