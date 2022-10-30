a = 0
b = 1

while True:
	print(a)
	print(b)
	a += b
	b += a
	if a > 100:
		break
