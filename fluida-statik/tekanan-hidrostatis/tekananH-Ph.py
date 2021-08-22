print('program ini dijalankan untuk mencari tekanan hidrostatis(Pa)')

Pr = float(input("masukan massa jenis fluida(kg/m^3): "))
h = float(input("masukan kedalaman fluida(m): "))
g = float(input("masukan percepatan gravitasi(m/s^2) yang ditentukan: "))

#jawab
print('Ph = Pr.g.h')
print('Ph =',Pr,".",g,".",h)
print('Ph =',Pr*g*h,"Pa")
print('besar tekanan hidrostatis adalah ',Pr*g*h,"Pa")
