#!/usr/bin/python
import socket 
import sys
import threading

# print_lock = threading.Lock()

#starting server
Port_no = int(sys.argv[1])
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('',Port_no))
server.listen()

#message to server that server is running           
print("The server is ready....")

# list of client and username
clients = []
usernames = []

#function to broadcast message to all clients
def broadcast(message):
    for client in clients:
       client.send(message)
    # client.send('\nWrite Message : '.encode('ascii'))

#function to collect message and broadcast it    
def messages(client):
   while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = usernames[index]
            usernames.remove(nickname)
            print('{} Disconnected !'.format(nickname))
            broadcast('{} left! <=='.format(nickname).encode('ascii'))
            break



#to receive client info and start thread

while True:
    client,addr = server.accept()
    print("Connected with {}".format(str(addr)))

    #sending message to client to send username
    client.send('NAME'.encode('ascii'))
    name = client.recv(1024).decode('ascii')
    #adding username and client to respective list
    usernames.append(name)
    clients.append(client)
       
    #printing message that client is added
    print('name of client is {}!!!'.format(name))
    client.send('connected to server...'.encode('ascii'))
    broadcast('{} joined the chat!'.format(name).encode('ascii'))
       
    #handling thread
    thread = threading.Thread(target=messages,args=(client,))
    thread.start()
    #thread.join()



