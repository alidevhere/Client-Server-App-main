import socket

HEADER = 64
PORT = 12345
FORMAT = 'utf-8'
SERVER = '127.0.0.1'
ADDR = (SERVER,PORT)
FILE_NAME='data.txt'

def receive_file():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
    file_len = client.recv(HEADER).decode(FORMAT)
    print('file len ',file_len,'  ',int(file_len))
    print(len(file_len))
    if file_len:
        file_data = client.recv(int(file_len)).decode(FORMAT)
        #print(file_data)
        f = open(f'client\{FILE_NAME}','w')
        f.write(file_data)
        f.close()
    




receive_file()
