import socket

def start_tcp_server(host, port):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific address and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        
        # Receive and send data
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            
            message = data.decode()
            print(f"Received from client: {message}")
            
            # Process the received message
            response = process_message(message)
            
            # Send the response back to the client
            client_socket.sendall(response.encode())
        
        # Close the client socket
        client_socket.close()

def process_message(message):
    # Process the message received from the client
    # You can implement your custom logic here
    # For example, you can do some calculations, database operations, etc.
    response = "Server response: " + message
    return response

# Start the server
start_tcp_server('127.0.0.1', 8080)
