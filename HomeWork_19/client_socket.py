import socket 


def client():
    host = socket.gethostname()
    port = 5000
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    message = ''
    
    while message != 'close':
        message = input('-->')
        client_socket.sendall(message.encode())
        
        data = client_socket.recv(1024).decode()
        print(f'Recieved from server: {data}')
        
    client_socket.close()
    
client()        