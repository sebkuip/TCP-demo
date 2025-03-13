import socket
import threading

def listen():
    while True:
        socket, address = serversocket.accept()
        client = ServerConnection(socket, address)
        client.start_listening()
        print(f"new connection from {address}")

class ServerConnection():
    def __init__(self, sock, address):
        self.socket: socket.socket = sock
        self.address = address
        self.connected = False
        self.listen_thread = threading.Thread(target=self.loop)

    def send(self, message):
        self.socket.send(message.encode())

    def receive(self):
        if self.connected:
            return self.socket.recv(1024).decode()
        else:
            raise ConnectionError("Client is not connected")

    def close(self):
        print(f"closing connection {self.address}")
        self.connected = False
        self.socket.close()

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
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('', 12345))
    serversocket.listen(5)
    print("starting server")
    listen()
