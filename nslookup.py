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

print("What's next commrade?")

print("[1]. Back to base!")
print("[2]. More R&D!")
print("[3]. Cyboogie!")
print("[4]. Survery their ports!")
print("[5]. Launch it!")
print("[6]. Exit")

#Imports scripts for each attack based on number chosen, back home or exit
selection = input("Choose wisely")
if selection == "1":
	import Harpocratic_Blackbird
elif selection == "2":
	import nslookup
elif selection == "3":
	import robots_crawler
elif selection == "4":
	import BackDoorothy
elif selection == "5":
	import DoS
elif selection == "6":
	sys.exit()
else:
	print("Invalid Selection. Enter 1-5.")
