from concurrent.futures import thread
import socket
import threading

from queue import Queue
queue = Queue()
open_ports = []

target = input(
    "Enter destination ip->""")  # target ip is requested from user


def portscan(port):
    try:

        # use of sockets required for communication
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def fill_queue(port_list):  # adding to the queue

    for port in port_list:
        queue.put(port)


def worker():
    while not queue.empty():  # process of calling ports in the queue

        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)


port_list = range(1, 1080)
fill_queue(port_list)

thread_list = []

for t in range(200):  # performing multithread operation
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:  # starting thread
    thread.start()


# the other thread does not start until the thread is finished.
for thread in thread_list:
    thread.join()


print("Open ports are:", open_ports)
