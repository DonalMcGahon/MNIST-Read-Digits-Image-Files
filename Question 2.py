# Adapted from: https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
# Adapted from: https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar
import gzip
import io

# Reading in image file
def read_images_from_file(file):
    with gzip.open(file, 'rb') as f:
        # The amount of bytes you want to read in eg. 4.
        magic = f.read(4)
        # reading in magic number
        magic = int.from_bytes(magic, 'big')
        print("magic is: ", magic)
        
        # reading in the number of labels in the image file
        noimg = f.read(4)
        noimg = int.from_bytes(noimg, 'big')
        print("number of labels: ", noimg)
        
        # reading in the number of rows in the image file
        norow = f.read(4)
        norow = int.from_bytes(norow, 'big')
        print("number of rows: ", norow)

        # reading in the number of columns in the image file
        nocol = f.read(4)
        nocol = int.from_bytes(nocol, 'big')
        print("number of cols: ", nocol)    
        
        
        images = []
        # Creating an array for the number of rows
        for i in range(noimg):
            rows = []
            # Creating an array for the number of columns
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                rows.append(cols)
            images.append(rows)
            
        return images

# Reading in train-images            
train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')
# When the number of rows in train_images is less than 4999
for row in train_images[4999]:
    # Any pixel value less than 128 is displayed as a full stop and any other pixel value is displayed as a hash symbol
    for col in row:
        print('.' if col <= 127 else '#', end='')
    print()