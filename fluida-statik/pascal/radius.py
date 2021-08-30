print('program ini dijalankan untuk mencari gaya pada hukum pascal dengan diketahui radiusnya')

fd = float(input('masukan gaya penampang 2: '))
rs = float(input('masukan jari-jari permukaan 1: '))
rd = float(input('masukan jari-jari permukaan 2: '))

# mencari radius
phi = 3.14
ls = phi*rs**2
print('luas permukaan 1 adalah', ls)
ld = phi*rd**2
print('luas permukaan 2 adalah', ld)

#eksekusi
print('F1 / A1 = F1 / A2')
print('F1 /',ls,'=',fd,'/',ld )
print('F1 =',fd/ld,'X',ls)
print('F1 =',fd/ld*ls)
fs = fd/ld*ls
print('besar gaya adalah', fs)