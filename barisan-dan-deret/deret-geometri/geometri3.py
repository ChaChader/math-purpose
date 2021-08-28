print('program ini dijalankan untuk menyelesaikan konsep penyelesaian berikut')
print('Sebuah bandul dibiarkan berayun. Jarak yang dilalui oleh bandul itu pada ayunan pertama adalah 50 cm dan jarak yang dilalui oleh bandul itu untuk setiap ayunan adalah 7 10 dari ayunan sebelumnya. Tentukan jumlah jarak yang dilalui oleh bandul itu sebelum berhenti!')

b = float(input('masukan besar tersebut: '))
r = float(input('masukan rasio: '))

print('-------jawab-------')
print('a/(1-r)')
print(b,'/ ( 1 -', r,')')
print(b/(1-r))
h = b/(1-r)
print('(',b,'/ ( 1 -', r,') ) . 2')
print(h*2)
print('jarak yang ditempuh adalah', h*2)
