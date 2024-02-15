#Imported modules
import urllib.request
import io
import pyfiglet
import colorama
from colorama import Fore
colorama.init()

ascii_banner = pyfiglet.figlet_format("Boston Dynamic Rogue-1")
print(Fore.CYAN + ascii_banner)

url = input(str("Please enter the target URL:"))

#Uses URL Library to obtain information on URL's robots.txt page, if applicable.
#Uses IO to format output from request.
def get_robots_txt(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url  
        
    # Add "http://" if the scheme is missing
    path = url.rstrip("/") + "/"  
    
    # Ensure the URL ends with a "/"
    try:
        req = urllib.request.urlopen(path + "robots.txt", data=None)
        return str(req.read(), 'utf-8')
    except Exception as e:
        return f"Error fetching robots.txt: {e}"

robots_txt_content = get_robots_txt(url)
print(robots_txt_content)

# Function to check robots.txt content against a wordlist file
def check_wordlist(robots_txt_content, wordlist_file):
    with open(wordlist_file, 'r') as file:
        wordlist = [line.strip() for line in file]

    for word in wordlist:
        if word.lower() in robots_txt_content.lower():
            return True
    return False

# Defining Wordlist file
default_wordlist_file = "wordlist.txt"

# Check if any word from the wordlist is found in the robots.txt content
if check_wordlist(robots_txt_content, default_wordlist_file):
    print("Potential sensitive information found in robots.txt!")
else:
    print("No sensitive information found in robots.txt.")

print("What's next commrade?")

print("[1]. Back to base!")
print("[2]. There is always time for Cyboogie!")
print("[3]. We need R&D!")
print("[4]. Survery their ports!")
print("[5]. Launch it!")
print("[6]. Exit")

#Imports scripts for each attack based on number chosen, back home or exit	
selection = input("Choose wisely......")
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
elif selection == "6":
	sys.exit()
else:
	print("Invalid Selection. Enter 1-6.")
