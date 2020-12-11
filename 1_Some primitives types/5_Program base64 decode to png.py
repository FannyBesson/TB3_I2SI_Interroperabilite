# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 11:02:29 2020

@author: Fanny Besson

a program to read the Base64 string in the document base64.txt and generate the png document.
"""

import base64
from PIL import Image
from io import BytesIO

#On ouvre le texte que l'on veut convertir
f = open('base64.txt', 'r')
data = f.read()
f.closed

#Comme ici base64.txt est un document html, il faut sélectionner la partie qui décrit l'image en base64
img64=''
stop='base64,'
for i in range(0,len(data)):
    if data[i:i+len(stop)]==stop:
        j=i+len(stop)
while (data[j:j+2] != '="'):
    img64+=data[j]
    j+=1
img64+=data[j]


#On décode img64 en un png, que l'on va sauvegarder dans image.png
im = Image.open(BytesIO(base64.b64decode(img64)))
im.save('BASE64_image.png', 'PNG')
