print('program ini dijalankan untuk mencari suku pertama')
s = float(input('masukan suku keberapa yang ingin dicari: '))
p = float(input('masukan bilangan pertama: '))
pd = float(input('masukan bilangan kedua: '))

print('jawab')
b = pd - p
print('beda antar bilangan adalah', b)
sn = s/2*(2*p+(s-1)*b)
print('jumlah',s,'suku pertama adalah',sn)