import socket


ascii_banner = ("NSLookup")
print(ascii_banner.center(80, "-"))


hostname = input("Please enter target website address:\n")


#IP lookup from hostname
print(f' {hostname} Ip Address is {socket.gethostbyname(hostname)}')
