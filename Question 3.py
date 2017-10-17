# Adapted from: https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
# Adapted from: https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar
import gzip
import io
import numpy as np

# Reading in label file
def read_labels_from_file(filename) :
    with gzip.open(filename, 'rb') as f:
        # The amount of bytes you want to read in eg. 4.
        magic = f.read(4)
        # reading in magic number
        magic = int.from_bytes(magic, 'big')
        print("magic is: ", magic)
        
        # The amount of bytes you want to read in eg. 4.
        noimg = f.read(4)
        # reading in noimg number
        noimg = int.from_bytes(noimg, 'big')
        print("number of labels: ", noimg)
        
        # reading in labels
        labels = [f.read(1) for i in range(noimg)]
        labels = [int.from_bytes(label, 'big') for label in labels]
        
        return labels


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
    
    

# Reading in train-images & t10k images            
train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')
test_images = read_images_from_file('data/t10k-images-idx3-ubyte.gz')

# Changing train_images to display as PDF and saving the pdf
import PIL.Image as pil
img = train_images[4999]
img = np.array(img)
img = pil.fromarray(img)
img = img.convert('RGB')
img.show()
img.save('Question3 Images/train-04999-2.png')

# Changing train_images to display as PDF and saving the pdf
import PIL.Image as pil
img = test_images[4999]
img = np.array(img)
img = pil.fromarray(img)
img = img.convert('RGB')
img.show()
img.save('Question3 Images/test-04999-2.png')