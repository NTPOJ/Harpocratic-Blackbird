#Imported modules
import urllib.request
import io

ascii_banner = ("Lets see some robots")
ascii_banner = ("Boston Dynamic Rogue-1")
print(ascii_banner)

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
