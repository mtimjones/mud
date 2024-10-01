import socket
import threading

def handle_client(client_socket, client_address):

    print(f"Accepted connection from {client_address}")

    while True:

        try:
            data = client_socket.recv(128)

            if not data:
                break

            message = data.decode().rstrip()
            if message != "":
                print(f"Received from {client_address}: {message}")

                # Process the message and send a response
                response = f"Echo: {message}"
                client_socket.send(response.encode())

        except ConnectionResetError:
            break

    client_socket.close()
    print(f"Connection closed with {client_address}")

def start_server(client):

    host = "127.0.0.1"  # Listen on localhost
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:

        client_socket, client_address = server_socket.accept()

        # Create a new thread to handle the client
        thread = threading.Thread(target=client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":

      start_server(handle_client)

