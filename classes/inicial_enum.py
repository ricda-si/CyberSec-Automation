from utils.output import print_header, print_inicial_enumeration_op as pieo
from tools.nmap_scan import NmapScanner as nmap
from os import system

class InicialEnum:
    def __init__(self):
        self.ip = ''
        self.hostname = ''
        self.os = ''
        self.ports = []

    def set_target(self):
        while self.ip == '':
            self.ip = input("Target IP: ")
        self.nmap = nmap(self.ip)

    def menu(self):
        while True:
            system("clear")
            print_header("Inicial Enumeration")
            pieo(self.ip, self.os)
            if self.ip == '':
                self.set_target()
                self.menu()
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

    def nmap_scan(self):
        self.nmap.simple_scan()

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

