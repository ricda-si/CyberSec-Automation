from utils.output import print_header, print_nmap_scan_op as nmap_op_print
from os import system

class NmapScanner:
    def __init__(self, target):
        self.target = target

    def menu(self):
        system("clear")
        print_header("Nmap Scan")
        nmap_op_print()

    def simple_scan(self):
        system(f"nmap {self.target} -p- -Pn -T4 -oN simple_scan.txt")

    def advanced_scan(self, ports='-'):
        system(f"nmap -A -T4 -p{ports} -Pn {self.target} -oN advanced_scan.txt")

    def custom_scan(self, flags):
        system(f"nmap {flags} {self.target}")
