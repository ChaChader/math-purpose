print('program ini dijalankan untuk menyelesaikan konsep penyelesaian berikut')
print('Tentukan jumlah enam bilangan pertama dari deret 125 – 50 + 20 – 8 +...!')

#input
bs = float(input('masukan bilangan pertama: '))
bd = float(input('masukan bilangan kedua: '))
bc = float(input('berapa bilangan yang ingin dicari jumlahnya: '))
print('-------jawab-------')
#rasio
print('rasionya adalah',bd/bs)
r = bd/bs
print('a(r^s-1)/r-1')
print(bs,'((',r,')^',bc,'-1)/',r,'-1')
print(bs,'(',r**bc,'-1)/',r-1)
print(bs,'(',(r**bc)-1,') /',r-1)
print(bs*((r**bc)-1),'/',r-1)
print(bs*((r**bc)-1)/(r-1))