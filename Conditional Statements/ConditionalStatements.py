#check if the iterable is empty
l=[1,2,3]
if len(l)==0:
    print('The Iterable is Empty')
else:
    print('The Iterable is not Empty')


#greatest of 3 numbers
num1=int(input('Enter 1st Number'))
num2=int(input('Enter 2nd Number'))
num3=int(input('Enter 3rd Number'))
if num1>num2 and num1>num3:
    print(f'{num1} is greater')
elif num2>num1 and num2>num3:
    print(f'{num2} is greater')
else:
    print(f'{num3} is greater')


#converting upper to lower and vice versa
#1st way
string=input('Enter The String')
new_string=''

for index in range(0,len(string)):
    char=string[index]
    ascii=ord(char)
    if ascii>64 and ascii<91:
        lower_ascii = ascii + 32
        new_string += chr(lower_ascii)
    elif ascii>96 and ascii<123:
        upper_ascii = ascii - 32
        new_string += chr(upper_ascii)
    else:
        new_string += char
print(f'old String was {string} and converted is {new_string}.')

#2nd way
string=input('Enter The String')
new_string=''

for index in range(0,len(string)):
    char=string[index]
    ascii=ord(char)
    if ascii in range(65,91):
        lower_ascii = ascii + 32
        new_string += chr(lower_ascii)
    elif ascii in range(97,123):
        upper_ascii = ascii - 32
        new_string += chr(upper_ascii)
    else:
        new_string += char
print(f'old String was {string} and converted is {new_string}.')

#3rd way
string=input('Enter The String')
new_string=''

for index in range(0,len(string)):
    char=string[index]
    if char.isupper():
        new_string += char.lower()
    elif char.islower():
        new_string += char.upper()
    else:
        new_string += char

print(f'old String was {string} and converted is {new_string}.')

#check if entered character is vowel or not
#1st method
character=input('Enter The Character')
if len(character)==1:
    if character in 'aeiouARIOU':
        print(f'{character} is vowel')
    else:
        print(f'{character} is not vowel')
else:
    print('Please Enter Single Value')

#2nd method
character=input('Enter The Character')
if len(character)==1:
    if character=='a' or character=='e' or character=='i' or character=='o' or character=='u' or character=='A' or character=='E' or character=='I' or character=='O' or character=='U':
        print(f'{character} is vowel')
    else:
        print(f'{character} is not vowel')
else:
    print('Please Enter Single Value')

#check if entered character is vowel or not, if it is vowel then create a dictionary with char and its ascii value pair
character=input('Enter The Character')
if len(character)==1:
    if character in 'aeiouAEIOU':
        d={}
        d[character]=ord(character)
        print(d)
    else:
        print(f'{character} is not vowel')
else:
    print('Please Enter Single Value')

# check if the key is present , if present then increment or initialize the value to 1
d={'name':'steve','age':21}
key=input('Enter The Key')
if key in d:
    if type(d[key]) in [int,float]:
        d[key] += 1
        print(f'the incremented value of key is {d[key]}')
    else:
        d[key]=1
        print(f'the initialized value of key is {d[key]}')
else:
    print('Key is not present')

# check if the given value is string or not
value=[1,2,3]
if type(value) == str:
    print('The value is String')
else:
    print('The value is not a String')

#check if the given number is even or odd
num=int(input('Enter The Number'))
if num%2==0:
    print(f'{num} id even')
else:
    print(f'{num} is odd')

# check whether the string is palindrome or not
string=input('Enter the String ')
reverse_String=string[::-1]
if string == reverse_String:
    print(f'{string} is a Palindrome String')
else:
    print(f'{string} is not a Palindrome String')

# check if the integer is palindrome or not
number=int(input('Enter the number'))
new_num=str(number)
reverse_number=new_num[::-1]
if new_num==reverse_number:
    print(f'{number} is a Palindrome Number')
else:
    print(f'{number} is not a Palindrome Number')

# check if the given year is leap year or not
year=int(input('Enter Year'))
if year%4==0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

# check if the given character is number or alphabet or special character
# 1st method
character=input('Enter The Character')
if len(character)==1:
    ascii=ord(character)
    if (ascii>64 and ascii<91) or (ascii>96 and ascii<123):
        print(f'{character} is alphabet')
    elif ascii>47 and ascii<58:
        print(f'{character} is number')
    else:
        print(f'{character} is Special Symbol')
else:
    print('Please Enter Single Value')

#2nd method
character=input('Enter The Character')
if len(character)==1:
    ascii=ord(character)
    if ascii in range(65,91) or ascii in range(97,123):
        print(f'{character} is alphabet')
    elif ascii in range(48,58):
        print(f'{character} is number')
    else:
        print(f'{character} is Special Symbol')
else:
    print('Please Enter Single Value')

#3rd method
character=input('Enter The Character')
if len(character)==1:
    if character.isalpha():
        print(f'{character} is alphabet')
    elif character.isnumeric():
        print(f'{character} is number')
    else:
        print(f'{character} is Special Symbol')
else:
    print('Please Enter Single Value')

#check if the given number is perfect square or not
num=int(input('Enter Any Number'))
temp = False
for i in range(1,num):
    square = i * i
    if num==square:
        temp=True
        break
if temp:
    print('The Number is Perfect Square')
else:
    print('The Number is not a Perfect Square')


# check if the entered marks is greater than 35 then print pass, else print fail, if the marks is above 60 print first class
marks=int(input('Enter Marks'))
if marks>65:
    print('First Class')
elif marks>35:
    print('Pass')
else:
    print('Fail')

# check if the given string is starting with vowel or not
#1st method
string=input('Enter The String')
start_char=string[0]
if start_char in 'aeiouAEIOU':
    print(f'{string} starts with a vowel')
else:
    print(f'{string} does not start with a vowel')

#2nd way
string=input('Enter String')
if string.startswith('a') or string.startswith('e') or string.startswith('i') or string.startswith('o') or string.startswith('u') or string.startswith('A') or string.startswith('E') or string.startswith('I') or string.startswith('O') or string.startswith('U'):
    print(f'{string} starts with a vowel')
else:
    print(f'{string} does not starts with a vowel')

# check if the given string is ending with vowel or not
#1st way
string=input('Enter The String')
last_char=string[-1]
if last_char in 'aeiouAEIOU':
    print(f'{string} ends with a vowel')
else:
    print(f'{string} does not end with a vowel')

#2nd way
string=input('Enter String')
if string.endswith('a') or string.endswith('e') or string.endswith('i') or string.endswith('o') or string.endswith('u') or string.endswith('A') or string.endswith('E') or string.endswith('I') or string.endswith('O') or string.endswith('U'):
    print(f'{string} ends with a vowel')
else:
    print(f'{string} does not ends with a vowel')

# check if the list has even number of elements
l=[1,2,3,44,55,66]
if len(l)%2==0:
    print('The list have even number of elements')
else:
    print('The list does not have even number of elements')

# check the number of keys in the dictionary, if the number is even print the dictionary as it is, else add a new key to make it even and print it
d={'name':'steve','email':'steve@gmail.com','city':'california'}
if len(d)%2==0:
    print(d)
else:
    d['age']=40
    print(d)

# In a number check if the first number is even or odd
num=int(input('Enter Any Number'))
new_num=str(num)
f_num=new_num[0]
first_num=int(f_num)
if first_num%2==0:
    print(f'The First Number {first_num} in {num} is even')
else:
    print(f'The First Number {first_num} in {num} is odd')

# In a number check if the second last number is even or odd
num=int(input('Enter Any Number'))
new_num=str(num)
sl_num=new_num[-2]
seclast_num=int(sl_num)
if seclast_num%2==0:
    print(f'The Second Last Number {seclast_num} in {num} is even')
else:
    print(f'The Second Last Number {seclast_num} in {num} is odd')
