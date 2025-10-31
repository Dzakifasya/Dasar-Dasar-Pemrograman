print("--------Biodata Fighter UFC--------")
#input
nama = input("Masukkan Nama Fighter UFC: ")
divisi = input("Masukkan Divisi Fighter UFC: ")
berat = int(input("Masukkan Berat Fighter UFC (dalam lbs): "))
Asal = input("Masukkan Asal Negara Fighter UFC: ")
Tinggi = float(input("Masukkan Tinggi Fighter UFC (dalam inci): "))
umur = int(input("Masukkan Umur Fighter UFC: "))

#process
tahunlahir = 2025 - umur
#Penentuan divisi berdasarkan berat lightweight atau welterweight
if berat <= 155:
    divisi = "lightweight"
elif berat <= 170:
    divisi = "welterweight"
else:
    divisi = "middleweight"

#output
print("\n--------Bio Data Fighter UFC--------"
      "\nNama Fighter UFC:\t\t%s"
      "\nDivisi Fighter UFC:\t\t%s"
      "\nBerat Fighter UFC:\t\t%d lbs"
      "\nAsal Negara Fighter UFC:%s"
      "\ntingi Fighter UFC:\t\t%.2f cm"
      "\nTahun Lahir Fighter UFC:%d"
      % (nama, divisi, berat, Asal, Tinggi, tahunlahir)
    )

#cetak python 3.6 (f-string)
print(f"\n--------Bio Data Fighter UFC--------"
      f"\nNama Fighter UFC: {nama}"
      f"\nDivisi Fighter UFC: {divisi}"
      f"\nBerat Fighter UFC: {berat} lbs"
      f"\nAsal Negara Fighter UFC: {Asal}"
      f"\ntingi Fighter UFC: {Tinggi:.2f} cm"
      f"\nTahun Lahir Fighter UFC: {tahunlahir}")