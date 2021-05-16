a = [1, 2, 3 ,4]
b = []
print(id(a))
print(id(b))
b.extend(a)
print(b)
print(id(a))
print(id(b))
b.append(5)
print(a)
print(b)