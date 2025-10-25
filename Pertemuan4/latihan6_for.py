print("-----cetak angka 1 s/d 10-----")
angka = 10
for no in range(angka):
    #no = no + 1
    no += 1
    print("Angka",no)

print("-----cetak angka genap-----")
bil = 10
for b in range(bil):
    #no = no + 1
    b += 1
    if b % 2 == 0:
      print("Bilangan Genap",b)

print("-----cetak angka ganjil-----")
bil = 10
for b in range(bil):
    #no = no + 1
    b += 1
    if b % 2 != 0:
      print("Bilangan Ganjil",b)


