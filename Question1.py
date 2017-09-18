# Adapted from: https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip

f = gzip.open('Data/t10k-images-idx3-ubyte.gz', 'rb')

firstbyte = f.read(1)

print (firstbyte)