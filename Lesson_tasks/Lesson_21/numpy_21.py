import numpy as np

a = np.array([[1, 4, 5],
			  [-5, 8, 9],
			  [-6, 7, 11]])
b = np.array([[3.0, 7, 4],
			  [-5.3, 7, 21],
			  [7.1, 9.3, 12.7]])
c = np.array([[1, 4, 5],
			  [-5, 8, 9],
			  [-6, 7, 11]], dtype=complex)
d = np.zeros((3, 3))

# print(a, b, c, d, sep='\n', end='\n')
# print(a[:,0], a[:,-1])

# print(a + b)
# print(a - b)
# print(a.dot(b))
# print(a.transpose())
# print(2 * a)

e = np.array([[2, 1],
			  [-3, 0],
			  [4, -1]])
t = np.array([[5, -1, 6],
			  [-3, 0, 7]])
print(e.dot(t))

y = np.array([[1, 2, 3]]).dot(np.array([[4],
										[5],
										[6]]))
print(y)
print(type(y))