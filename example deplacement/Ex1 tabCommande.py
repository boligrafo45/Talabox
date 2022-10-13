#!/usr/bin/env python
# coding: utf-8

# In[3]:


# bibliothèque permettant la communication série
import time    # pour le délai d'attente entre les messages
import subprocess #pour lancer des commandes bash
import csv #pour lire le fichier
import sys #pour fermer avec sys.exit()
import os
from numpy import sign
import pandas as pd


# In[4]:


def getTab():
    newTab = [[-0.1,1,1,1,1]]
    with open('sound.csv', 'r') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            new_row = [float(row[0]), float(row[1]), float(row[2]),float(row[3]), float(row[4])]
            newTab+=[new_row]
    file.close()
    return newTab


# In[5]:


# def getTab():
    #newTab = [[-0.1,1,1,1,1]]
    #with open('Documents/Projet%20Celia/Code/Talabox/sound.csv', 'r') as file:
    #reader = pd.read_csv(r"C:\Users\cs223092\OneDrive - De Vinci\Documents\sound.csv", sep=';')
   # for row in reader:
    #    new=float(row[1][0])
        #new_row = [float(row[0]), float(row[1]), float(row[2]),float(row[3]), float(row[4])]
        #newTab+=[new_row]
    #file.close()
   # return newTab
    #return new


# In[16]:


tab=getTab()
tab


# In[14]:


tab2=tab[2]
tab2


# In[15]:


tab2[0]


# In[ ]:




