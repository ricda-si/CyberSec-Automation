from utils.output import print_header, print_inicial_enumeration_op as pieo
from tools.nmap_scan import NmapScanner as nmap
from os import system
from pathlib import Path

class InicialEnum:
    def __init__(self):
        self.ip = '192.168.80.134'
        self.hostname = ''
        self.os = ''
        self.ports = []
        self.nmap = nmap(self.ip)

    def set_target(self):
        while self.ip == '':
            self.ip = input("Target IP: ")
        self.nmap = nmap(self.ip)

    def menu(self):
        while True:
            system("clear")
            print_header("Inicial Enumeration")
            pieo(self.ip, self.os, True)
            if self.ip == '':
                self.set_target()
                continue
            user = input("> ")
            match user:
                case '1':
                    self.nmap_scan()
                case '2':
                    self.dir_enum()
                case '3':
                    self.smb_enum()
                case '4':
                    self.target_info()
                case '99':
                    break

    def nmap_scan(self):
        self.nmap.menu()

    def dir_enum(self):
        ...

    def smb_enum(self):
        ...

    def target_info(self):
        system("clear")
        print_header("inicial enumeration")
        pieo(target='', os=self.os)
        print(f"IP: {self.ip}")
        print(f"OS: {self.os}")
        for port in self.ports:
            print(f"Ports: {port}")
        print(f"Hostname: {self.hostname}")

