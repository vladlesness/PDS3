class NotEqualLengthError(Exception):
	def __init__(self, val=None):
		if val:
			self.message = val

	def __str__(self):
		if self.message:
			return self.message
		else:
			return 'the amounts of elements are not equal'


class NotEqualRowColumnError(Exception):
	def __init__(self, val=None):
		if val:
			self.message = val

	def __str__(self):
		if self.message:
			return self.message
		else:
			return 'the length of rows are not equal to the length of columns'