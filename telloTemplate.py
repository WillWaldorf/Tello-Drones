# TelloTemplate - Mason Fisher
# The starting point for your Tello projects
# Some parts from Tello3.py
# Made on Feb 9th 2019
#
# This program is in the public domain

import threading
import socket
import sys
import time

host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)

def recv():
    # Message receiver
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

def sendmsg(msg, delay):
    # Message sender
    # msg is the message we want to send
    # delay is if we want to add a delay (normally we want to)
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sent = sock.sendto(msg, tello_address)
    if delay == True:
        time.sleep(5)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()
print("Starting!")
time.sleep(1)
sendmsg("command", False) # Tell the drone if it's ready to recive commands

# Commands go here, see SDK documentation for info

print("Done!")
sock.close()
