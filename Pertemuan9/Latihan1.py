def panggilAku(nama, kota = "Depok"):
    print("Hello world!")
    print(f"nama saya {nama}")
    print(f"asal saya dari {kota}")

def hitungumur(tahun):
    panggilAku("Zackpass")
    tahun_ini = int(input("tahun berapa sekarang ?"))
    umur = tahun_ini - tahun
    print(f"umur saya {umur}")

# panggilAku("Dzaki", "Kelapa Dua")
# panggilAku("Fasya")
hitungumur(2007)
