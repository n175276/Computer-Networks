#!/usr/bin/python
import socket 
import sys
import threading

#print_lock = threading.Lock()
#collecting nickname and server port from cm line 
username = sys.argv[2]
Port_no = int(sys.argv[1])

#connecting to server
serverName = '127.0.0.1'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverName,Port_no))

#collecting message and sending username to server
def receive():
   while True:
        message = client.recv(1024).decode('ascii')
        if message == 'NAME':
            client.send(username.encode('ascii'))          
        else:
            print('==>',message)

#sending client messages to server 
def write():
    while True:
        mess = input('')
        message = ('{}: {}'.format(username, mess))
        client.send(message.encode('ascii'))
        # print_lock.acquire()
        
        




# Starting Threads For Listening And Writing       
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
#receive()
#write()
# receive_thread.join()
# write_thread.join()
# print("Write Message : ")