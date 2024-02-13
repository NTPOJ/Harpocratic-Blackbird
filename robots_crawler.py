#Imported modules
import urllib.request
import io
import pyfiglet
import colorama
from colorama import Fore
colorama.init()

ascii_banner = pyfiglet.figlet_format("Lets see some robots")
ascii_banner = pyfiglet.figlet_format("Boston Dynamic Rogue-1")
print(Fore.CYAN + ascii_banner)

url = input(str("Please enter target URL:"))
#Uses URL Library to obtain information on URL's with a robots.txt page.
#Uses IO to format output from request.
def get_robots_txt(url):
	if url.endswith('/'):
		path = url
	else:
		path = url + '/'
	req = urllib.request.urlopen(path + "robots.txt", data=None)
	data = io.TextIOWrapper(req, encoding='utf-8')
	return data.read()

print(get_robots_txt(url))

print("[1]. Back to base!")
print("[2]. There is always time for Cyboogie!")
print("[3]. We need R&D!")
print("[4]. Survery their ports!")
print("[5]. Launch it!")

#Imports scripts for each attack based on number chosen	
selection = input("What next commrade?")
if selection == "1":
	import Harpocratic-Blackbird
elif selection == "2":
	import robots_crawler
elif selection == "3":
	import nslookup
elif selection == "4":
	import BackDoorothy
 elif selection == "5":
	import DoS
else:
	print("Invalid Selection. Enter 1-5.")
