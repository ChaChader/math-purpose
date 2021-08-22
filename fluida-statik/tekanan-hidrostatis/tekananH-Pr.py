print('program ini dijalankan untuk mencari massa jenis fluida(kg/m^3)')

Ph = float(input("masukan besar tekanan hidrostatis(Pa): "))
h = float(input("masukan kedalaman fluida(m): "))
g = float(input("masukan percepatan gravitasi(m/s^2) yang ditentukan: "))

#jawab
print('Ph = Pr.g.h')
print('Pr = Ph.h/g')
print('Pr =',Ph,". ",h,"/ ",g)
print('Pr =',Ph*h/g, "kg/m^3")
print('besar massa jenis fluida tersebut adalah ',Ph*h/g, "kg/m^3")
