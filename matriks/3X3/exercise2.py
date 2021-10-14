import numpy as np

B = np.array([[2, 0], [0, 1]])
D = np.array([[2, 1], [-3, 1]])
C = D - B   
print('data yang diketahui')
print(D)
print(B)
print('hasil penjumlahan')
print(C)