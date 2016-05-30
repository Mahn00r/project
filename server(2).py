'''
    Simple socket server using threads
'''
 
import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5150# Arbitrary non-privileged port
 
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
BUFSIZE = 1024
t=[]
#Function for handling connections. This will be used to create threads
def clientthread(conn,):
    #Sending message to connected client
	n = len(arr)
	while n:
                n -= 1
                arr[n]['con'].send('Welcome to the server. Enter Id of User You want to chat with\n')
                
        t.append(conn)
	address=conn.recv(200)
	print address
	t.append(conn)
	#print arr[loop]['con']
       
	while True:
                data=conn.recv(BUFSIZE)
                if conn == t[0]:
                    conn = t[1]
                    conn.send(data)
                    conn = t[0]
                elif conn == t[1]:
                    conn = t[0]
                    conn.send(data)
                    conn = t[1]
                if not data: 
                    break
        
                
    #came out of loop
	conn.close()


#This Function will show the list of all connected users
def ShowAllUser(conn):
        i=0;
	n = len(arr)
	while n:
		n -= 1
		conn.send(str(i+1) + ':' + arr[n]['nam']+"  (connected)\n")
		i += 1
	return
	

#This Function WIll Show to All User About New Connection
def ShowToAll(temp):
	n = len(arr)
	i=0;
	while n:
		n -= 1
		arr[n]['con'].send( a['nam'] + "(Now Connected)\n")
                i += 1
	return

arr =[] # this is to keep track of users
i = 0

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    a = {}
    a['con'] = conn
    a['adr'] = addr
    a['nam'] = conn.recv(200)
    ShowToAll(a)
    arr += [a]
    ShowAllUser(conn)
    #print arr
   
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
    i += 1
 
s.close()

