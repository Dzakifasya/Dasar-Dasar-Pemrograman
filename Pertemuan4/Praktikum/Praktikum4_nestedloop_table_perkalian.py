print("Tabel Perkalian")
n = int(input("Tabel Perkalian Sampai Angka:"))

for i in range(1, n+1):
    for j in range (1, n+1):
        print(f"{i*j:3}", end ="")
    print("")