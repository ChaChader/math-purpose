print('program ini dijalankan untuk mencari C pada persamaan kuadrat ax2 + bx + c = 0')

#input A,B dan nilai
a = float(input('masukan nilai a pada persamaan kuadrat: '))
b = float(input('masukan nilai b pada persamaan kuadrat: '))
x = float(input('masukan nilai dari persamaan kuadrat: '))

#jawab
print('-------jawab-------')
print('ax^2 + bx + c = 0')
print(a,"X",x,'^2 +', b,x,'+ C = 0')
print(a*x**2,"+",b*x,'+ C = 0')
print(a*x**2+b*x,'+ C = 0')
print("c =",-1*(a*x**2+b*x))
print('nilai a yang memenuhi persamaan tersebut adalah', -1*(a*x**2+b*x))