from math import sqrt
print(" @@@    @@@     @  @      @    @   @@@ ")
print("@   @  @   @    @  @      @    @  @   @")
print("@   @  @   @    @  @      @    @  @   @")
print("@@@@@  @@  @    @  @      @@@@@@  @@@@@")
print("@   @  @  @@    @  @      @    @  @   @")
print("@   @  @   @@   @  @      @    @  @   @")
print("@   @   @@@  @  @  @@@@@  @    @  @   @")
print("KALKULATOR PYTHAGORAS")
formula = input ('Sisi mana yang ingin anda hitung = ')

if formula == 'c':
    sisiA = int(input('Masukkan panjang sisi a = '))
    sisiB = int(input('Masukkan panjang sisi b = '))

    sisiC = sqrt(sisiA*sisiA + sisiB*sisiB)
    print ('Panjang sisi c adalah', sisiC)

elif formula == 'a':
    sisiC = int(input('Masukkan panjang sisi c = '))
    sisiB = int(input('Masukkan panjang sisi b = '))

if (sisiC<sisiB):
    print ("panjang c tidak valid")
    sisiC=int(input('Masukkan panjang sisi c = '))

    sisiA = sqrt(sisiC*sisiC + sisiB*sisiB)
    print ('Panjang sisi a adalah', sisiA)

elif formula == 'b':
    sisiC = int(input('Masukkan panjang sisi c = '))
    sisiA = int(input('Masukkan panjang sisi a = '))

if (sisiC<sisiA):
    print ("panjang c tidak valid")
    sisiC=int(input('Masukkan panjang sisi c = '))

    sisiB = sqrt(sisiC*sisiC + sisiA*sisiA)
    print ('Panjang sisi b adalah', sisiB)


