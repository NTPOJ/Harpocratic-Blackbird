#Imported modules
import urllib.request
import sys
import io
import pyfiglet
import colorama
from colorama import Fore

colorama.init()

ascii_banner = pyfiglet.figlet_format("CYBOOGIE!")
print(Fore.CYAN + ascii_banner)

while True:
    url = input(str("Please enter the target URL:"))

    def get_robots_txt(url):
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        path = url.rstrip("/") + "/"
        try:
            req = urllib.request.urlopen(path + "robots.txt", data=None)
            return str(req.read(), 'utf-8')
        except Exception as e:
            return f"Error fetching robots.txt: {e}"

    robots_txt_content = get_robots_txt(url)
    print(robots_txt_content)

    def check_wordlist(robots_txt_content, wordlist_file):
        with open(wordlist_file, 'r') as file:
            wordlist = [line.strip() for line in file]

        for word in wordlist:
            if word.lower() in robots_txt_content.lower():
                return True
        return False

    default_wordlist_file = "wordlist.txt"

    if check_wordlist(robots_txt_content, default_wordlist_file):
        print("Potential sensitive information found in robots.txt!")
    else:
        print("No sensitive information found in robots.txt.")

    print("What's next comrade?")

    print("[1]. Back to base!")
    print("[2]. There is always time for Cyboogie!")
    print("[3]. We need R&D!")
    print("[4]. Survery their ports!")
    print("[5]. Launch it!")
    print("[6]. Exit")

    selection = input("Choose wisely: ")

    if selection == "1":
        import Harpocratic_Blackbird
    elif selection == "2":
        # Continue to the next iteration of the loop
        continue
    elif selection == "3":
        import DNS_Converter
    elif selection == "4":
        import BackDoorothy
    elif selection == "5":
        import DoS
    elif selection == "6":
        sys.exit()
    else:
        print("Invalid Selection. Enter 1-6.")
