print('program ini dijalankan untuk mencari luas pada hukum pascal')

fs = float(input('masukan gaya penampang 1: '))
fd = float(input('masukan gaya penampang 2: '))
ld = float(input('masukan luas penampang 2: '))

print('F1 / A1 = F1 / A2')
print(fs, '/ A1 =',fd,'/',ld)
print('A1 =',ld,'/',fd,'X',fs)
print('A1 =',ld/fd*fs)
ls = ld/fd*fs
print('besar luas penampang adalah', ls)