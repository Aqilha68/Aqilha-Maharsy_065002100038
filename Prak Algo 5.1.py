print(" @@@    @@@     @  @      @    @   @@@ ")
print("@   @  @   @    @  @      @    @  @   @")
print("@   @  @   @    @  @      @    @  @   @")
print("@@@@@  @@  @    @  @      @@@@@@  @@@@@")
print("@   @  @  @@    @  @      @    @  @   @")
print("@   @  @   @@   @  @      @    @  @   @")
print("@   @   @@@  @  @  @@@@@  @    @  @   @")

print('---HITUNG GAJI HARIAN---')
a=float(input('Jam Masuk Kerja: '))
gaji = 175000
if a >=7.00:
    print('Selamat Pagi')
elif a >=12.00:
    print('Selamat Siang')

b=float(input('Jam pulang kantor: '))
if b >=15.00:
    print('Selamat Siang')

elif b >=16.00:
    print('Selamat Sore')
elif b - a == 8.00:
    gaji=gaji
elif b -a >=8.59:
    c = int((b - a)-8)
    gaji2=((c)*15000)
    y=int((b - a) - 8.00)
c = int((b -a)-8)
gaji2=((c)*15000)

print('----Rincian Gaji----')
print(f'Waktu Kerja     : {int(b-a)} Jam')
print(f'Gaji per Hari   : Rp.{gaji}') 
print(f'Lembur          : Rp.{gaji2} ({c} Jam x Rp.15000)')
print(f'Total Gaji      : Rp.{(gaji)+gaji2}')