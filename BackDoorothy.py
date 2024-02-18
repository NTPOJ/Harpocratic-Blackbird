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

# Enables threading for port scans
print_lock = threading.Lock()

ascii_banner = pyfiglet.figlet_format("Back Doorothy")
print(Fore.MAGENTA + ascii_banner)

while True:
    # Input for host IP
    ip = input("Enter Host IP to scan: ")

    # Scan is defined by imported module functions.
    # Uses sockets to obtain data from the internet.
    # Prints out open ports
    # Timer set to pass closed ports and move on to the open ports and services.
    print("Scan started at:" + str(datetime.now()))

    def service_scan(ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((ip, port))
                banner = s.recv(1024).decode('utf-8').strip()
                service_name = socket.getservbyport(port)
                with print_lock:
                    if banner:
                        print(Fore.WHITE + f"[{port}]" + Fore.GREEN + f"Open - {service_name} - Version: {banner}")
                    else:
                        print(Fore.WHITE + f"[{port}]" + Fore.GREEN + f"Open - {service_name} - Version: N/A")

        except (socket.timeout, socket.error):
            pass

    # Perform the service scan
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1000):
            executor.submit(service_scan, ip, port + 1)

    print("What's next comrade?")

    print("[1]. Back to base!")
    print("[2]. I need more!")
    print("[3]. Cyboogie!")
    print("[4]. We need R&D!")
    print("[5]. Launch it!")
    print("[6]. Exit")

    # Imports scripts for each attack based on the number chosen, back home, or exit
    selection = input("Choose wisely: ")

    if selection == "1":
        import Harpocratic_Blackbird
    elif selection == "2":
        # Continue to the next iteration of the loop
        continue
    elif selection == "3":
        import Cyboogie
    elif selection == "4":
        import nslookup
    elif selection == "5":
        import DoS
    elif selection == "6":
        sys.exit()
    else:
        print("Invalid Selection. Enter 1-6.")
