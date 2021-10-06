print(" @@@    @@@     @  @      @    @   @@@ ")
print("@   @  @   @    @  @      @    @  @   @")
print("@   @  @   @    @  @      @    @  @   @")
print("@@@@@  @@  @    @  @      @@@@@@  @@@@@")
print("@   @  @  @@    @  @      @    @  @   @")
print("@   @  @   @@   @  @      @    @  @   @")
print("@   @   @@@  @  @  @@@@@  @    @  @   @")
a=int(input("Masukkan total harga belanjaan anda = "))
b=int(input("Masukkan jumlah uang anda = "))
kembalian=(b-a)
print("Kembalian anda sejumlah = ", "Rp.",kembalian)
uang_pecahan = [100000,50000,20000,10000,5000,2000,1000]
jumlah_pecahan = {}
sisa = kembalian
for pecahan in uang_pecahan:
    if sisa<pecahan:
        continue
    banyak_pecahan = int(sisa/pecahan)
    sisa = sisa-(pecahan*banyak_pecahan)
    print('uang kertas {} sebanyak: {} lembar'.format(pecahan, banyak_pecahan))