d={'one':1,10:1,}
print(d)

d['two']=2
d['two']=4
print(d)

print(d.pop('two'))
print(d)

d['three']=3
print(d)

d[12]=2
print(d)

print(d.popitem())

print(d.keys())
print(d.values())
d1=d.copy()
print(d1)
d1.clear()
print(d1)

