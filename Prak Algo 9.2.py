print(" @@@    @@@     @  @      @    @   @@@ ")
print("@   @  @   @    @  @      @    @  @   @")
print("@   @  @   @    @  @      @    @  @   @")
print("@@@@@  @@  @    @  @      @@@@@@  @@@@@")
print("@   @  @  @@    @  @      @    @  @   @")
print("@   @  @   @@   @  @      @    @  @   @")
print("@   @   @@@  @  @  @@@@@  @    @  @   @")
def kali(value) :
	hasil = 1
	for i in value :
		hasil *= i
	print("Hasil kali value list :",hasil)
	return hasil

list = [4, 2, 5, 1, 3]
print("List :",list)
kali(list)