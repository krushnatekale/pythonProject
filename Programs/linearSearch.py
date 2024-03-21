l=[22,1,3,44,32,56,78]
key=int(input('Enter Value To Search'))
flag=False
for index,element in enumerate(l):
    if key ==element:
        print(f'{key} is present in list at index {index}')
        flag=True
if not(flag):
    print(f'{key} is not present in list')
