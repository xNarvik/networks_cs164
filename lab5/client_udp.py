import socket
import sys

#create dgram socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print "Failed to creat socket"
    sys.exit()

host = "foxtrot-3"
port = 8888 #4367

while(1):

    
    try:
        #Set string
        s.sendto(msg, (host,port))

        #receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print "Server reply :" + reply

    except socket.error, msg:
        print "Error: " + str(msg[0]) + " Message " + msg[1]
        sys.exit()
        
