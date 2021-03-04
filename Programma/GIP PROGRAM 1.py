from PIL import Image
import os
import numpy as np


lib = os.getcwd()
img = Image.open('img.jpg')
array = np.array(img)
print(array.shape)      # (100, 200, 4)
print(array)

array2 = np.zeros([1080, 1920, 3], dtype=np.uint8)
array2 = [255, 128, 0]
img = Image.fromarray(array2)
img.save('testrgb.png')
