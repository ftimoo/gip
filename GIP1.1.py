from PIL import Image
import os
import numpy as np


lib = os.getcwd()
img = Image.open('img.png')
array = np.array(img)
print(array.shape)      # (100, 200, 4)
print("er zullen " + str(array.shape[1])+ " colommen zijn.")
if (array.shape[2] == 4):
    array = np.delete(array, 3, 2)

colommen = []
for i in range(array.shape[1]):
    colommen.append([])

i = 0
for pix in array:
    for pic in pix:
        i+=1
        colommen[i % array.shape[1]].append(pic)


i = 1
for rij in colommen:
    print()
    print()
    print("rij "+ str(i))
    for elenment in rij:
        print(elenment)
    i += 1

img.save('testrgb.png')
input("")