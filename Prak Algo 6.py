print(" @@@    @@@     @  @      @    @   @@@ ")
print("@   @  @   @    @  @      @    @  @   @")
print("@   @  @   @    @  @      @    @  @   @")
print("@@@@@  @@  @    @  @      @@@@@@  @@@@@")
print("@   @  @  @@    @  @      @    @  @   @")
print("@   @  @   @@   @  @      @    @  @   @")
print("@   @   @@@  @  @  @@@@@  @    @  @   @")
print('MENGHITUNG JARAK TEMPUH GLBB')
def kecepatan(a,b,c):
    print('Jarak tempuh jika kecepatan awal=',a,'percepatan=',b,'dan jarak tempuh=',c,'adalah',a*2+(2*b*(c)))
    return a*2+(2*b*(c))

kecepatan_awal=int(input("Masukkan v0= "))
percepatan=int(input("Masukkan a= "))
jarak=int(input("Masukkan s= "))
kecepatan(kecepatan_awal,percepatan,jarak)