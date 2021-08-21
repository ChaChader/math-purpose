print("program ini dijalankan untuk mencari hasil dari suku yang ditentukan")
a = float(input("masukan suku pertama: "))

b = float(input("masukan selisih dari pola: "))

n = float(input("suku ke berapa: "))

#catatan
print("-------")
print("note: ")
print("a = suku pertama yang dimana adalah", a)
print("b = selisih dari pola yang dimana adalah", b)
print("n = suku ke", n)
print("-------")

#jawab
print("jawab: ")
j = a + (n - 1) * b
print("a + (n - 1) * b")
print(a ,"+ (",n ,"- 1) *", b)
print(a ,"+ (",n - 1,") *", b)
print(a ,"+ ",(n - 1) * b)
print(a + (n - 1) * b)
print("jadi, jawaban dari suku ke" , n , "adalah" , j)