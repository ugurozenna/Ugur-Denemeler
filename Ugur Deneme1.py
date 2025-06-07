# # isim= input("adin ne ? ")
# # yemek=input("en sevdigin yemek? ")
# # print(isim,yemek,"yemeyi cok sever")
# from operator import truediv

# # sayi_1= input("ilk sayiyi gir")
# # sayi_2=input("ikinci sayiyi gir")
# # print(int(sayi_2)+int(sayi_1))

# # isim=input("Adin ne ")
# # print(isim.title())


# # yas=23
# # okul= False

# # if yas>22 and okul:
# #     print("okuldan sonra askere")
# # elif yas>22 and not okul:
# #     print("Askere gideceksin")
# # else:
# #     print("Askerlik icin buyumen gerekli")


# # yas= int(input("Yas kac "))
# # okul= input("evet:e, hayir:h ")

# # if yas>22 and okul=="e":
# #     print("okuldan sonra askere")
# # elif yas>22 and okul=="h":
# #     print("Askere gideceksin")
# # else:
# #     print("Askerlik icin buyumen gerekli")




from time import sleep
i=1
while i<4:

    yas= int(input("Yas kac "))
    okul= input("Okula gidiyor musun? evet:e, hayir:h ")

    if yas>22 and okul=="e":
        print("okuldan sonra askere")
    elif yas>22 and okul=="h":
        print("Askere gideceksin")
    else:
        print("Askerlik icin buyumen gerekli")

    print(i, "sayac calisiyor gibi")

    if i==2:
        print ("bu da bonus araya if sokalim")
    i=i+1
sleep(3)
print("bu donguyu Tadinda birakalim")

sleep(3)
print("eeee")
sleep(3)
print("hmmmm")
sleep(3)
print("Yada devam edelim")
sleep(3)

sayi_1=input("bana bir sayi yaz  ")
sayi_2=input("sana zahmet bir tane daha  ")
islem=str(input("Bu iki sayiya toplama,cikarma,bolme veya carpma islemlerinden hangisini uygulayalim ?"   ))


if  islem !="+" and islem !="-" and islem !="*" and islem !="/": 
    print("hayir sembol girmelisin +  -  *  / ")
    sleep(2)
    islem=input("Tekrar Dene  ")
if  islem !="+" and islem !="-" and islem !="*" and islem !="/": 
    print("hayir sembol girmelisin +  -  *  /   bu sons sans")
    sleep(2)
    islem=str(input(("hadi Bismillah  ")))
if  islem !="+" and islem !="-" and islem !="*" and islem !="/": 
            sleep(1)
            print("Tadimiz kacti Ali Riza Bey! bye bye")    
elif islem =="+":
    print("Sonuc :",sayi_1+sayi_2)
    sleep(4)
    print("Bu bir sakaydi")
    sleep(2)
    print("Sonuc : "+str(int(sayi_1)+int(sayi_2)))
elif islem =="-":
    print("Sonuc :",sayi_1+sayi_2)
    sleep(4)
    print("Bu bir sakaydi")
    sleep(2)
    print("Sonuc : "+str(int(sayi_1)-int(sayi_2)))
elif islem =="*": 
    print("Sonuc :",sayi_1+sayi_2)
    sleep(4)
    print("Bu bir sakaydi")
    sleep(2)
    print("Sonuc : "+str(int(sayi_1)*int(sayi_2)))
elif islem =="/": 
    print("Sonuc :",sayi_1+sayi_2)
    sleep(4)
    print("Bu bir sakaydi")
    sleep(2)
    print("Sonuc : "+str(int(sayi_1)/int(sayi_2)))