#Module Imports
import os
import sys
import colorama
from colorama import *
import pyfiglet

colorama.init()

#Clears the terminal when running
os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.RED + "Your good friend Harpocratic Blackbird!".center(80, "-"))
print(Fore.RED + 
"""
                                    .:^
             ^                     /   :
'`.        /;/                    /    /
\  \      /;/                    /    /
 \\ \    /;/                    /  ///
  \\ \  /;/                    /  ///
   \  \/_/____________________/    /
    `/                         \  /
    {  o              o  }'
     \_________________________/
""")

#Attack Options
print("List of Attacks:")
print("-" * 80)
print("[1]. DNS Converter")
print("[2]. BackDoorothy (Port Scanner)")
print("[3]. Directroy Scanner!")
print("[4]. !CAUTION! (DoS)")
print("[5]. Exit")

#Imports scripts for each attack based on number chosen	
selection = input("Choose Attack Number:")
if selection == "1":
	import DNS_Converter
elif selection == "2":
	import BackDoorothy
elif selection == "3":
	import Cyboogie
elif selection == "4":
	import DoS
elif selection == "5":
	sys.exit()
else:
	print("Invalid Selection. Enter 1-5.")
