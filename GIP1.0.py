from PIL import Image
import os
import numpy as np


lib = os.getcwd()
img = Image.open('img.png')
array = np.array(img)
print(array.shape)      # (100, 200, 4)
if (array.shape[2] == 4):
    array = np.delete(array, 3, 2)
    print(array.shape)      # (100, 200, 4)
rijen = []
for i in range(array.shape[1]):
    rijen.append([])
print (rijen)
i = 0
for pix in array:
    for pic in pix:
        i+=1
        rijen[i % array.shape[1]].append(pic)







print(rijen[0])
print(rijen[1])
i = 1
for rij in rijen:
    print()
    print()
    print("rij "+ str(i))
    for elenment in rij:
        print(elenment)
    i += 1

img.save('testrgb.png')
input("")