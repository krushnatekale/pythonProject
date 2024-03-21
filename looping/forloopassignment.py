#Print numbers from 0 to 4 (upto 5 but not including 5)
for i in range(0,5):
    print(i)

# Print numbers from 1 to 4 (num starts from zero if start index is omitted)
for i in range(1,5):
    print(i)

# Print every alternate numbers starting zero
for i in range(0,11,2):
    print(i)

# Print number from 10 to 1
for i in range(10,0,-1):
    print(i)

# Print number form 10 to 0
for i in range(10,-1,-1):
    print(i)

# Print alternate numbers from 10 to 0.
for i in range(10,0,-2):
    print(i)

# Print "Python is awesome!!" 5 times
for i in range(0,5):
    print("Python is awesome!!")

# Print numbers from -10 to -1
for i in range(-10,0,1):
    print(i)

# Print numbers from 10 to -1
for i in range(10,-2,-1):
    print(i)

# Print even numbers
for num in range(0,10):
    if num%2==0:
        print(num)

# Print odd  numbers
for num in range(0,10):
    if num%2!=0:
        print(num)

# Iterate over the list only if the list has atleast 1 item.
l = [[1, 2, 3], [], ["hai"]]
for element in l:
    if len(element)>=1:
        print(element)

# Iterate over the list only if the string has atleast 1 item.
l = ['hello','welcome','to','Python','','Programming']
for element in l:
    if len(element)>=1:
        print(element)

# Iterate over the list only if the dictionary has atleast 1 item.
l = [{'h':['hello','hi']},{'name':'motu','bestfriend':'patlu'},{},{'p':['python','programming'],'t':['to','there']}]
for element in l:
    if len(element)>=1:
        print(element)

# Iterate over the list only if the set has atleast 1 item.
l = [{1,2,3},{},{4,5,6}]
for element in l:
    if len(element)>=1:
        print(element)

# Iterate over the list only if the tuple has atleast 1 item.
l = [(1,2,3),(),(3,4,5),(5,6,7)]
for element in l:
    if len(element)>=1:
        print(element)

# Find the sum of first 10 even numbers
sum=0
for i in range(2,21,2):
    sum+=i
print(sum)

# Write a program to print prime numbers from 1 to 50
for i in range(1,51):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)

# Write a program for Linear Search


# Program to convert uppercase characters to lowercase characters in the string
#WITH IN-BUILT METHODS
s='Hello Welcome to Python Programming'
new_string=''
for i in s:
    if i.isupper():
        new_string += i.lower()
    else:
        new_string += i
print(new_string)

#WITHOUT IN-BUILT METHODS
s='Hello Welcome to Python Programming'
new_string=''
for i in s:
    ascii=ord(i)
    if ascii>=65 and ascii<=90:
        lower_ascii=ascii+32
        char = chr(lower_ascii)
        new_string += char
    else:
        new_string += i
print(new_string)

# Program to convert lowercase characters to uppercase characters in the string

#WITH IN-BUILT METHODS
s='Hello Welcome to Python Programming'
new_string=''
for i in s:
    if i.islower():
        new_string += i.upper()
    else:
        new_string += i
print(new_string)

#WITHOUT IN-BUILT METHODS
s='Hello Welcome to Python Programming'
new_string=''
for i in s:
    ascii=ord(i)
    if ascii>=97 and ascii<=122:
        upper_ascii = ascii-32
        char = chr(upper_ascii)
        new_string += char
    else:
        new_string += i
print(new_string)

# Program to print only integer datatypes in the list
data = [ "hi", "hello", 10, "12.3", 12, 90, 6.2]
for element in data:
    if type(element)==int:
        print(element)

# Program to print only integer and float datatypes in the list
data = [ "hi", "hello", 10, "12.3", 12, 90, 6.2]
for element in data:
    if type(element) in [int,float]:
        print(element)

# program to print all the numeric values in the list
data = [ "hi", "hello", 10, "12.3", 12, 90, 6.2]
for element in data:
    if type(element) in [int,float]:
        print(element)

# Program to print only vowels in the string "Python selenium"
string= "Python selenium"
for char in string:
    if char in 'aeiouAEIOU':
        print(char)

# Program to print only consonants in the string "Python selenium"
string= "Python selenium"
for char in string:
    if char not in 'aeiouAEIOU':
        print(char)

# Program to print all the square numbers in the list.
nums = [10, 25, 4, 56, 64, 256]
for num in nums:
    sqrt=num**0.5;
    sqrt=int(sqrt)
    if sqrt**2==num:
        print(num)


#STRING
# Iterating over string using range function.
s = "hello world"
for index in range(0,len(s)):
    print(s[index],end='')

# iterating over a string in reversed direction
s = "hello world"
for index in range(len(s)-1,-1,-1):
    print(s[index],end='')

# Printing Index and Character using range class
s = "hello world"
for index in range(0,len(s)):
    print(f'{index} : {s[index]}')

# Iterating over multiple string objects using zip class
s = "hello world"
s1="Python Programming"
for val1,val2 in zip(s,s1):
    print(val1,val2)

# Printing alternate characters of the string
s = "hello world"
for index in range(0,len(s),2):
    print(s[index])

# Program to count the number of digits and alphabets in the string "hai 1234 python23"
#WITH IN-BUILT METHODS
string='hai 1234 python23'
alpha_count=0
digit_count=0
for i in string:
    if i.isalpha():
        alpha_count += 1
    elif i.isdigit():
        digit_count += 1
print(f'In String : {string} , there are {alpha_count} Alphabets and {digit_count} Digits. ')

#WITHOT IN-BUILT METHODS
string='hai 1234 python23'
alpha_count=0
digit_count=0
for i in string:
    ascii=ord(i)
    if (ascii>=65 and ascii<=90) or (ascii>=97 and ascii<=122):
        alpha_count += 1
    elif ascii>=48 and ascii<=57:
        digit_count += 1
print(f'In String : {string} , there are {alpha_count} Alphabets and {digit_count} Digits. ')


# Program to count the number of capital and small letters in the string "HelLo WORld"

# WITHOUT IN-BUILT METHODS
string='HelLo WORld'
upper_count=0
lower_count=0
for i in string:
    ascii=ord(i)
    if ascii>=65 and ascii<=90:
        upper_count += 1
    elif ascii>=97 and ascii<=122:
        lower_count += 1
print(f'In String : {string}, there are {lower_count} Lowercase and {upper_count} Uppercase characters.')

# WITH IN-BUILT METHODS
string='HelLo WORld'
upper_count=0
lower_count=0
for i in string:
    if i.isupper():
        upper_count += 1
    elif i.islower():
        lower_count += 1
print(f'In String : {string}, there are {lower_count} Lowercase and {upper_count} Uppercase characters.')


#List

# Prints the item and its corresponding index in the list
l=[12,3,44,5,32,2]
for i in range(0,len(l)):
    print(i,l[i])

#WITH ENUMERATE FUNCTION
l=[12,3,44,5,32,2]
for index,value in enumerate(l):
    print(index,value)


# Printing alternate items of the list
l=['String',22,33,5.5,True]
for i in range(0,len(l),2):
    print(l[i])

# Iterating over multiple lists simultaneously
l1=[1,1.0,'Hello',True,21]
l2=[2,3.0,'Bye',False,12]
for i in zip(l1,l2):
    print(i)

# Iterating through multiple list with un-equal lengths using zip class
l1=[1,1.0,'Hello',True,21,456,'Python']
l2=[2,3.0,'Bye',False,12]
for i in zip(l1,l2):
    print(i)

# Program to print filenames ending with pdf.
files = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.pdf', 'apple.doc']
for i in files:
    name=i.split('.')
    if name[-1] == 'pdf':
        print(name[0])

# #2nd way
files = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.pdf', 'apple.doc']
d={}
for i in files:
    name=i.split('.')
    if name[1] not in d:
        d[name[1]] = [name[0]]
    else:
        d[name[1]] += [name[0]]
print(d['pdf'])

# Print the extension of each file name in the list
files = ['youtube.txt', 'yahoo.pdf', 'microsoft.doc', 'apple.xls', 'amazon.xml']
for i in files:
    name=i.split('.')
    print(name)

# Program to print the length of each word in the list
list=['hello','there','this','is','a','string']
for i in list:
    print(i,len(i))

# Program to print the length of each word in the list in th form of tuples
list=['hello','there','this','is','a','string']
for i in list:
    t=(i,len(i))
    print(t)


#Dictionary
# Print only keys of the dictionary
d={'name':'Steve','salary':72000,'age':32}
for i in d.keys():
    print(i)

# Print Values of the dictionary
d={'name':'Steve','salary':72000,'age':32}
for i in d.values():
    print(i)

# Print index and item of the dictionary
d={'name':'Steve','salary':72000,'age':32}
for index,key in enumerate(d):
    print(index,key,d[key])

# Count number of words in a sentence using get method
sentence = 'hello world hello world welcome to python'
d={}
for i in sentence:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in sentence:
    print(i,d[i])

# Counting number of characters in a string
s = 'abracadabraca'
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)

# Counting number of vowels in a string
string = 'hello world hello world welcome to python'
d={}
for i in string:
    if i in 'aeiouAEIOU':
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
print(d)

# Counting occurances of word in the string
sentence = "hello world welcome to python hello hi hello hello"
list=sentence.split(' ')
d={}
for i in list:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)

# Counting occurances of each character in the string
s = 'abracadabraca'
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)

# Create a dictionary for the below list
cities = [('India', 'Bangalore'),
          ('India', 'Chennai'),
          ('India', 'Delhi'),
          ('India', 'Kolkata'),
          ('USA', 'Dallas'),
          ('USA', 'New York'),
          ('USA', 'Chicago'),
          ('China', 'Beijing'),
          ('China', 'Shanghai')
          ]
d={}
for i in cities:
    country = i[0]
    city = i[1]
    if country not in d:
        d[country]=[city]
    else:
        d[country] += [city]
print(d)

# Adding items of two lists corresponding to their indices
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
result=[]
for num1,num2 in zip(a,b):
    result.append(num1+num2)
print(result)

# flattening the list using Multiple "for" loops
items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l=[]
for list in items:
    for num in list:
        l.append(num)
print(l)

# Python Program for n-th Fibonacci number
num1=0
num2=1
num3=0
n=int(input('Enter Value of n : '))
if n==1:
    print(num1)
elif n==2:
    print(num2)
else:
    for i in range(3,n+1):
        num3=num1+num2
        num1=num2
        num2=num3
    print(num3)

# Python Program for Sum of squares of first n natural numbers
n=int(input('Enter Value of n : '))
sum=0
for i in range(1,n+1):
    sum += i**2
print(sum)


# Python Program for cube sum of first n natural numbers
n=int(input('Enter Value of n : '))
sum=0
for i in range(1,n+1):
    sum += i**3
print(sum)
