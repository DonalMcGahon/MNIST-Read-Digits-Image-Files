from mnist import MNIST

mndata = MNIST('train-images-idx3-ubyte.gz')

images, labels = mndata.load_training()

index = random.randrange(0, len(images))
print(mndata.display(images[index]))
