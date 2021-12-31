def Binary_search(num,nilai_dicari,kiri,kanan):
    while kiri <= kanan:
        mid = (kiri + kanan)//2
        if nilai_dicari == num[mid]:
            return mid
        elif nilai_dicari > num[mid]:
            kiri = mid + 1
        else:
            kanan = mid - 1
    return -1
num =[]
minta=int(input('berapa rangenya? '))
for i in range(minta):
    i+=1
    num.append(int(input(f'masukan angka ke {i}:')))
print(num)
nilai_dicari = int(input('angka berapa?'))
hasil = Binary_search(num,nilai_dicari,0,len(num)-1)
if hasil != -1:
    print("Angka ditemukan pada index ke " + str(hasil))
else:
    print("Angka tidak ditemukan")