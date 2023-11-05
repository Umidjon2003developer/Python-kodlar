#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:10:11 2023

@author: umidjon
"""

# import auto_moode
# avto1=auto_moode.avto_info('GM', 'malibu', 'qora', 'auto', 2022,3000)
# auto_moode.info_print(avto1)
# from auto_moode import avto_info as ainfo, info_print as iprint     # AS avto_infoga yangi ainfo

# avto1=ainfo('GM', 'malibu', 'qora', 'automat', 2022,3000)
# iprint(avto1)rat

# from auto_moode import * #Hamma funksiyalarni import qiladi

# avto1=avto_info('GM', 'malibu', 'qora', 'automat', 2022,3000)
# info_print(avto1)

# import random as r
# son=r.randint(1,100)  #randint raqam tanlab oladi
# print(son)

# x=list(range(0,101,5))
# print(x)
# print(r.choice(x))   # choice belgi, string tanlab oladi

# x=list(range(11))
# print(x)
# r.shuffle(x)
# print(x)

# import math
# uzunlik=lambda pi, r:2*pi*r   # Lambda nomsiz funksiya
# print(uzunlik(math.pi,10))

# daraja =lambda x,y:x**y
# print(daraja(3,3))

# def daraja(n):
#     return lambda x:x**n
# kavadrat=daraja(2)
# kub=daraja(3)
# from math import  sqrt
# sonlar=list(range(11))
# ildizlar=list(map(sqrt, sonlar))  #MAP o'ziga bitta fun va qiymat qabul qiladi va qiymatni funksiyaga jo'natadi
# print(ildizlar)

# def daraja(x):
#     return x*x
# print(list(map(daraja,sonlar)))
# kavadrat=list(map(lambda x:x*x, sonlar))
# print(kavadrat)

# a=[2,3,4]
# b=[3,5,7]
# a_b=list(map(lambda x,y:x+y,a,b))
# print(a_b)

# import random as r
# sonlar=r.sample(range(100), 10)
# juft_sonlar=list(filter(lambda son:son%2==0,sonlar))
# print(juft_sonlar)

mevalar=['olma','behi', "o'rik",'shaftoli','gilos']
# harf='b'
# meva_b=list(filter(lambda meva:meva.startswith(harf),mevalar))
# print(meva_b)
meva_b=list(filter(lambda meva:len(meva)<=5,mevalar))
print(meva_b)


