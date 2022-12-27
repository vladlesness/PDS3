A, B = {0, 3, 4, 5, 7, 9,11, 18, 47}, {5, 7,47}
C, D ={3, 6, 7, 8, 10, 12, 14, 21, 50}, {8, 10, 50}
E, F = {0, 8, 14, 18, 21, 22, 25, 30, 55}, {0, 22, 55, 56}

print(A.union(B))
print(C.union(D))
print(E.union(F))

print(A.intersection(B), A & B)
print(C.intersection(D), C & D)
print(E.intersection(F), E & F)

print(A.difference(B), A - B)
print(C.difference(D), C - D)
print(E.difference(F), E - F)

A.update(B)
print(A)
C.update(D)
print(C)
E.update(F)
print(E)