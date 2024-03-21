#Datatype assignments

#List
li=[1,23,4,'String',True]
li.extend([12,True,'Hello'])
print(li)

li.remove('String')
print(li)

li.append('String')
print(li)

li.pop()
print(li)

li.insert(1,'String')
print(li)

li.pop(1)
print(li)

li.clear()
print(li)

#set
s={1,4}
s.add(3)
s.add(5)
s.add('hello')
s.add(30.2)
s.add(34)
print(s)

s.pop()
print(s.pop())

# s.remove(34)
s.remove(30.2)
print(s)

s1={1,2,3,4}
s2={3,4,5,6}
print(s1.intersection(s2))
print(s1.difference(s2))
s3=s1.union(s2)
print(s3)

s4=s3.copy()
print(s4)
s4.clear()
print(s4)

#dictionary
d={'name':'steve','age':20}
d['city']='California'
d['DOB']=2003
d['email']='steve2003@gmail.com'
d['profession']='student'
d['mobile']=1223223233
print(d)

print(d['age'])
print(d['city'])

print(d.get('email'))
print(d.get('mobile'))

print(d.values())
print(d.keys())

print(d.popitem())
d.popitem()
print(d)

d.pop('age')
d.pop('DOB')
d.pop('city')
print(d)

d1=d.copy()
print(d1)

d1.clear()
print(d1)

#String
s='UPPERCASE'
print(s.lower())

s='lowercase'
print(s.upper())

s='This is String'
print(s.startswith('Th'))
print(s.endswith('ng'))

s='  This is String    '
print(s.lstrip())
print(s.rstrip())
print(s.strip())

s='This is String'
print(s[::-1])
print(s[::-2])
print(s[::2])

print(s[1:3])
print(s.count('is'))
print(s.replace('i','u'))


#Count length Of Every Collection
l=[1,2,3,4,5]
print(len(l))

s={1,3,2,4,6}
print(len(s))

d={'name':'Krushna','age':22,'city':'pune'}
print(len(d))

t=(1,4,3,2,5,6)
print(len(t))

s='Hello World'
print(len(s))

a=1234
b=123.4
c=False

# print(len(a)) #Error
# print(len(b)) #Error
# print(len(c)) #Error


