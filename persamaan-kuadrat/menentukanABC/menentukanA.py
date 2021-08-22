print('program ini dijalankan untuk mencari a pada persamaan kuadrat ax2 + bx + c = 0')

#input B,C dan nilai
b = float(input('masukan nilai b pada persamaan kuadrat: '))
c = float(input('masukan nilai c pada persamaan kuadrat: '))
x = float(input('masukan nilai dari persamaan kuadrat: '))

#jawab
print('-------jawab-------')
print('ax^2 + bx + c = 0')
print('a',x,'^2 +', b,x,'+',c,"= 0")
print('a', x**2, '+', b*x, "+", c, "= 0")
print('a', x**2, '+', b*x + c, "= 0")
print('a', x**2,"=", -1*(b*x + c))
print('a', (x**2)/(x**2),"=", (-1*(b*x + c))/(x**2))
print('nilai a yang memenuhi persamaan tersebut adalah', (-1*(b*x + c))/(x**2))

