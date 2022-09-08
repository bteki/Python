import socket
import sys

# Create socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()  # add comment ...

    except socket.error as msg:
        print('Socket creation error: ' + str(msg))


# Binding socket and listen for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print('Binding the port ' + str(port))

        s.bind((host, port))  # add comment ...
        s.listen(5)  # add comment ...

    except socket.error as msg:
        print('Socket binding error' + str(msg) + '\n' + 'Retrying ...')
        bind_socket()

    # Establish connection with client


def socket_accept():
    conn, address = s.accept()  # add comment ...
    print('Connection has been established |' + ' IP ' + address[0] + ' | Port ' + str(address[1]))
    send_commands(conn)
    conn.close()


# Send command to client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()  # add comment ...
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
