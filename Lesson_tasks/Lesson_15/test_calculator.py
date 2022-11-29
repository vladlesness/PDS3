from calculator import calculate, Calculator


def test_calculate_add():
	assert calculate(5, 2, '+') == 7


def test_calculate_subtract():
	assert calculate(5, 2, '-') == 3


def test_calculate_multiply():
	assert calculate(5, 2, '*') == 10


def test_calculate_divide():
	assert calculate(6, 2, '/') == 3


calc = Calculator()


def test_calculator_add():
	assert calc.add(12, 3) == 15


def test_calculator_subtract():
	assert calc.subtract(12, 3) == 9


def test_calculator_multiply():
	assert calc.multiply(12, 3) == 36


def test_calculator_divide():
	assert calc.divide(12, 3) == 4