print('program ini dijalankan untuk soal yang biasanya "tentukan baris kursi ke-?"')

#golongan satu
bp = int(input("masukan baris yang pertama disebutkan: "))
kp = int(input("ada berapa jumlahnya pada baris tersebut: "))
print("pada baris ke " , bp , "ada " , kp , " buah")

#golongan dua
bd = int(input("masukan baris yang kedua disebutkan: "))
kd = int(input("ada berapa jumlahnya pada baris tersebut: "))
print("pada baris ke " , bd , "ada " , kd , " buah")

#golongan tiga
bt = int(input("masukan baris yang ketiga disebutkan: "))
kt = int(input("ada berapa jumlahnya pada baris tersebut: "))
print("pada baris ke " , bt , "ada " , kt , " buah")

#ditanya
dtny = int(input("baris keberapa yang mau dicari berapa banyak buahnya? "))

#menjawab
#mencari selisih
sb = kd - kp
print("selisih nya adalah", sb)

#catatan istilah
print("-------")
print("note:")
print("dtny = baris yang ingin dicari berapa banyak buahnya")
print("kp = jumlah buah pada baris pertama")
print("sb = selisih jumlah dari dua baris")
print("-------")

#masukan ke persamaan
print("jawab: ")
hasilK = dtny / 2 * (2 * kp + (dtny - 1) * sb)
print("dtny / 2 * (2 * kp + (dtny - 1) * sb)")
print("dtny / 2 * (2 * kp + (",dtny," - 1) * sb)")
print("dtny / 2 * (2 * kp + ",(dtny - 1)," * sb)")
print("dtny / 2 * (2 * ",kp + (dtny - 1)," * sb)")
print("dtny / 2 * (2 * ",kp + (dtny - 1)," * ",sb),")"
print(dtny ,"/ 2 *", (2 * kp + (dtny - 1) * sb))
print(dtny / 2 ,"*(", (2 * kp + (dtny - 1) * sb),")")
print(dtny / 2 * (2 * kp + (dtny - 1) * sb))
print("ada", hasilK, "buah pada baris ke", dtny)