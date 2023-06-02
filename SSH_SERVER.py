import os
import paramiko
import socket
import sys
import threading

CWD = r'C:\path\keys'
HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD, 'test_rsa.key'), password='pass')

class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == 'use') and (password == 'pass'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def start_shell(self, channel):
        channel.send('Welcome to the server!\n')
        while True:
            try:
                command = channel.recv(1024).decode().strip()
                if command.lower() == 'exit':
                    channel.send('Exiting.\n')
                    break
                output = self.execute_command(command)
                channel.send(output + '\n')
            except Exception as e:
                channel.send('An error occurred: ' + str(e) + '\n')
                break

    def execute_command(self, command):
        # Add your command execution logic here
        return 'Command execution result: ' + command.upper()

if __name__ == '__main__':
    server = '192.168.0.1'
    ssh_port = 22

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server, ssh_port))
        sock.listen(100)
        print('[+] Listening for connection ...')
        client, addr = sock.accept()
        print('[+] Got a connection!', client, addr)

        bhSession = paramiko.Transport(client)
        bhSession.add_server_key(HOSTKEY)

        server = Server()
        try:
            bhSession.start_server(server=server)
        except paramiko.SSHException as e:
            print('[-] SSH negotiation failed:', str(e))
            sys.exit(1)

        chan = bhSession.accept(20)
        if chan is None:
            print('*** No channel.')
            sys.exit(1)

        print('[+] Authenticated!')
        server.start_shell(chan)

    except KeyboardInterrupt:
        print('[-] Server terminated by user.')
        sys.exit(1)
    except Exception as e:
        print('[-] Error:', str(e))
        sys.exit(1)
