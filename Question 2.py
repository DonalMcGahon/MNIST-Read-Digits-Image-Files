'''from mnist import MNIST

mndata = MNIST('train-images-idx3-ubyte.gz')

images, labels = mndata.load_training()

index = random.randrange(0, len(images))
print(mndata.display(images[index]))'''

import gzip

# Reading in the gz files
# with gzip.open('Data/t10k-labels-idx1-ubyte.gz', 'rb') as f:
def read_labels_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic is:", magic)
        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("Number of labels is:", nolab)
        
        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label, 'big') for label in labels]

return labels

train_labels = read_labels_from_file('Data/train-labels-idx1-ubyte.gz')
test_labels = read_labels_from_file('Data/t10k-labels-idx1-ubyte.gz')