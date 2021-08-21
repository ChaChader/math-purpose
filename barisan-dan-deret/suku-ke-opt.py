print("program ini dijalankan untuk mencari suku keberapa dari yang ditentukan")
a = float(input("masukan suku pertama: "))

b = float(input("masukan selisih dari pola: "))

n = float(input("masukan hasil untuk menentukan suku ke yang akan dicari: "))

#catatan
print("-------")
print("note: ")
print("a = suku pertama yang dimana adalah", a)
print("b = selisih dari pola yang dimana adalah", b)
print("n = hasil suku ke yang akan dicari adalah", n)
print("-------")

#jawab
print("jawab: ")
j = (n-a+b)/b
print("(n-a+b)/b")
print("(",n,"-",a,"+",b,")/",b)
print(n-a+b,"/",b)
print((n-a+b)/b)
print("jadi,", n, "merupakan suku ke", j)