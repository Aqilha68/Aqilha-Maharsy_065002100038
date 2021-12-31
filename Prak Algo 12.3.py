def selection():
    list=[]
    minta=int(input('Berapa kali maunya? '))
    for i in range(minta):
        i+=1
        list.append(int(input(f'Masukan angka ke {i}: ')))
    print (f'list: {list}')
    for i in range(0,len(list)-1):
        p=0
        mini=list[-1]
        for j in range(i,len(list)):
            if list[j]<=mini:
                mini=list[j]
                p=j
        list[i],list[p]=list[p],list[i]
    print(f'list dengan selection: {list}')
selection()