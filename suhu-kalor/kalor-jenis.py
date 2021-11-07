#kalor jenis
print('program ini dijalankan untuk masalah kalor jenis')
doks= ['kalor jenis : c | massa zat : m | perubahan suhu : T | banyak kalor yang diterima/ dilepas: Q']
print(doks)
def c (kalorjenis):
    m = float(input('masukan massa zat: '))
    t = float(input('masukan perubahan suhu: '))
    q = float(input('masukan banyak kalor yang diterima/dilepas: '))
    print('c =', q, '/', '(',m, '*', t, ')')
    c = q/(m*t)
    print('c =', c, 'J/KG.K')

def m (massazat):
    c = float(input('masukan kalor jenis: '))
    t = float(input('masukan perubahan suhu: '))
    q = float(input('masukan banyak kalor yang diterima/dilepas: '))
    print('m =', q, '/', '(',c, '*', t, ')')
    m = q/(c*t)
    print('m =', m, 'KG')

def t (perubahansuhu):
    c = float(input('masukan kalor jenis: '))
    m = float(input('masukan massa zat: '))
    q = float(input('masukan banyak kalor yang diterima/dilepas: '))
    print('t =', q, '/', '(',c, '*', m, ')')
    t = q/(c*m)
    print('t =', t, 'oK')

def q (banyakkalor):
    c = float(input('masukan kalor jenis: '))
    m = float(input('masukan massa zat: '))
    t = float(input('masukan perubahan suhu: '))
    print('q =', c, '*', m, '*', t)
    q = c*m*t
    print('q =', q, 'J')

sat= input('masukkan satuan yang ingin dicari : ')

if sat == 'c':
    c(1)
elif sat == 'm':
    m(1)
elif sat == 't':
    t(1)
elif sat == 'q':
    q(1)
else:
    print('satuan yang kamu masukan salah')
