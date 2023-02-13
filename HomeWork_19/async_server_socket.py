import select
import socket
import queue
import requests

 
host = socket.gethostname()
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind((host, port))

print(f'Waiting for connection...')
server.listen(2)
inputs = [server]
outputs = []
message_queues = {}

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs,  message_queues)

    for s in readable:
        if s is server:
            connection, address = s.accept()
            inputs.append(connection)
            message_queues[connection] = queue.Queue()
            print(f'New connected user {str(address)}')
        else:
            data = s.recv(1024)
            if data:
                print(f'From connected user {str(address)}: {str(data.decode())}')
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]    
                
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait().decode()
            if 'https://' not in next_msg:
                next_msg = 'https://' + next_msg 
            next_msg = requests.get(next_msg).text 
            s.sendall(next_msg.encode()) 
            print(f'Sended to connected user {str(address)}: {str(next_msg)}')     
        except queue.Empty:     
            outputs.remove(s)
                               
                    
    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
           outputs.remove(s)
        s.close()
        del message_queues[s]     
        
