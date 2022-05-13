#!/usr/bin/env python3

from constants import HOST, PORT
import socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print(f'Received {data!r}')

if __name__ == '__main__':
    main()
