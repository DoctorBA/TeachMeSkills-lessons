import socket 


def server():
    host = socket.gethostname()
    port = 5000
        
    server_socet = socket.socket()    
    server_socet.bind((host, port))
    
    server_socet.listen(2)
    print(f'Waiting for connection...')
    conn, address = server_socet.accept()
    print(f'Connection from: {str(address)}')
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        
        print(f'From connected user {str(address)}: {str(data)}')
        data = input('-->')
        conn.send(data.encode())
        
    conn.close()    
        
server()        
