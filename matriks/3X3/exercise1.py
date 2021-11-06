import numpy as np
r = print

m = np.array([[-6,-14,10],[-4,0,2],[9,14,-15]])
n = np.array([[205.000,145.000,265.000]])

C = m.dot(n)
r('matriks m adalah\n',m)
r('matriks n adalah\n',n)
r('dikali menjadi')
r(C)
r('determinannya adalah')
print (np.linalg.det(C))

print(-2*1-7*4)

