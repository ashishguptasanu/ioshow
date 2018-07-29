import numpy as np

#X = np.array(range(24))
#Y = X.reshape((3,4,2))
#print(X)
#print(Y)

#x = np.array([11, 22])
#y = np.array([9, 12, 56])
#z = np.array([23, 43, 55])

#c = np.concatenate((x, y, z))
#print(c)
#x = np.array(range(24))
#x = x.reshape((3,4,2))
#y = np.array(range(100, 124))
#y = y.reshape((3,4,2))

#z = np.concatenate((x, y), axis=1)
x = np.array([2, 3, 15, 13, 5])
y = x[:, np.newaxis]
print(x.ndim)
print(y.ndim)


