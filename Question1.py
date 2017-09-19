# Adapted from: https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip

# Reading in the gz files
f = gzip.open('Data/t10k-images-idx3-ubyte.gz', 'rb')
g = gzip.open('Data/t10k-labels-idx1-ubyte.gz', 'rb')
h = gzip.open('Data/train-images-idx3-ubyte.gz', 'rb')
i = gzip.open('Data/train-labels-idx1-ubyte.gz', 'rb')

# The amount of bytes you want to read in eg. 4.
magic = f.read(4)
magic1 = g.read(4)
magic2 = h.read(4)
magic3 = i.read(4)

# This prints: b'\x00\x00\x08\x03'
# In binary, this is: 00000000 00000000 00001000 00000011

# Picture 1
print("This is the amount of bytes in this file.")
print( "They are displayed below in hexadecimal:")
print(type(magic))
print(magic)

# Picture 2
print("This is the amount of bytes in this file. They are displayed below in hexadecimal")
print( "They are displayed below in hexadecimal:")
print(type(magic1))
print(magic1)

# Picture 3
print("This is the amount of bytes in this file. They are displayed below in hexadecimal")
print( "They are displayed below in hexadecimal:")
print(type(magic2))
print(magic2)

#Picture 4
print("This is the amount of bytes in this file. They are displayed below in hexadecimal")
print( "They are displayed below in hexadecimal:")
print(type(magic3))
print(magic3)

# int.from_bytes(magic, "big") -> for iPython

# print(int.from_bytes(magic, ))