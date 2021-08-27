import math
print('program ini dijalankan untuk menyelesaikan konsep soal berikut')
print("Jika suku ke-2 barisan geometri adalah 6 dan suku ke-5 adalah 48. Tentukan suku keberapa 6144!")

us = float(input('masukan suku awal yang diketahui: '))
js = float(input('ada berapa buah pada suku tersebut: '))
ud = float(input('masukan suku kedua yang diketahui: '))
jd = float(input('ada berapa buah pada suku tersebut: '))
bil = float(input('bilangan berapa yang ingin dicari sukunya? '))

# diketahui & ditanya
print("-------diketahui & ditanya-------")
print('suku ke', us, 'adalah', js)
print('suku ke', ud, 'adalah', jd)
print('bilangan', bil, 'merupakan suku keberapa?')

#jawab
print('-------jawab-------')
print('mencari rasio')
print("U", us,"= a X r^",us-1,"=",js)
ar = js
print("U", ud,"= a X r^",ud-1,"=",jd)
print("a X r X r^", ud-2,"=",jd)
print(ar,"X r^", ud-2,"=",jd)
print("r^", ud-2,"=",jd/ar)
print("r =",(jd/ar)//(ud-2))
r = (jd/ar)//(ud-2)
print("U", ud, "= a X r =", js)
print("a X", r, "=", js)
print("a =",js/r)
a = js/r
print("eksekusi:")
print('Un=a X r^n-1')
print(bil,'=',a,"X",r,"^n-1")
print(bil/a,'=',r,"^n-1")
ba = bil/a
hba = math.log(ba,r)
print(r,"^",hba,'=',r,"^n-1")
print(hba,'= n-1')
print(hba+1,"= n")
n = hba+1
print(bil, "merupakan hasil dari suku ke", n)