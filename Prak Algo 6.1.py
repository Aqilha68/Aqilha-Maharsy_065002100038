from math import *
print(" @@@    @@@     @  @      @    @   @@@ ")
print("@   @  @   @    @  @      @    @  @   @")
print("@   @  @   @    @  @      @    @  @   @")
print("@@@@@  @@  @    @  @      @@@@@@  @@@@@")
print("@   @  @  @@    @  @      @    @  @   @")
print("@   @  @   @@   @  @      @    @  @   @")
print("@   @   @@@  @  @  @@@@@  @    @  @   @")
loop=1
while loop ==1:
    def kubus (a):
        print("sisi=",a,"luas=",6*a)
        return 6*a
    def balok(a,b,c):
        print('hasilnya adalah',(2*(a*b)) + (2*(a*c)) + (2*(b*c)))
        return (2*(a*b)) + (2*(a*c)) + (2*(b*c))
    def tabung(a,b):
        print('maka hasilnya adalalah',int(2*(pi*(a**2)))*(a+b))
        return float((2*(pi*(a**2)))*(a+b))
    def kerucut(a,b):
        print('maka hasilnya adalalah',pi*a*(a+b))
        return pi*a*(a+b)
    def bola(a):
        print('maka hasilnya adalalah',4*(pi*(a**2)))
        return 4*(pi*(a**2))
    print ("KALKULATOR MENCARI LUAS\n1.Kubus\n2.Balok\n3.Tabung\n4.Kerucut\n5.bola\n6.keluar")
    pilih=int(input('mau yang mana: '))
    if pilih ==1:
        no1=int(input('masukan sisi: '))
        kubus(no1)
    elif pilih ==2:
        no1=int(input('masukan panjang: '))
        no2=int(input('masukan lebar: '))
        no3=int(input('masukan tinggi'))
        balok(no1,no2,no3)
    elif pilih ==3:
        no1=float(input('masukan jari jari: '))
        no2=float(input('masukan tinggi: '))
        float(tabung(no1,no2))
    elif pilih ==4:
        no1=float(input('masukan jari jari: '))
        no2=float(input('masukan garis (s): '))
        kerucut(no1,no2)
    elif pilih ==5:
        no1=float(input('masukkan jari jari:'))
        bola(no1)
    elif pilih ==6:
        break
    else:
        print("kamu salah, ulangi lagi")
        pilih=int(input('mau yang mana: '))