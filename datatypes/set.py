# s={1,2,'Hello',34,32.0,'a'}
# s.add(22)
# print(s)
#
# s.pop()
# print(s)
#
# s.remove(34)
# print(s)
# # s.remove(34)   #will give KeyError : cause 34 is not present
# print(s)
#
# s.discard(34)

# s={1,2,'bye',4,5}
# # s.discard('hello')
# print(s)
# s.add(32)
# print(s)


s={1,4,3,2}
s.add(23)
s.add(3)
print(s)

s.pop()
print(s)
s.pop()
print(s)

s.remove(4)
print(s)
# s.remove(4)
s.discard(3)
print(s)

s1={1,2,3}
s2={3,4,5}
print(s1.intersection(s2)) #Common Element
print(s1.difference(s2)) #Unique From First
print(s1.union(s2))
print(dir(set))


a={1,2,'hello',4,5}
a.discard('bye')
print(a)
