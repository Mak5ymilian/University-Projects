import socket
import threading

host = '127.0.0.1'  # localhost
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()  # listens for connections

clients = []
nicknames = []


def broadcast(message):  # broadcasts messages to all clients from the server
    for client in clients:
        client.send(message)


def handle(client):  # Checks for messages from client to post to all clients
    while True:  # While loop constantly checks for messages
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the server. '.encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = s.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)

        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the server!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()
