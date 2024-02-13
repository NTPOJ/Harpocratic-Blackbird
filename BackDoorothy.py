#Important modules to import
import socket
import sys
from datetime import datetime
import threading
import concurrent.futures
import pyfiglet
import colorama
from colorama import Fore
colorama.init()

#Enables threading for port scans
print_lock = threading.Lock()

ascii_banner = pyfiglet.figlet_format("Back Doorothy")
print(Fore.MAGENTA + ascii_banner)

#Input for host IP
ip = input("Enter Host IP to scan: ")

#Scan is defined by imported module functions.
#Uses sockets to obtain data from the internet.
#Prints out open ports
#Timer set to pass closed ports and move on to the open ports.
print("Scanning started at:" + str(datetime.now()))
def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{port}]" + Fore.GREEN + "Open")
    except:
        pass

#Sets the amount of threads to run, and the range for ports. 
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1000):
        executor.submit(scan, ip, port + 1)
