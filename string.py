# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
cars=['bmw','mers','audi','kia','honda']
## cars.sort(reverse=True);
## print(sorted(cars))
matn = "Men yangi 📱✰oldim"
#print(matn)
ism='Umidjon'
fam=' Tursunov'
och=" Qahhorjon O'g'li"
tol=f"Men{fam} {ism} {och}"
#print(tol)
#print(tol.upper())
#print(tol.lower())
#print(tol.title())
#print(tol.capitalize())
meva="   olma   "
#print(meva)
#print(meva.lstrip())
#print(meva.rstrip())
#print(meva.strip())
#ism=input("Ismingiz nima? \n>>>")
#print("Assalomu aleykum mening ismim "+ism.title())
a=5
b=10.2
c=a*b
d=100//2 #int qaytaradi
PI=3.14159 #Constanta o'zgaruvchi
yosh=20
print(ism + ' '+ str(yosh)+' yoshda')  #STR int => str o'tkazadi
# t_yil=int(input("Tug`ilgan yilingizni kiriting: "))  #INT str=> int o'tkadi
# yosh1=2023-t_yil
b=str(b)
b=float(b)  #FLOAT str=>float o'tkazadi
mevalar=['olma','anor','shaftoli']
mevalar.append('o`rik')   #LIST ohiriga element qo'shadi
mevalar.insert(0,'behi')  #LIST indexga qarab qo'shadi
del mevalar[1] #LIST indexdagi elementni o'chiradi
mevalar.remove('anor')  #LIST nomi orqali topib o'chiradi FAQAT BIRINCHISINI
mahsulot=mevalar.pop(1) #LISTdagi elementni boshqa o'zgaruvchiga beradi

print(sorted(cars))  #Listni  tartiblash
print(sorted(cars,reverse=True))  #Listni teskari tartiblash
sonlar=list(range(0,10,1))  # 0 dan 10 gacha sonlarni chiqarib beradi 10 kirmaydi 1 qadambilan chiqadi
max=max(sonlar) #MAX -kattasini topib beradi
min=min(sonlar) #MIN -kichigini topib beradi 
sum=sum(sonlar) #SUM -jamini chiqarib beradi 
print(sonlar[1:4])  #1 dan 4 gacha elementlarni chiqaradi 4 chiqmaydi
sonlar1=sonlar[:] #LIST dan nusha olish
card=('ali','bmw') #() -O'zgarmas tuple yaratadi
card=list(card) # Listga aylantiradi 
card=tuple(card) #Listni tuplega aylantiradi 
dostlar=[]
print("5 ta eng saqin do'stingiz kim? ")
#for n in range(5):
#    dostlar.append(input(f"{n+1} -do'stingiznni kiriting:"))
#print(dostlar)
avtolar = ['audi','bmw','volvo','kia','hyundai']
for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
    else: # aks holda ... 
        print(avto.title()) # avto nomini faqat birinchi harfini katta bilan yoz.
yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2023-yil<18: # foydalanuvchining yoshini hisoblaymiz
    print(f"Yoshingiz {2020-yil}da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")
    yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2020-yil<18: # foydalanuvchining yoshini hisoblaymiz
    print(f"Yoshingiz {2020-yil}da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")
    #Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car=='gm':
    print(car.upper())
  else:
    print(car.title())
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks xolda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
login = input("Login kiriting: ")
if login.lower() == 'admin':
  print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
  print(f"Xush kelibsiz {login.title()}!")


y=input("YOshingizni kiriting ? ")
y=int(y)
if y<=4:
    print("yoshingiz 4dan kichik")
elif y<=12:
    print("Sizning yoshingiz 4 va 12 oralig'ida ")
else :
    print("sizning yoshingiz 12dan katta")












