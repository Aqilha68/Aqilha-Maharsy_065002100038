def ganjil(karatker):
    x = [karatker[i] for i in range (len(karatker)) if i%2==1]
    print('Karakter index ganjil: ',''.join(x))
    return(x)

a=input('Masukkan sebuah kata:')
ganjil(a)