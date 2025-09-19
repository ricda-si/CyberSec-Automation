from utils.output import print_header, print_nmap_scan_op as nmap_op_print
from os import system
from pathlib import Path

class NmapScanner:
    def __init__(self, target):
        self.target = target
        self.save_path = Path(__name__).resolve().parent.parent / "data"

    def menu(self):
        system("clear")
        print_header("Nmap Scan")
        nmap_op_print()
        print(f"{self.save_path}\\simple_scan.txt")
        user = input("> ")
        match user:
            case '1':
                self.simple_scan()
            case '2':
                self.advanced_scan()
            case '3':
                flags = input("Custom Scan flags -> ")
                self.custom_scan(flags)

    def simple_scan(self):
        system(f"nmap {self.target} -p- -Pn -T4 -oN {self.save_path}\\simple_scan.txt")

    def advanced_scan(self, ports='-'):
        system(f"nmap -A -T4 -p{ports} -Pn {self.target} -oN {self.save_path}\\advanced_scan.txt")

    def custom_scan(self, flags):
        system(f"nmap {flags} {self.target}")
