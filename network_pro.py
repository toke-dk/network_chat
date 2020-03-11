from socket import*
import os
host_input = input("Hvilken ip har din makker? ")
host = f'{host_input}'
port = 12345

s = socket(AF_INET, SOCK_STREAM)

s.connect((host, port))

while True:
    data = s.recv(1024)
    print(data.decode())
# print(data.decode())