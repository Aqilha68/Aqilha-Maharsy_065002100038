string = list(map(str, input("Masukan kalimat: ").lower()))

def vokal_kon(n):
  konsonan=0
  vokal=0
  for i in range(0, len(string)):
    if string[i]=='a' or string[i]=='i' or string[i]=='u' or string[i]=='e' or string[i]=='o':
      vokal+=1
    else:
      konsonan+=1
  print("Jumlah huruf Vokal adalah",vokal)
  print("Jumlah huruf konsonan adalah",konsonan)
vokal_kon(string)