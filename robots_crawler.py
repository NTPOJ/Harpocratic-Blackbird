#Imported modules
import pyfiglet
import urllib.request
import io
import colorama
from colorama import Fore
colorama.init() 

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
