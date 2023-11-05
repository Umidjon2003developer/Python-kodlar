#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 22:47:17 2023

@author: umidjon
"""

# def summa(x,y,*sonlar):
#     return x+y+sum(sonlar)
# print(summa(1,12))

def avto_info(kompaniya,model,**malumotlar):
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar 
avto1=avto_info('BMW', 'M5', rang='Qora',yili='2023',narxi=45000)



