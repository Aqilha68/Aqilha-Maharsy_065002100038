import math
print(" @@@    @@@     @  @      @    @   @@@ ")
print("@   @  @   @    @  @      @    @  @   @")
print("@   @  @   @    @  @      @    @  @   @")
print("@@@@@  @@  @    @  @      @@@@@@  @@@@@")
print("@   @  @  @@    @  @      @    @  @   @")
print("@   @  @   @@   @  @      @    @  @   @")
print("@   @   @@@  @  @  @@@@@  @    @  @   @")
n = int(input('Masukkan angka: '))

def hitung_faktorial (n):
  if n > 2:
    return n * hitung_faktorial(n - 1)

  return 2

faktorial = hitung_faktorial(n)
print('Nilai faktorialnya adalah',faktorial)