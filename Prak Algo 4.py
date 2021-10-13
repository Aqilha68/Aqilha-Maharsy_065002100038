print(" @@@    @@@     @  @      @    @   @@@ ")
print("@   @  @   @    @  @      @    @  @   @")
print("@   @  @   @    @  @      @    @  @   @")
print("@@@@@  @@  @    @  @      @@@@@@  @@@@@")
print("@   @  @  @@    @  @      @    @  @   @")
print("@   @  @   @@   @  @      @    @  @   @")
print("@   @   @@@  @  @  @@@@@  @    @  @   @")
import sys
x=0
while x ==0:
    a = int(input('''
    ---PROGRAM KONVERSI BILANGAN--
    1 -> Desimal ke Biner
    2 -> Biner ke Desimal
    3 -> Exit
    Silahkan pilih menu : '''))

    if a == 1 :
        desimal = int(input('Masukkan bilangan desimal : '))
        biner = bin(desimal) .replace("0b","")
        print('Nilai binernya adalah',biner)

    elif a == 2 :
        biner = input('Masukkan bilangan biner : ')
        desimal = 0
        pangkat=len(biner)-1

        for i in range(len(biner)):
            idesimal=int(biner[i]) * 2 ** pangkat
            desimal += idesimal
            pangkat -= 1
        print ('Nilai desimalnya adalah',desimal)

    elif a == 3 :
        print('Terima kasih telah menggunakan program ini!')
        sys.exit(0)
