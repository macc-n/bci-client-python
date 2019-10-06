import socket


class TCPClient:

    def __init__(self, address, port):
        self.fail = False
        self.stopChar = ';'

        self.address = address
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (address, port)
        try:
            self.sock.connect(address)
        # except ConnectionError:
        except Exception:
            print("Impossibile stabilire la connessione")
            self.fail = True

    def send_message(self, message):
        self.sock.sendall(message + self.stopChar)

    def close_socket(self):
        self.sock.close()
