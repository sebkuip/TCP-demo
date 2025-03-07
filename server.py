import socket
import threading

running = False
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 12345))
serversocket.listen(5)

def listen():
    while running:
        socket, address = serversocket.accept()
        client = ServerConnection(socket, address)
        client.start_listening()
        print(f"new connection from {address}")

class ServerConnection():
    def __init__(self, client, address):
        self.client: socket.socket = client
        self.address = address
        self.connected = False
        self.listen_thread = threading.Thread(target=self.loop)

    def send(self, message):
        self.client.send(message.encode())

    def receive(self):
        if not self.connected:
            return self.client.recv(1024).decode()
        else:
            raise ConnectionError("Client is not connected")

    def close(self):
        print(f"closing connection {self.address}")
        self.connected = False
        self.client.close()

    def loop(self):
        while self.connected:
            try:
                message = self.receive()
                print(f"message from {self.address}: {message}")
                if message == "close":
                    self.close()
            except ConnectionError:
                print("connection closed")
                break

    def start_listening(self):
        self.connected = True
        self.listen_thread.start()

if __name__ == "__main__":
    print("starting server")
    running = True
    listen()