import socket
import sys
import pyfiglet
import colorama
from colorama import Fore

colorama.init()

while True:
    ascii_banner = pyfiglet.figlet_format("NSLookup")
    print(Fore.GREEN + ascii_banner.center(80, "-"))

    hostname = input("Please enter target website address:\n")

    # IP lookup from hostname
    print(f' {hostname} Ip Address is {socket.gethostbyname(hostname)}')

    print("What's next comrade?")

    print("[1]. Back to base!")
    print("[2]. MORE DNS Converter!")
    print("[3]. Directroy Scanner!")
    print("[4]. Port Scanner!")
    print("[5]. !CAUTION! (DoS)")
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
        import BackDoorothy
    elif selection == "5":
        import DoS
    elif selection == "6":
        sys.exit()
    else:
        print("Invalid Selection. Enter 1-6.")
