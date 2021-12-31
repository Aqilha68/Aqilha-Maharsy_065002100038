def bubble_sorted():
    list=[]
    minta=int(input('berapa rangenya? '))
    for i in range(minta):
        i+=1
        list.append(int(input(f'masukan angka ke {i}:')))
    print('list normalnya:',list)
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    print(f'Hasil Bubble Sort = {list}')
bubble_sorted()