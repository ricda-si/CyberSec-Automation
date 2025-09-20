from utils.output import print_header, print_nmap_scan_op as nmap_op_print
from os import system
from pathlib import Path
import subprocess
import re

class NmapScanner:
    def __init__(self, target, save_path):
        self.target = target
        self.save_path = save_path

    def menu(self):
        system("clear")
        print_header("Nmap Scan")
        nmap_op_print()
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
        cmd = ["nmap", self.target, "-p-", "-Pn", "-T4"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout
        open_ports = re.findall(r"(\d+)/tcp\s+open", output)
        if open_ports:
            print(open_ports)
            input()
        else:
            print("No open ports.\n")
            input()

    def advanced_scan(self, ports='-'):
        system(f"nmap -A -T4 -p{ports} -Pn {self.target} -oN {self.save_path}/advanced_scan.txt")

    def custom_scan(self, flags):
        system(f"nmap {flags} {self.target}")

    def save_scan(self, filename, data):
        path = self.save_path + f"/{filename}"
        with open(path, 'w') as file:
            file.write(data)
