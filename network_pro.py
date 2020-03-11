from socket import*
import os

host = '0.0.0.0'
port = 12345

s = socket(AF_INET, SOCK_STREAM)

s.connect((host, port))

while True:
    data = s.recv(1024)
    print(data.decode())
# print(data.decode())