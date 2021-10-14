import numpy as np
r = print
a1 = 2
a2 = -1
a3 = 1
b1 = -2
b2= 0
b3 = 1
d1 = -1
d2 = 1
e1 = 2
e2 = -2
f1= 2
f2 = 3
m = np.array([[a1,a2,a3],[b1,b2,b3]])
n = np.array([[d1,d2],[e1,e2],[f1,f2]])

C = m.dot(n)
r('matriks m adalah\n',m)
r('matriks n adalah\n',n)
r('dikali menjadi')
r(C)
r('determinannya adalah')
print (np.linalg.det(C))

print(-2*1-7*4)

