from Bank import *

#--------membuat objek----------
The_Fearless = Bank('001','Joshua Van',5000000)
The_Canibal = Bank('002','Alexandre Pantoja',3000000)
The_Machine = Bank('003','Merab Dvalishvili',7000000)
No_mercy = Bank('004','Petr Yan',4000000)

#use member class

The_Fearless.nabung(1500000)
The_Machine.tarik(2000000)
No_mercy.nabung(1000000)
The_Canibal.tarik(500000)
print(Bank.BANK,
    "\n==========================",)
The_Fearless.cetak()
The_Canibal.cetak()
The_Machine.cetak()
No_mercy.cetak()
print ("Jumlah Nasabah\t: %i orang"%Bank.jmlNasabah)
