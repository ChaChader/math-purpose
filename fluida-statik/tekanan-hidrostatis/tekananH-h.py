print('program ini dijalankan untuk mencari kedalaman fluida(m)')

Ph = float(input("masukan besar tekanan hidrostatis(Pa): "))
Pr = float(input("masukan massa jenis fluida(kg/m^3): "))
g = float(input("masukan percepatan gravitasi(m/s^2) yang ditentukan: "))

#jawab
print('Ph = Pr.g.h')
print('h = Ph.g/Pr')
print('h =',Ph,".",g,"/",Pr)
print('h =',Ph*g/Pr,"m")
print('kedalaman fluida tersebut adalah ', Ph*g/Pr,"m")
