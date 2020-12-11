# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 12:06:31 2020
Python 2.7
@author: Fanny Besson

Un fichier pour manipuler les dates en python
"""

from datetime import datetime
import time

date=datetime.now() #Récuperer la date d'aujourd'hui
print("Date du jour: ")
print(date)

#Convertir du texte en date
text='2020-09-10'
date=datetime.strptime(text, "%Y-%m-%d")
print("Date convertie: ")
print(date)
print(type(date))

#Convertir une date en texte
text=datetime.strftime(date, "%Y-%m-%d")
print("Date convertie en texte:")
print(text)
print(type(text))

#N'afficher que l'année
print("Année:")
print(time.strftime('%Y')) 
# %Y: année, %b: nom du mois, %d:jour du mois, %H: heure, %M: minute, %S: seconde 

#Changer le format d'une date
date = datetime.today()
print("Modification du format:")
print(date.__format__('%b %d %Y'))
print(date.__format__('%d/%m/%y %H:%M'))

#Récuperer l'epochstamp
print("Epoch Stamp:")
print(time.time())

#Convertir epochstamp en date:
timestamp=time.time()
print("Converstion de l'epoch stamp en date:")
print(datetime.fromtimestamp(timestamp))