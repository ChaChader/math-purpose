#perubahan wujud zat
print('program ini dijalankan untuk menyelesaikan masalah perubahan wujud zat')
print('documentation')
print('kalor laten: l\nkalor yang dibutuhkan: q\nmassa zat: m')
print(doks)
def l():
    q = float(input('masukan kalor yang dibutuhkan: '))
    m = float(input('masukan massa zat: '))
    l=q/m
    print('l =',q,'/',m)
    print(l,'J/KG')
def q():
    l = float(input('masukan kalor laten: '))
    m = float(input('masukan massa zat: '))
    q=l*m
    print('q =',l,'*',m)
    print(q,'J')
def m():
    q = float(input('masukan kalor yang dibutuhkan: '))
    l = float(input('masukan kalor laten: '))
    m=q/l
    print('m =',q,'/',l)
    print(m,'KG')

sat= input('masukan satuan yang ingin dicari: ')
if sat == 'l':
    l()
elif sat == 'q':
    q()
elif sat == 'm':
    m()
else:
    print('satuan yang anda masukan salah')