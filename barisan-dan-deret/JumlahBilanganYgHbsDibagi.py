print("program ini dijalankan untuk menyelesaikan permasalahan 'jumlah bilangan tertentu yang habis dibagi'")
bap = int(input("masukan bilangan asli pertama yang akan dijumlahkan: "))
bat = int(input("masukan bilangan asli terakhir yang akan dijumlahkan: "))
hbsdbg = int(input("masukan angka supaya habis dibagi: "))
print("Hitung jumlah bilangan asli antara", bap, "sampai", bat, "yang habis dibagi oleh", hbsdbg)

#panduan
dbgP = int(input("angka apa yang habis dibagi dan lebih serta tidak jauh dari bilangan asli pertama: "))
dbgT = int(input("angka apa yang habis dibagi dan kurang serta tidak jauh dari bilangan asli terakhir: "))

#note
print("-------")
print("note: ")
print("hbsdbg =", hbsdbg, "sebagai angka yang akan menghabiskan pembagian")
print("ddgbT = angka apa yang habis dibagi oleh", hbsdbg, "dan kurang serta tidak jauh dari bilangan asli terakhir yaitu", bat)
print("ddgbP = angka apa yang habis dibagi oleh", hbsdbg, "dan lebih serta tidak jauh dari bilangan asli pertama yaitu", bap)
print("-------")

#jawab
jawaban = ( dbgT - dbgP + hbsdbg ) / hbsdbg
print("jawab: ")
print("n = ( dbgT - dbgP + hbsdbg ) / hbsdbg")
print("n = ( ",dbgT," - ",dbgP," + ",hbsdbg," ) / ",hbsdbg)
print("n =(", dbgT - dbgP + hbsdbg,")/",hbsdbg)
print("n =", ( dbgT - dbgP + hbsdbg ) / hbsdbg)
print("jumlah bilangan asli antara", bap, "sampai", bat, "yang habis dibagi oleh", hbsdbg, "adalah ", jawaban)
