import socket
import threading

class ClientConnection:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        self.listen_thread = threading.Thread(target=self.loop)

    def connect(self, address):
        self.client.connect(address)
        self.connected = True
        self.listen_thread.start()

    def send(self, message):
        self.client.send(message.encode())

    def receive(self):
        if self.connected:
            return self.client.recv(1024).decode()
        else:
            raise ConnectionError("Client is not connected")

    def close(self):
        self.connected = False
        self.client.close()

    def loop(self):
        while self.connected:
            try:
                message = self.receive()
                print(f"message from server: {message}")
                if message == "close":
                    self.close()
            except ConnectionError:
                break

if __name__ == "__main__":
    client = ClientConnection()
    client.connect(("localhost", 12345))
    while True:
        message = input("message: ")
        client.send(message)
        if message == "close":
            client.close()
            break