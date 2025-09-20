from utils.output import print_header, print_nmap_scan_op as nmap_op_print, print_inicial_enumeration_op as pieo
from utils.save_files import save_file
from os import system
import subprocess
import re

class NmapScanner:
    def __init__(self, target):
        self.target = target
        self.os = ''
        self.open_ports = []

    def menu(self):
        while True:
            system("clear")
            print_header("Nmap Scan")
            pieo(self.target)
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
                case '99':
                    break

    def simple_scan(self):
        print(f"[+] Running 'nmap {self.target} -p22,80,139,445 -Pn -T4 -O'")
        cmd = ["nmap", self.target, "-p22,80,139,445", "-Pn", "-T4", "-O"]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"[!] Error: {e}")
            input("\nPress any...")
            return

        output = result.stdout
        self.open_ports = re.findall(r"(\d+)/tcp\s+open", output)

        if self.open_ports:
            for port in self.open_ports:
                print(f"Port: {port}")
        else:
            print("No open ports.\n")

        os_match = re.search(r"OS details: (.+)", output)
        if os_match:
            self.os = os_match.group(1)
            print(f"\nOS: {self.os}")
        else:
            print("\n[!] Error getting OS version.")

        print("[+] Saving output file. . .")
        self.save_scan("simple_scan.txt", output)
        input("[+] Press any ")

    def advanced_scan(self):
        if not self.open_ports:
            print("[!] No open ports found.")
            input("[*] Press any...")
            return

        ports_str = ",".join(self.open_ports)
        print(f"[+] Running 'nmap {self.target} -A -T4 -p{ports_str} -Pn -T4'")
        cmd = ["nmap", self.target, f"-p{ports_str}", "-Pn", "-T4", "-A"]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"[!] Error: {e}")
            input("\nPress any...")
            return

        output = result.stdout

        ports = re.split(r"(?=\d+/tcp\s+open)", output)

        for section in ports:
            port_match = re.match(r"(\d+/tcp)\s+open\s+([\w\-\._]+)?\s*(.*)", section)
            if port_match:
                port, service, version = port_match.groups()
                print(f"{port} - {service} - {version}")

                scripts = re.findall(r"^\|\s+(.*)", section, re.MULTILINE)
                for script in scripts:
                    print(f"{script}")
                print("-" * 50)

        print("[+] Saving output file. . .")
        self.save_scan("simple_scan.txt", output)
        input("[+] File saved!\n[+] Press any ")

    def custom_scan(self, flags):
        system(f"nmap {flags} {self.target}")

    def save_scan(self, filename, data):
        save_file(filename, data, "nmap")
        print("[+] File saved!")
