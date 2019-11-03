import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1255
s.bind((host,port))
#max 5 clients can be accepted
s.listen(5)

#accept connection with client
socketclient, address = s.accept()

##print("Got Connection from", address)
con = True
while con:
    msg = socketclient.recv(1024)
    msg = msg.decode('utf-8')
    print(msg)
    if msg =='quit':
         s.close()