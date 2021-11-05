print('MENGHITUNG JARAK TEMPUH GLBB')
def kecepatan(kecepatan_awal,percepatan,jarak):
    a=kecepatan_awal**2+(2*percepatan*(jarak))
    print('Jarak tempuh jika kecepatan awal= ',kecepatan_awal,'percepatan= ',percepatan,'dan jarak tempuh= ',jarak, 'adalah',a)
    return a

kecepatan_awal:int(input("Masukkan v0= "))
percepatan:int(input("Masukkan a= "))
jarak:int(input("Masukkan s= "))
kecepatan(kecepatan_awal,percepatan,jarak)