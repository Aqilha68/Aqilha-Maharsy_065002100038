mahasiswa=[]
def data_masuk():
   nama  = input("Masukkan Nama Mahasiswa: ")
   nilai1=int(input("Masukkan Nilai Praktikum 1: "))
   nilai2=int(input("Masukkan Nilai Praktikum 2: "))
   nilai3=int(input("Masukkan Nilai Praktikum 3: "))
   list=[nama,nilai1,nilai2,nilai3]
   mahasiswa.insert(len(mahasiswa),list)
   main()
def data():
    print(" NAMA |","PRAK 1|","PRAK 2|","PRAK 3|")
    for i in mahasiswa:
        print(i[0],"     ",i[1],"     ",i[2],"     ",i[3])
    main()
def nilaimahasiswa():
    for i in range(len(mahasiswa)):
        total=0
        for j in range (1,len(mahasiswa[i])):
            total+=mahasiswa[i][j]
        print(mahasiswa[i][0],"=",total/len(mahasiswa[i]))
    main()
def nilaipraktikum():
    praktikum1=0
    praktikum2=0
    praktikum3=0
    for i in range(len(mahasiswa)):
        praktikum1+=mahasiswa[i][1]
        praktikum2+=mahasiswa[i][2]
        praktikum3+=mahasiswa[i][3]
    praktikum1=praktikum1/len(mahasiswa)
    praktikum2=praktikum2/len(mahasiswa)
    praktikum3=praktikum3/len(mahasiswa)
    print("Nilai rata-rata 1= ",praktikum1)
    print("Nilai rata-rata 2= ",praktikum2)
    print("nilai rata-rata 3= ",praktikum3)
    main()
def nilairatarata():
    nilaimahasiswa=[]
    total=0
    for i in range(len(mahasiswa)):
        total=0
        for x in range (1,len(mahasiswa[i])):
            total+=mahasiswa[i][x]
        nilaimahasiswa.insert(len(nilaimahasiswa),total/5)
    total=0
    for i in nilaimahasiswa:
        total+=i
    total=total/len(nilaimahasiswa)
    print(total)
    main()
def update_nilai():
    update=input("Nama Yang Dicari :")
    nilai=int(input("Ingin Update nilai Praktikum ke-: "))
    nilai_baru=int(input("Nilai Baru: "))
    for i in mahasiswa:
        if i [0]==update:
            i[nilai]=nilai_baru
    main()
def main():
    print("Program Membuat List")
    print("1. Input Data")
    print("2. View Data")
    print("3. Hitung nilai rata-rata praktikum tiap mahasiswa")
    print("4. hitung nilai rata-rata setiap praktikum mahasiswa")
    print("5. Mencari nilai rata-rata dari setiap mahasiswa")
    print("6. Update nilai praktikum mahasiswa")
    print("7. Exit")
    pilih=int(input("Pilih menu yang tersedia: "))
    if pilih==1:
        data_masuk()
    elif pilih==2:
        data()
    elif pilih==3:
        nilaimahasiswa()
    elif pilih==4:
        nilaipraktikum()
    elif pilih==5:
        nilairatarata()
    elif pilih==6:
        update_nilai()
    elif pilih==7:
        exit()
    else:
        print("Keyword yang kamu masukan salah!")
        pilih=int(input("Pilih menu yang tersedia: "))
main()