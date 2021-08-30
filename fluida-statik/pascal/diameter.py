print('program ini dijalankan untuk mencari gaya pada hukum pascal dengan diketahui diameternya')

fd = float(input('masukan gaya penampang 2: '))
ds = float(input('masukan diameter permukaan 1: '))
dd = float(input('masukan diameter permukaan 2: '))

# mencari diameter
phi = 3.14
ls = 1/4*phi*ds**2
print('luas permukaan 1 adalah', ls)
ld = 1/4*phi*dd**2
print('luas permukaan 2 adalah', ld)

#eksekusi
print('F1 / A1 = F1 / A2')
print('F1 /',ls,'=',fd,'/',ld )
print('F1 =',fd/ld,'X',ls)
print('F1 =',fd/ld*ls)
fs = fd/ld*ls
print('besar gaya adalah', fs)