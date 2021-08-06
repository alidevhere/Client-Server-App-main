import socket
import threading
import os


HEADER = 64
PORT = 12345
FORMAT = 'utf-8'
DISCONNECT = 'DISCONNECT'
FILE_NAME='data.txt'

#SERVER = str(socket.gethostbyname(socket.gethostname()))
#SERVER = '127.0.0.1'
#SERVER = '119.160.97.67'
SERVER = ''
ADDR = (SERVER,PORT)
server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Starting Server...')
server.bind(ADDR)

def start_server():
    print('Server address : ',ADDR)
    print(print(FORMAT))
    server.listen()
    
    print('waiting for connections..')
    while True:
        conn,addr = server.accept()
        try:
            print('connected with {addr}')
            filename='data.txt'
            send_file(conn,addr,FILE_NAME)
            print('file sent....')

        except:
            print('Exception: Exception occured while establishing connection.')


def send_file(conn,addr,path):
    print(f'[ FILE TRANSFER ] {addr} requested for file "{path}" ')
    f = open(f'server\{path}','r')
    file = f.read()
    file_len = str(len(file))
    file_len += ' '* (HEADER - len(file_len))
    
    print('[ STATUS ] : sending file...')
    #print(file)
    print('\n',len(file))
    
    # sending file length as header
    conn.send(bytes(file_len,FORMAT))
    # sending complete file
    conn.send(bytes(file,FORMAT))
    print(f'[ COMPLETED ] : file "{path}" sent successfully to {addr}.')


start_server()




