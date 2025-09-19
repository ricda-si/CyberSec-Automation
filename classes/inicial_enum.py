from utils.print_headers import print_header, print_ini_enum_op as pieo
import os

class InicialEnum:
    def __init__(self):
        self.ip = ''
        self.hostname = ''
        self.os = ''
        self.ports = []

    def set_target(self):
        while self.ip == '':
            self.ip = input("Target IP: ")

    def menu(self):
        os.system("cls")
        print_header("inicial enumeration")
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
        os.system("nmap 192.168.80.1 -o nmap.txt >/dev/null")


    def dir_enum(self):
        ...

    def smb_enum(self):
        ...

    def target_info(self):
        os.system("cls")
        print_header("inicial enumeration")
        pieo(target='', os=self.os)
        print(f"IP: {self.ip}")
        print(f"OS: {self.os}")
        for port in self.ports:
            print(f"Ports: {port}")
        print(f"Hostname: {self.hostname}")

