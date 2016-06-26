'''
    Simple socket server using threads
'''
 
import socket
import sys
from thread import *
 
HOST = ''   
PORT = 5100  
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
k=0
t=[]
p=0
j=0
n=0
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    #conn.send('Welcome to the server.') #send only takes string
    for k in range(i-1):
        conn.sendall(str(arr2[k]))
    for j in range(i-1): 
       # arr[j].sendall('new connections  connected to network are: ')
        arr[j].sendall(str(c))
    #conn.sendall("Which client do you want to connect to? enter his address\n")
    address = conn.recv(1024)
    t.append(conn)
    n=0
    for n in range(i):
        if (address == arr2[n]):
            arr2[n]=arr[n]
            t.append(arr2[n])
            #infinite loop so that function do not terminate and thread do not end.
    while True:
    
            data=conn.recv(1024)
            
        
            if conn == t[0]:
                conn = t[1]
                conn.sendall(data)
                conn = t[0]
            elif conn == t[1]:
                conn = t[0]
                conn.sendall(data)
                conn = t[1]
            if not data: 
                break
        
         
        
     
    #came out of loop
    conn.close()
arr =[] # this is to keep track of users
c=0
arr2=[]
i=0
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    arr.append(conn)
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    arr2.append(str(addr[1]))
    c=addr[1]
    
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
    
    i += 1
 
s.close()
