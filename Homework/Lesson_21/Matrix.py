import RowMatrixException


class Row:
	def __init__(self, iterable):
		if all([isinstance(i, (int, float)) for i in iterable]):
			self.__row = iterable
			self.len = len(iterable)
		else:
			raise TypeError(f'cannot construct a row from {type(iterable)}, must be an iterable of int or float')

	def __getitem__(self, idx):
		# Behavior of using square brackets [] on instances of this class like with lists
		return self.__row[idx]

	def __setitem__(self, idx, val):
		# Behavior of using square brackets [] to change a value on instances of this class like with lists
		self.__row[idx] = val

	def __str__(self):
		return ' '.join([str(i) for i in self.__row])

	def __add__(self, other):
		# Add a row to another row, int or float
		if isinstance(other, Row):
			if self.len != other.len:
				raise RowMatrixException.NotEqualLengthError('the numbers of row elements are not equal')
			return Row([self[i] + other[i] for i in range(self.len)])
		elif isinstance(other, (int, float)):
			return Row([self[i] + other for i in range(self.len)])
		else:
			raise TypeError(f'unsupported operand type(s) for +: Row and {type(other)}')

	def __sub__(self, other):
		# Subtract a row from another row, int or float
		if isinstance(other, Row):
			if self.len != other.len:
				raise RowMatrixException.NotEqualLengthError('the numbers of row elements are not equal')
			return Row([self[i] - other[i] for i in range(self.len)])
		elif isinstance(other, (int, float)):
			return Row([self[i] - other for i in range(self.len)])
		else:
			raise TypeError(f'unsupported operand type(s) for -: Row and {type(other)}')

	def __mul__(self, other):
		# Multiply a row by another row, int or float
		if isinstance(other, (int, float)):
			return Row([self[i] * other for i in range(self.len)])
		else:
			raise TypeError(f'unsupported operand type(s) for *: Row and {type(other)}')

	def __truediv__(self, other):
		# Divide a row by int or float
		if isinstance(other, (int, float)):
			return Row([self[i] / other for i in range(self.len)])
		else:
			raise TypeError(f'unsupported operand type(s) for /: Row and {type(other)}')


class Matrix:
	def __init__(self, iterable):
		if all([isinstance(i, Row) for i in iterable]):
			self.__mat = [r for r in iterable]
		elif all([isinstance(i, (list, tuple, set)) for i in iterable]):
			self.__mat = [Row(r) for r in iterable]
		else:
			raise TypeError(f'cannot construct a matrix from {type(iterable)}, must be an iterable of Row, list, tuple or set')
		self.m = len(iterable)
		self.n = self.__mat[0].len
		self.size = self.m, self.n

	def __getitem__(self, idx):
		# Behavior of using square brackets [] on instances of this class like with lists
		return self.__mat[idx]

	def __setitem__(self, idx, val):
		# Behavior of using square brackets [] to change a value on instances of this class like with lists
		self.__mat[idx] = val

	def __str__(self):
		return '\n'.join([str(row) for row in self.__mat])

	def __add__(self, other):
		# Add a matrix to another matrix, int or float
		if isinstance(other, Matrix):
			if self.size != self.size:
				raise RowMatrixException.NotEqualLengthError('the numbers of matrix elements are not equal')
			return Matrix([self.__mat[i] + other.__mat[i] for i in range(self.m)])
		elif isinstance(other, (int, float)):
			return Matrix([self[i] + other for i in range(self.m)])
		else:
			raise TypeError(f'unsupported operand type(s) for +: Matrix and {type(other)}')

	def __sub__(self, other):
		# Subtract a matrix from another matrix, int or float
		if isinstance(other, Matrix):
			if self.size != self.size:
				raise RowMatrixException.NotEqualLengthError('the numbers of matrix elements are not equal')
			return Matrix([self.__mat[i] - other.__mat[i] for i in range(self.m)])
		elif isinstance(other, (int, float)):
			return Matrix([self[i] - other for i in range(self.m)])
		else:
			raise TypeError(f'unsupported operand type(s) for -: Matrix and {type(other)}')

	def __mul__(self, other):
		# Multiply a matrix by another matrix, int or float
		if isinstance(other, Matrix):
			if self.n != other.m:
				raise RowMatrixException.NotEqualRowColumnError(f'A matrix with the length of rows {self.n} is multiplied by '
																f'a matrix with the length of columns {other.m}')
			return Matrix([[sum([self[i][k] * other[k][j] for k in range(other.m)]) for j in range(self[i].len)] for i in range(self.m)])
		elif isinstance(other, (int, float)):
			return Matrix([self[i] * other for i in range(self.m)])
		else:
			raise TypeError(f'unsupported operand type(s) for *: Matrix and {type(other)}')

	def __truediv__(self, other):
		# Divide a matrix by int or float
		if isinstance(other, (int, float)):
			return Matrix([self[i] / other for i in range(self.m)])
		else:
			raise TypeError(f'unsupported operand type(s) for /: Row and {type(other)}')

	def transposed(self):
		# Transpose a matrix
		return Matrix([[self[j][i] for j in range(self[i].len)] for i in range(self.m)])


m = Matrix([[4, 2, 0],
			[1, 3, 2],
		    [-1, 3, 10]])
m[0], m[1] = m[1], m[0]
m[1] += m[0] * -4
m[2] += m[0]
m[1] /= -2
m[2] /= 6
m[1], m[2] = m[2], m[1]
m[2] += m[1] * -5
print(m)
