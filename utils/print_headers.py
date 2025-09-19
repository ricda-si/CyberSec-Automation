import os

def print_header(title):
    size = len(title)
    print("+" + ("-" * size) + "+")
    print(f"|{title.capitalize()}|")
    print("+" + ("-" * size) + "+")
