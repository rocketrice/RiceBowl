import socket

HOST = ""
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST,PORT))
    print "[+] Server Bound"

    s.listen(1)
    print "[+] Listening for connection"

    conn, addr = s.accept()
    print "[+] Connection received from " + str(addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print "[+] Message recieved: " + str(data)



    while True:
        conn.close()
        s.listen(1)
        conn, addr = s.accept()
        cmd = raw_input()
        conn.send(cmd)

        data = conn.recv(2048)
        print str(data)

except ValueError:
    "[-] something went wrong"
    s.close()