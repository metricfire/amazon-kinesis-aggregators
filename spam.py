#!/usr/bin/python
import time
import socket
import random
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('hi')

while True:
    value = random.random() * 100
    payload = "77777777-9999-4444-8888-999999999999.metric.abc {}\n".format(value)
    print('sending: {}'.format(payload))
    sock.sendto(payload.encode('utf-8'), ("localhost", 30666))
    time.sleep(0.2)
