
#Module Imports
import os
import colorama
from colorama import *
import pyfiglet

colorama.init()

#Clears the terminal when running
os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to Drone.py!".center(80, "-"))
print(Fore.GREEN +
"""
   .-.    _,  .-.  ,_    .-.
 '-._'--'  \_| |_/  '--'_.-'
     '-._  \ | | /  _.-'
         `-.^| |^.-'
            `\=/`
	""")

#Attack Options
print("List of Attacks:")
print("-" * 80)
print("[1]. NS Lookup")
print("[2]. BackDoorothy (Port Scanner)")
print("[3]. Robots.txt crawler")
print("[4]. TU-95 (DoS)")

#Imports scripts for each attack based on number chosen	
selection = input("Choose Attack Number:")
if selection == "1":
	import nslookup
elif selection == "2":
	import BackDoorothy
elif selection == "3":
	import robots_crawler
elif selection == "4":
	import DoS
else:
	print("Invalid Selection. Enter 1-4.")


