from PIL import Image
import os
import numpy as np


lib = os.getcwd()
img = Image.open('img.jpg')
array = np.array(img)
print(array.shape)      # (100, 200, 4)
print(array)


for pix in array:
    for pic in pix:
        print(pic)
    

img.save('testrgb.png')
input("")