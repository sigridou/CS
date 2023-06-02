import paramiko

def connect_to_server():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect('192.168.0.1', port=22, username='use', password='pass')

        while True:
            command = input("Enter command: ")
            if command.lower() == 'exit':
                break

            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode()
            print(output)

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check the username and password.")
    except paramiko.SSHException as e:
        print("Error occurred while connecting:", str(e))
    finally:
        client.close()

if __name__ == '__main__':
    connect_to_server()
