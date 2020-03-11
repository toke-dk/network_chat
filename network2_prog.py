from socket import*

HOST = '192.168.0.255'
PORT = 12345

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

conn, addr = s.accept()

while True:
    msg = input("msg: ")
    conn.send(msg.encode())

