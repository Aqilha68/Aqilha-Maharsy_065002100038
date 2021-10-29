print(" @@@    @@@     @  @      @    @   @@@ ")
print("@   @  @   @    @  @      @    @  @   @")
print("@   @  @   @    @  @      @    @  @   @")
print("@@@@@  @@  @    @  @      @@@@@@  @@@@@")
print("@   @  @  @@    @  @      @    @  @   @")
print("@   @  @   @@   @  @      @    @  @   @")
print("@   @   @@@  @  @  @@@@@  @    @  @   @")

a = int(input("Masukan Jumlah bilangan: "))
while a<2:
  print("Salah, input ulang")
  a = int(input("Masukan Jumlah bilangan: "))
F1=int(input("Masukan bilangan pertama: "))
F2 = int(input("Masukan bilangan kedua: "))
for i in range(a):
  b=F1
  
  x = F1+F2
  F1=F2
  F2=x
  print(b)