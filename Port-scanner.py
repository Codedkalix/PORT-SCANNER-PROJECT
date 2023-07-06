import socket
import sys
import pyfiglet
from datetime import datetime

banner = pyfiglet.figlet_format("Port Scanner")
print(banner)

target = input("Please Enter Host To Scan: ")
host = socket.gethostbyname(target)

try:
    file = open("Port-scan-2.txt","w")
except FileExistsError:
    print("File Exists Error")
    sys.exit()    

date = datetime.date(datetime.now())
t1 = datetime.now()

print("Start Time: {}".format(t1.strftime("%H:%M:%S:")))
file.write("Start Time: {}\n".format(t1.strftime("%H:%M:%S:")))
try:

    for port in range(1, 1025):
        # AF_INET means IPv4 addresses. AF_INET6 means IPv6 address
        # SOCK_STREAM means we are using TCP Connection. SOCK_DGRAM for UDP 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.001)
        result = sock.connect_ex((host, port))
        if result == 0 :
            try:
                print("Port No : {} Open Protocol Service Name: {}".format(port, socket.getservbyport(port, "tcp")))
                file.write("\nPort No : {} Open Protocol Service Name: {}".format(port, socket.getservbyport(port, "tcp")))
            except socket.error:
                print("Port No : {} Open Protocol Service Name: {}".format(port, "unknown"))
                file.write("\nPort No : {} Open Protocol Service Name: {}".format(port, "unknown"))

except socket.gaierror:
    print("Hostname could not be resolved. Existing")
    file.write("\n\nHostname could not be resolved. Existing")
    sys.exit
except socket.error:
    print("Couldn't connect to server. Existing")
    file.write("\n\nCouldn't connect to server. Existing")    
    sys.exit

t2 = datetime.now()

print("\n\nEnd Time: {}".format(t2.strftime("%H:%M:%S:")))
file.write("\n\nEnd Time: {}".format(t2.strftime("%H:%M:%S:")))

Total_time = t2 - t1

print("\n\nTotal_time: {}".format(Total_time))
file.write("\n\nTotal_time: {}".format(Total_time))


            