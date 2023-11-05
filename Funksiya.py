#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:32:51 2023

@author: umidjon
"""

# def salom_ber(ism):
#     """Funksiya foydalanuvchidan ismni olib 
#     salom beradi"""
#     print(f"Assalomu aleykum {ism.title()}")
    
# salom_ber('Umidjon')
# def tol_ism(ism,familya):
#     """Foydalanuvchidan to'liq ismni olib chiqaruvchi funksiya"""
#     print(f"Assalomu aleykum {ism.title()} "
#           f"Sizning familyangiz {familya.title()}"
#           )
    
    
# tol_ism('Umidjon', 'Tursunov')
    
    
# def tol_ism(ism,yosh):
#         """Foydalanuvchidan to'liq ismni olib chiqaruvchi funksiya"""
#         print(f"Assalomu aleykum {ism.title()} "
#               f"Sizning yoshingiz {2023-yosh}"
#               )
        
        
# tol_ism('Umidjon', 2003)
    
# def t_i_yasash(ism, fam, o_ism=''):
#     if o_ism:
#         t_isim=f"{ism} {fam} {o_ism} o'g'li"
#     else:
#         t_isim=f"{ism} {fam}"
#     return t_isim
# talaba= t_i_yasash('Umidjon', 'Tursunov')



# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")


def oraliq(min,max, qadam=None ):
    sonlar=[]
    if qadam:
        while min<max:
            sonlar.append(min)
            min+=qadam
    else:
        while min<max:
            sonlar.append(min)
            min+=1
    return sonlar
sonlar=oraliq(1,11,2)

# print(sonlar)


# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("\nIshlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break

# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")


# def bahola(ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=int(baho)
#     return baholar
# talabalar=['Asadbek','Boburjon','hasan','husan']
# baholar=bahola(talabalar[:])
# print(baholar)






























