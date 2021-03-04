from PIL import Image
import numpy as np
import random

img = Image.open('img.jpg')
array1 = np.array(img)

img2 = Image.open('img2.jpg')
array2 = np.array(img2)

img3 = Image.open('img3.jpg')
array3 = np.array(img3)

bigarray = [array1,array2,array3]

for x in range(400):
    number = random.randint(0, 2)
    img = Image.fromarray(bigarray[number])
    img.show()
input("")