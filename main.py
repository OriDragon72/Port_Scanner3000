import socket

from art import text2art

print("Welcome to: ")
print(text2art("ScanP.3000"))

CommonPs = {
    20: "FTP", 
    21: "FTP", 
    22: "SSH", 
    23: "Telnet", 
    25: "SMTP", 
    53: "DNS", 
    80: "HTTP", 
    110: "POP3", 
    443: "HTTPS", 
    3306: "MySQL", 
    8080: "HTTP Proxy", 
    8443: "HTTPS"
}
ports = list(CommonPs.keys())

def scan(t, p):
  sock = None
  try:
    sock = socket.socket()
    sock.settimeout(1)
    sock.connect((t, p))
    b = sock.recv(1024)
    print(f"Port {p} is open on {t} with banner: {b}")
  except Exception as e:
    print("An error occurred:", e)
  finally:
    if sock:
      sock.close()
      
answer = input("Would you like to scan a port? (y/n): ")

if answer == "y":
  print("Would you like to use [n]ormal (IP)")
  print("or [a]dvance (DNS) formatting for the website?")
  
  a = input("(n/a): ")
  
  if a == "n":
    tarGet = input("Enter target website in format '##.##.##.##': ")
    
    for port in ports:
      scan(tarGet, port)
      
  elif a == "a":
    target = input("Enter target website in format 'www.example.com': ")
    targetIp = socket.gethostbyname(target)
    
    for port in ports:
      scan(targetIp, port)
      
  else:
    print("Invalid input. Please enter 'n' or 'a'.")
    exit()
    
elif answer == "n":
    print("Okay, goodbye!")
    exit()
  
else:
    print("Invalid input. Please enter 'y' or 'n'.")
    exit()

print("Scan complete!")
