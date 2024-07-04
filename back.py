import socket
import ssl
import threading

class IRCClient:
    def __init__(self, server, port, nickname, channel, gui_callback):
        self.server = server
        self.port = int(port)
        self.nickname = nickname
        self.channel = channel
        self.gui_callback = gui_callback
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        try:
            context = ssl.create_default_context()
            self.sock = context.wrap_socket(self.sock, server_hostname=self.server)
            self.sock.connect((self.server, self.port))
            self.sock.send(f"NICK {self.nickname}\r\n".encode('utf-8'))
            self.sock.send(f"USER {self.nickname} 0 * :{self.nickname}\r\n".encode('utf-8'))
            self.sock.send(f"JOIN {self.channel}\r\n".encode('utf-8'))

            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()

            threading.Timer(1.5, self.clear_chat).start()
        except Exception as e:
            print(f"Failed to connect: {str(e)}")

    def send_message(self, message):
        if message.strip():
            if self.channel.startswith('#'): 
                prefix = "[BRIDGE] username/irc:"
            else: 
                prefix = "[BRIDGE] username/discord:"
            
            full_message = f"{prefix} {message}"

            # Send raw message to IRC server
            self.sock.send(f"PRIVMSG {self.channel} :{message}\r\n".encode('utf-8'))

            # Pass prefixed message to GUI callback
            self.gui_callback(full_message)

    def receive_messages(self):
        while True:
            try:
                message = self.sock.recv(2048).decode('utf-8')
                if not message:
                    break
                if message.startswith('PING'):
                    self.sock.send('PONG\r\n'.encode('utf-8'))
                elif message:
                    self.gui_callback(message.strip()) 
            except Exception as e:
                print(f"Error receiving message: {str(e)}")
                break

    def stop(self):
        self.sock.close()

    def clear_chat(self):
        self.gui_callback("")  

if __name__ == "__main__":
    def gui_callback(message):
        print(f"Updating GUI with message: {message}") 

    server = input("Server: ")
    port = input("Port: ")
    nickname = input("Nickname: ")
    channel = input("Channel: ")

    client = IRCClient(server, port, nickname, channel, gui_callback)
    client.start()
