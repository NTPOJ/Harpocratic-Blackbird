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
#Timer set to pass closed ports and move on to the open ports and services.
print("Scan started at:" + str(datetime.now()))
def service_scan(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            service_name = socket.getservbyport(port)
            with print_lock:
                print(Fore.WHITE + f"[{port}]" + Fore.GREEN + f"Open - {service_name}")
    except (socket.timeout, socket.error):
        pass

# Perform the service scan
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1000):
            executor.submit(service_scan, ip, port + 1)

#Sets the amount of threads to run, and the range for ports. 
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1000):
        executor.submit(scan, ip, port + 1)

print("What's next commrade?")

print("[1]. Back to base!")
print("[2]. I need more!")
print("[3]. Cyboogie!")
print("[4]. We need R&D!")
print("[5]. Launch it!")
print("[6]. Exit")

#Imports scripts for each attack based on number chosen, back home or exit
selection = input("Choose wisely")
if selection == "1":
	import Harpocratic_Blackbird
elif selection == "2":
	import BackDoorothy
elif selection == "3":
	import robots_crawler
elif selection == "4":
	import nslookup
elif selection == "5":
	import DoS
elif selection == "6":
	sys.exit()
else:
	print("Invalid Selection. Enter 1-5.")
