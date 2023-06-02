import socket

def start_tcp_client(host, port):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")

        while True:
            # Send message to the server
            message = input("Enter a message to send (or 'quit' to exit): ")
            client_socket.sendall(message.encode())

            # Check if the client wants to quit
            if message.lower() == 'quit':
                break

            # Receive the response from the server
            response = client_socket.recv(1024)
            print(f"Received from server: {response.decode()}")

    finally:
        # Close the socket
        client_socket.close()

# Start the client
start_tcp_client('127.0.0.1', 8080)
