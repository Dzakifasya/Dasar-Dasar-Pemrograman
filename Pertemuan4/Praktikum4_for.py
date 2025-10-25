print("Menghitung Total Belanja")
jumlah_barang = int (input("Masukan jumlah barang:"))
total = 0

for i in range (1, jumlah_barang + 1):
    harga = int(input(f"Masukan Harga Barang Ke-{i}:"))
    total += harga

print(f"Total Belanja Anda Adalah: Rp.{total}")