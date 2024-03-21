# List And Set comprehension

# Square Numbers in the list. Using List 4_Comprehensions
l=[i*i for i in range(1,11)]
s={i*i for i in range(1,11)}
# print(l)
# print(s)

# List of even numbers between range 1-50
l1=[i for i in range(1,51) if i%2==0]
s1={i for i in range(1,51) if i%2==0}
# print(l1)
# print(s1)

# Returns a list names starting with vowels in the given string
names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
list=[i for i in names if i[0] in 'aeiouAEIOU']
set={i for i in names if i[0] in 'aeiouAEIOU'}
# print(list)
# print(set)

# Filtering all the languages which starts with 'p'
languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']
list=[i for i in languages if i.startswith('P')]
set={i for i in languages if i.startswith('P')}
# print(list)
# print(set)

# Names starting with consonants
names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
list=[i for i in names if i[0] not in 'aeiouAEIOU']
set={i for i in names if i[0] not in 'aeiouAEIOU'}
# print(list)
# print(set)

# Filtering out those names which are less than 6 characters
names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']
list=[i for i in names if len(i)<6]
set={i for i in names if len(i)<6}
# print(list)
# print(set)

# Raise to the power of list index
a = [1, 2, 3, 4, 5]
list=[value**index for index,value in enumerate(a)]
set={value**index for index,value in enumerate(a)}
# print(list)
# print(set)

# Build a list of tuples with string and its length pair
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
list=[(i,len(i)) for i in names]
set={(i,len(i)) for i in names}
# print(list)
# print(set)

# Build a list with only with even length string
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
list=[i for i in names if len(i)%2==0]
set={i for i in names if len(i)%2==0}
# print(list)
# print(set)

# Generating List of PI values
# o/p: [3.0, 3.1, 3.14, 3.141]


# Reverse the item of a list if the item is of odd length string
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
list=[i[::-1] for i in names if len(i)%2!=0]
set={i[::-1] for i in names if len(i)%2!=0}
# print(list)
# print(set)

# Reverse the item of a list if the item is of odd length string otherwise keep the item as is!.
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
list=[i[::-1] if len(i)%2!=0 else i for i in names]
set={i[::-1] if len(i)%2!=0 else i for i in names}
# print(list)
# print(set)

# Reverse the string if the string is of odd length, otherwise keep it as is.
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
list=[i[::-1] if len(i)%2!=0 else i for i in names]
set={i[::-1] if len(i)%2!=0 else i for i in names}
# print(list)
# print(set)

#============= Dictionary Comprehension ===============

# Building a dict of word and length pair
words = "This is a bunch of words"
list=words.split(' ')
d={i:len(i) for i in list}
# print(d)

# Flipping keys and values of the dictionary using dict comprehension
d = {'a': 1, 'b': 2, 'c': 3}
d1={d[i]:i for i in d}
# print(d1)

# Counting the number of each character in a String
my_string = 'guido van rossum'
d={i:my_string.count(i) for i in my_string}
# print(d)

# Counting the number of each character in a String
sentence = "hello world welcome to python hello hi world welcome to python"
d={i:sentence.count(i) for i in sentence}
# print(d)

# Dictionary of character and ascii value pairs
s = 'abcABC'
d={i:ord(i) for i in s}
# print(d)

# Creating Dictionary of city and population pairs using Dict Comprehension
cities = ['Tokyo',
          'Delhi',
          'Shanghai',
          'Sao Paulo',
          'Mumbai'
          ]
population = ['38,001,000',
              '25,703,168',
              '23,740,778',
              '21,066,245',
              '21,042,538'
              ]

d={city:popu for city,popu in zip(cities,population)}
# print(d)

# Create a dictionary of dialcode and country from the following list
dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
    ]
d={i[0]:i[1] for i in dial_codes}
print(d)

# Building a dictionary whose price value is more than 200
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
d={i:prices[i] for i in prices if prices[i]>200}
print(d)
