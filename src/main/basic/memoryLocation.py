names = ['ram', 'Pratik']
print(id(names))

ename = names

names = ['ram', 'Punit']
print(id(names))
print(id(ename))

ename = names

print(names)
print(ename)