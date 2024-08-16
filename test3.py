a = [(3,1),(2,2),(1,3),4]

b = a[:-1]
b.sort(key= lambda n : n[0])

print(b)