# run: pip install IPy :in terminal if in replit.
# First version

import socket

from IPy import IP

try:
    s = socket.socket()
    port = int(input("Port: "))
    ipaddr = input("IP: ")
    s.connect((ipaddr, port))

except socket.error:
    print("Socket connection error occurred")
except ValueError:
    print("Invalid port number. Please enter a valid integer")
except Exception as e:
    print("An error occurred:", e)

