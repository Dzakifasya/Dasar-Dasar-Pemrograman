pembeli = "Budi"
produk = "TV"
jumlah = 3

if produk == "TV":
    harga_satuan = 3000000
elif produk == "Kulkas":
    harga_satuan = 4000000
elif produk == "AC":
    harga_satuan = 5000000
else:
    harga_satuan = 0
harga_kotor = harga_satuan * jumlah

if produk == "AC" and jumlah >= 2:
    diskon = 0.2 * harga_kotor
if produk == "Kulkas" and jumlah >= 2:
    diskon = 0.1 * harga_kotor
else:
    diskon = 0.05 * harga_kotor
ppn = 0.1 * (harga_kotor - diskon)
netto = (harga_kotor - diskon) + ppn

print("Pembeli\t:",pembeli,
      "\nProduk\t:",produk,
      "\nHarga Satuan\t:",harga_satuan,
      "\nHarga Kotor\t:",harga_kotor,
      "\nPPN\t\t:",ppn,
      "\nJumlah Bayar\t:",netto,
      )