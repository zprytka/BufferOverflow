#!/usr/bin/env python3

import socket, time, sys

ip = "127.0.0.1"

port = 4444
timeout = 5
prefix = ""

string = b'A' * 50

while True:
  try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(timeout)
      s.connect((ip, port))
      print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
      print(s.recv(1024))
      s.send(b'Administrator'+b'\r\n')
      print(s.recv(1024))
      s.send(string + b'\r\n')
      print(s.recv(1024))
  except:
    print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
    sys.exit(0)
  string += b'A' * 50
  time.sleep(1)
