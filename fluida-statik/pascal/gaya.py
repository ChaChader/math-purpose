print('program ini dijalankan untuk mencari gaya pada hukum pascal')

fd = float(input('masukan gaya penampang 2: '))
ls = float(input('masukan luas permukaan 1: '))
ld = float(input('masukan luas permukaan 2: '))

print('F1 / A1 = F1 / A2')
print('F1 /',ls,'=',fd,'/',ld )
print('F1 =',fd/ld,'X',ls)
print('F1 =',fd/ld*ls)
fs = fd/ld*ls
print('besar gaya adalah', fs)