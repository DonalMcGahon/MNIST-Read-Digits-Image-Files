import gzip
import io

def read_images_from_file(file):
    with gzip.open(file, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("magic is: ", magic)
        
        noimg = f.read(4)
        noimg = int.from_bytes(noimg, 'big')
        print("number of labels: ", noimg)

        norow = f.read(4)
        norow = int.from_bytes(norow, 'big')
        print("number of rows: ", norow)
        
        nocol = f.read(4)
        nocol = int.from_bytes(nocol, 'big')
        print("number of cols: ", nocol)    
        
        
        images = []
        
        for i in range(noimg):
            rows = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                rows.append(cols)
            images.append(rows)
            
        return images

            
train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')

for row in train_images[4999]:
    for col in row:
        print('.' if col <= 127 else '#', end='')
    print()