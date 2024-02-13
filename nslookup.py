import socket
import pyfiglet
import colorama
from colorama import Fore

colorama.init()

ascii_banner = pyfiglet.figlet_format("NSLookup")
print(Fore.GREEN + ascii_banner.center(80, "-"))


hostname = input("Please enter target website address:\n")


#IP lookup from hostname
print(f' {hostname} Ip Address is {socket.gethostbyname(hostname)}')
