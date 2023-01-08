#! /usr/bin/python3
# portBannerGrab.py

import socket                       # import the socket module

Ports = [21, 22, 25, 3306]          # place the port numbers you want to scan here

for Port in Ports:
    try:
        s = socket.socket()             # create an object named 's' instantiated from the socket class to the socket module
        print('This is the Banner for the Port')
        print(Port)
        
        # use the connect() method from the socket module make connection to ip address and port
        # syntax is object.method (for example, socket.connect)
        s.connect(("127.0.0.1", Port))  # set to scan localhost on 'Port, change target IP as needed

        answer = s.recv(1024)           #use receive (recv) method to read 1024 bytes of data, contains the banner information, assign as answer

        print(answer)                       

        s.close()
    except ConnectionRefusedError:
        print('Connection Refused for Port: ')
        print(Port)
