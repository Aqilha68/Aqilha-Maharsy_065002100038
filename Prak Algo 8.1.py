def hitung_range():
    print("PROGRAM MENGHITUNG JUMLAH RANGE")
    a=input("Masukkan angka pertama: ")
    a=int (a)
    b=int(input('Masukkan angka kedua: '))
    sum=0
    for i in range(a, b+1, 1):
        sum=sum+i
    print("Jumlah range adalah: ", sum)
hitung_range()