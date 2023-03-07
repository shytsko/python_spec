a, b = 1, 2
print(a, b)
print(id(a), id(b))
a, b = b, a
print(a, b)
print(id(a), id(b))
c = 1
print(id(c))
