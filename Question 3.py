import gzip

def read_images_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic is:", magic)
        
        noimg = f.read(4)
        noimg = int.from_bytes(noimg, 'big')
        print("Number of images is:", noimg)

        norow = f.read(4)
        norow = int.from_bytes(norow, 'big')
        print("Number of rows is:", norow)

        nocol = f.read(4)
        nocol = int.from_bytes(nocol, 'big')
        print("Number of colums is:", nocol)

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

train_images = read_images_from_file('Data/train-images-idx3-ubyte.gz')
test_images = read_images_from_file('Data/t10k-images-idx3-ubyte.gz')

for row in train_images[4999]:
	for col in row:
		print('.' if col <= 127 else '#', end='')
	print()

import PIL.Image as pil
img = pil.fromarray(np.array(train_images[4999]))
img = img.convert('RGB')
img.show()
img.save('2.png')