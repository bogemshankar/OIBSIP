import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000

clients = {} # socket -> username
lock = threading.Lock()


def timestamp():
    return datetime.now().strftime("[%H:%M]")


def broadcast(message, sender=None):
    """Send a message to every connected client except the sender."""
    with lock:
        for client in list(clients):
            if client is not sender:
                try:
                    client.sendall(message.encode("utf-8"))
                except OSError:
                    pass


def handle_client(conn, addr):
    try:
        username = conn.recv(1024).decode("utf-8").strip() or "Unknown"
    except OSError:
        conn.close()
        return

    with lock:
        clients[conn] = username

    print(f"{timestamp()} {username} connected from {addr[0]}:{addr[1]}")
    broadcast(f"{timestamp()} * {username} joined the chat *\n")

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            text = data.decode("utf-8").strip()
            if text:
                broadcast(f"{timestamp()} {username}: {text}\n", sender=conn)

    except OSError:
        pass

    finally:
        with lock:
            clients.pop(conn, None)

        conn.close()
        print(f"{timestamp()} {username} disconnected")
        broadcast(f"{timestamp()} * {username} left the chat *\n")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server is listening on {HOST}:{PORT} ... (press Ctrl+C to stop)")

    try:
        while True:
            conn, addr = server.accept()
            threading.Thread(
                target=handle_client,
                args=(conn, addr),
                daemon=True
            ).start()

    except KeyboardInterrupt:
        print("\nServer stopped.")

    finally:
        server.close()


main()
