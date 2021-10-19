a=0
while a==0:
    print(" @@@    @@@     @  @      @    @   @@@ ")
    print("@   @  @   @    @  @      @    @  @   @")
    print("@   @  @   @    @  @      @    @  @   @")
    print("@@@@@  @@  @    @  @      @@@@@@  @@@@@")
    print("@   @  @  @@    @  @      @    @  @   @")
    print("@   @  @   @@   @  @      @    @  @   @")
    print("@   @   @@@  @  @  @@@@@  @    @  @   @")

    x=input('Isi list angka (integer): ')
    genap=[]
    ganjil=[]
    for x in x.split():
        if int(x)%2==0:
                print('List angka memiliki angka genap')
                break
        if int(x)%2==0:
            genap.append(int(x))
            print('List angka memiliki angka genap')
            break
    
        else:
            print('List angka tidak memiliki angka genap')
            break