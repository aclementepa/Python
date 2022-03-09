import socket
import time
import sys
import os
import subprocess

s = socket.socket()
host = socket.gethostname()
port = 8081
s.bind(('', port))

print("waiting for connections...")
s.listen()
conn, addr = s.accept()
print(addr, "is connected to server")
terminated='n'
while(terminated == 'n'):
    command = input(str("Enter Command: "))
    # ssh = subprocess.Popen(["ssh", "%s" % ])
    conn.send(command.encode())
    print("Command has been sent successfully.")
    data = conn.recv(1024)
    data = data.decode()
    if data:
        print(data)

    terminated = input(str("Are you done? (y/n) "))
    conn.send(terminated.encode())
print("Process Terminated")