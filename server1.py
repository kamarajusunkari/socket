import socket
import sys
host = socket.gethostname()
port = 9999
s = socket.socket()
print('binding the port' + str(port))
s.bind((host, port))
s.listen(5)


conn, add = s.accept()
print('connection has been established' + 'IP' + add[0] + 'port' + str(add[1]))

while True:
    cmd = input()
    if cmd == 'quit':
        conn.close()
        s.close()
        sys.exit()
    if len(str.encode(cmd)) > 0:
        conn.send(str.encode(cmd))
        client_response = str(conn.recv(1024), 'utf-8')
        print(client_response, end=" ")
