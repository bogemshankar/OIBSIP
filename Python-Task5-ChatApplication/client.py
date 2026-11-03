import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
        except OSError:
            break

        if not data:
            print("\nDisconnected from the server.")
            break

        print("\n" + data.decode("utf-8").strip())


def main():
    username = ""
    while not username:
        username = input("Enter your name: ").strip()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Could not connect. Please start server.py first.")
        return

    sock.sendall(username.encode("utf-8"))
    print("Connected! Type a message and press Enter. Type 'quit' to leave.")
    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

    try:
        while True:
            message = input()
            if message.lower() == "quit":
                break

            if message.strip():
                sock.sendall(message.encode("utf-8"))

    except (KeyboardInterrupt, EOFError):
        pass

    finally:
        sock.close()
        print("You left the chat.")


main()
