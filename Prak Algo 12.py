list=[]
minta=int(input('berapa rangenya? '))
for i in range(minta):
    i+=1
    list.append(int(input(f'masukan angka ke {i}:')))
print(sorted(list))