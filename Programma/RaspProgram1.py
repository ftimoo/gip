from PIL import Image
import os
import numpy as np
from stime import *
import time
from apa102_pi.driver import apa102

def listToLed(kleuren):        
    strip = apa102.APA102(num_led=len(kleuren), order = 'rgb')
    i = 0
    
    strip.show()
    for sub in kleuren:
        kleur = 0
        j = 0
        for test in sub:
            kleur += test*16**(4-j*2)
            j+=1
        strip.set_pixel_rgb(i,kleur)
        i += 1
    strip.show()




stime()


lib = os.getcwd()
img = Image.open('rgb.png')
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

newArray= []
i = 1

for k in range(3):
    i = 1
    print(k)
    for rij in colommen:
        try:
            listToLed(rij)
        except:
            print(k,i)
        if i == 283:
            for element in rij:            
                newArray.append(element)
        i += 1


for k in range(3):
    i = 1
    print(k)
    for rij in colommen:
        try:
            listToLed(rij)
        except:
            print(k,i)
        if i == 283:
            for element in rij:            
                newArray.append(element)
        i += 1

stime()

img.save('testrgb.png')
input("")
