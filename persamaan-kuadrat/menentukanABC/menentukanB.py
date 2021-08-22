print('program ini dijalankan untuk mencari b pada persamaan kuadrat ax2 + bx + c = 0')

#input A,C dan nilai
a = float(input('masukan nilai a pada persamaan kuadrat: '))
c = float(input('masukan nilai c pada persamaan kuadrat: '))
x = float(input('masukan nilai dari persamaan kuadrat: '))

#jawab
print('-------jawab-------')
print('ax^2 + bx + c = 0')
print(a,"X",x,"^2 + b",x,"+", c,"= 0")
print(a*x**2,"+ b",x,"+", c,"= 0")
print('b',x,"=",-1*(a*x**2),"+",-1*(c))
print('b',x,"=",-1*(a*x**2) + -1*(c))
print('b',x/x,"=",(-1*(a*x**2) + -1*(c))/x)
print('nilai a yang memenuhi persamaan tersebut adalah', )