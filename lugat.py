#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 17:12:25 2023

@author: umidjon
"""

#mashina=input('Mashina turuni kiriting? ')
# cars={'BMW':'X8','Mers':'cls200','AUDI':'RS8','FERARI':'F8'} #Lug'at
# cars['GM']="Gentira" #lug'atga yangi qo'shish
# #for car in cars:
# #    if car==mashina:
# #        print(cars[car])
# #        break
# del cars['GM']  #Lug'atdan o'chirish
# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# print(python_izohli_lugati['tuple'])

#kalit = input("Kalit so'z kiriting:").lower()
#print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))
#kalit = input("Kalit so'z kiriting:").lower()
#tarjima = python_izohli_lugati.get(kalit)
#if tarjima==None:
#    print("Bunday so'z mavjud emas")
#else:
#    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
# talaba={
#         'yosh':20,
#         'ism':'Umidjon',
#         'Fam':'Tursunov',
#         'kurs':3
#         }
# print(talaba.items())
# for kalit, qiymat in talaba.items():
#         print(f"Kalit: {kalit}")
#         print(f"Qiymat: {qiymat}\n")
# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# print(mahsulotlar.keys())
# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Sizlarda {buyum}lar yo'q ekan")
# for mah in sorted(mahsulotlar):
#     mahsulotlar==mah
#     print(mah.title())
# for narx in mahsulotlar.values():
#     print(f"Mahsulotlart narxi {narx}")
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)
        

                        #NESTING
        
# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }        
# cars=[car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['km']}-km yurgan, "
#           f"{car['korobka']} "
#           f"{car['yil']} -yil, {car['narh']}$")
# print(f"{cars[0]['model']}") #Lug'atdan element olish
# malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
# for n in range(10):
#     new_car = { # har bir yangi mashina uchun lug'at yaratamiz
#         'model':'malibu',
#         'rang':None, # rangi noaniq
#         'yil':2020,
#         'narh':None, # narhi belgilanmagan
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz
# for malibu in malibus[:3]:
#         malibu['rang']='qizil'

# for malibu in malibus[3:6]:
#     malibu['rang']='qora'
# # for malibu in malibus:
# #     if malibu['korobka']=='avto':
# #         malibu['narh']=40000
# #     else:
# #         malibu['narh']=35000
# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narh']=40000
#     else:
#         malibu['narh']=35000
# # for malibu in malibus:
# #     print(malibu)

# for car in malibus:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['km']}-km yurgan, "
#           f"{car['korobka']} "
#           f"{car['yil']} -yil, {car['narh']}$")

                #LUG'AT ICHIDA RO'YXAT
# dasturchilar={
#     'ali':['CSS','MYSQL'],
#     'vali':['HTML','JS'],
#     'husan':['Python','c++'],
#     'hasan':['c#','go']
#     }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarni biladi:")
#     for til in tillar:
#         print(f"{til.upper()}", end=' ')
person = {
    'Ali': {
        'familya': 'Valiyev',
        'tyil': 1995,
        'malumoti': 'oliy',
        'fartzandi': {
            'ism': 'Aziz',
            'yili': 2017,
            'til': ['uzbek', 'rus']
        }
    },
    'Hasan': {
        'familya': 'Aimov',
        'tyil': 1989,
        'malumoti': 'oliy',
        'fartzandi': {
            'ism': 'Aziz',
            'yili': 2010,
            'til': ['uzbek', 'ingliz']
        }
    },
    'Ahad': {
        'familya': 'Aripov',
        'tyil': 1979,
        'malumoti': 'oliy',
        'fartzandi': {
            'ism': 'Alisher',
            'yili': 2003,
            'til': ['uzbek', 'koreys']
        }
    }
}

for odam, info in person.items():
    print(f"\n{odam.title()} {info['familya'].title()}, "
          f"{info['tyil']}-yil, "
          f"{info['malumoti']}\n"
          "Farzandi:",end=' '
          )
    for bola in [info['fartzandi']]:
        print(f"\n   {bola['ism'].title()}, "
              f"{   bola['yili']}-tug'ilgan"
              "\n   Biladigan tillar: "
              )
        for tili in bola['til']:
            print("     ",tili.upper())



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









