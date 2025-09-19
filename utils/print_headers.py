import os

def print_header(title):
    size = len(title) + len("\t") + len("\t")
    print("+" + ("-" * size) + "+")
    print(f"|   {title.capitalize()}    |")
    print("+" + ("-" * size) + "+")
