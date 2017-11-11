import socket
import sys 

host        = raw_input("Host name i.e. www.google.com: ")
sPort,ePort = map(int,raw_input("Port range <0,65535> i.e. 25 80: ").split())

try:
    host_ip = socket.gethostbyname(host)
except socket.gaierror:
    print "There was an error resolving the host"
    sys.exit()

print "Scaning ports in range",sPort,ePort

ports = []
for port in range(sPort,ePort+1):
    if port < 0 or port > 65535:
        print "Not in range <0, 65535>"
        break
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host_ip, port))
        print "Open port:",port
        ports.append(port)
        s.close()
    except Exception:
        print "Error",port

print "Open ports at %s: %s"%(host, ports)

'''for testing www.portquiz.net'''
