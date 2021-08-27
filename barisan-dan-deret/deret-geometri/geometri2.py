print('program ini dijalankan untuk menyelesaikan konsep penyelesaian berikut')
print('Dalam suatu barisan geometri, jumlah suku kedua dan suku ketiga adalah 30, dan jumlah suku ketiga dan suku keempat adalah 45. Tentukan suku pertama dan rasio dari barisan tersebut!')

#input
print('-golongan 1-')
ss = float(input('masukan suku yang pertama kali disebutkan: '))
sd = float(input('masukan suku yang kedua kali disebutkan: '))
jss = float(input('masukan jumlah dari kedua suku tadi: '))
print('jumlah suku ke', ss, 'dan',sd, 'adalah', jss)
print('-golongan 2-')
st = float(input('masukan suku yang ketiga kali disebutkan: '))
se = float(input('masukan suku yang keempat kali disebutkan: '))
jsd = float(input('masukan jumlah dari kedua suku tadi: '))
print('jumlah suku ke', st, 'dan',se, 'adalah', jsd)

#jawab
print('-------jawab-------')
print('-golongan 1-')
print('U',ss,'+ U',sd,'=',jss)
print('a.r^',ss-1,'+ a.r^',sd-1,"=",jss)
print('a.r^',ss-1,'(1 + r) =', jss)
print('a =',jss,'/','(',ss-1,'(1 + r)',')')

print('-golongan 2-')
print('U',st,'+ U',se,'=',jsd)
print('a.r^',st-1,'+ a.r^',se-1,"=",jsd)
print('a.r^',st-1,'(1 + r) =', jsd)
print('a =',jsd,'/','(',st-1,'(1 + r)',')')

print('--semi-eksekusi--')
print(jss,'/','(',ss-1,'(1 + r)',')','=',jsd,'/','(',st-1,'(1 + r)',')')
print(jss,'/',1,'=',jsd,'/ r')
print('r =', jsd * 1 / jss)
r = jsd*1/jss

print('---eksekusi---')
print('a = jss / r*(1+r)')
print(' a=',jss,'/',r,'*(',1,'+',r,')')
print(' a=',jss,'/',r,'*(',1 + r,')')
print(' a=',jss,'/',r*(1+r))
print(' a=',jss/(r*(1+r)))
a = jss/r*(1+r)