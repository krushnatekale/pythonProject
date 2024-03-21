# a='abcdefghij'
# b='XYZ'
# c='1234567'
#
# index=0
# while True:
#     if index<len(a) or index<len(b) or index<len(c):
#         if index<len(a):
#             print(a[index].upper(),end='')
#         if index<len(b):
#             print(b[index].lower(),end='')
#         if index<len(c):
#             print(c[index],end='')
#         print(", ",end='')
#     else:
#         break
#     index+=1
# #
#
string='A3J7P5S3Y'
ch = None
for i in string:
    if i.isalpha():
        ch=i
        print(ch,end='')
    elif i.isdigit():
        for j in range(1,int(i)):
            print(ch,end='')
