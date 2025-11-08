############################# DICTIONARY PRACTICE ####################################

Basic dictionary operations
a = {}
print(type(a))
a = {'name': 'anu', 'place': 'ekm', 'phn': 777}
print(a['name'])
a['name'] = 'abin'                   # Update value
print(a)
a['course'] = 'mca'                  # Add new key-value pair
print(a)

Creating dictionary using variables
name1 = 'abcs'
email1 = 'nvks@gmail.com'
phone1 = 777
newdict = {'name': name1, 'email': email1, 'phone': phone1}
print(newdict)
print(newdict.get('email'))           # Access using get()
print(newdict['email'])               # Direct access
print(newdict.get('age'))             # Returns None (key not present)
print(newdict['age'])                 # Raises KeyError

########################################################################################

# User input key-value pairs into a dictionary

data_dict = {}
n = int(input("How many key-value pairs do you want to enter? "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    data_dict[key] = value

print("\nFinal Dictionary:")
print(data_dict)

# Looping through dictionary
for i in newdict:
    print(i, newdict[i])              # Prints key and value
for i in newdict.values():
    print(i)                          # Prints only values

########################################################################################
# (1) Count occurrences of each element in a list

list1 = [1, 2, 1, 3, 1, 2, 3, 4]
dict1 = {}
for i in list1:
    dict1[i] = list1.count(i)
print(dict1)

Using list comprehension for user input
n = int(input('Enter limit: '))
print('Enter list values:')
list1 = [int(input()) for i in range(n)]
dict1 = {i: list1.count(i) for i in list1}
print(dict1)

########################################################################################
# (2) Store square of each element from list into dictionary

n = int(input('Enter limit: '))
print('Enter values:')
list1 = [int(input()) for i in range(n)]
dict1 = {i: i**2 for i in list1}
print(dict1)

########################################################################################
# (3) Separate negative and positive numbers in a list

list1 = [1, -2, 3, -4, 5, -6]
negatives = []
positives = []
for i in list1:
    if i < 0:
        negatives.append(i)
    else:
        positives.append(i)
print(negatives + positives)

########################################################################################
# (4) Find palindrome words in a list

words = ['level', 'world', 'madam', 'python', 'noon']
palindromes = [word for word in words if word == word[::-1]]
print(palindromes)

########################################################################################
# (5) Replace vowels with '*'

s = 'programming'
vowels = ['a', 'e', 'i', 'o', 'u']
for j in s:
    if j in vowels:
        s = s.replace(j, '*')
print(s)

########################################################################################
# (6) Find the longest word in a sentence

s = 'she is reading a book'
words = s.split()
lengths = [len(word) for word in words]
longest = max(lengths)
print(words[lengths.index(longest)])

########################################################################################
# (7) Find common elements between two lists

l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
common = list(set(l1) & set(l2))
print(common)

########################################################################################
# Dictionary methods: pop, popitem, keys, values

a = {'b': 12, 'c': 'hello', 'd': True, 'e': 1.4}
a['s'] = 'how'
b = a.pop('s')                        # Remove key 's'
print(b)
a.popitem()                           # Removes last inserted item
print(a)
for k in a:
    print(k, a[k])
for v in a.values():
    print(v)
for k in a.keys():
    print(k)

########################################################################################
# Nested dictionary example

contact = {'gopika': {'name': 'gopika', 'email': 'gopika1@gmail.com', 'phone': [9900, 6392]}}
print(contact['gopika']['email'])

########################################################################################
# Simple calculator using dictionary

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
choice = {1: 'Addition', 2: 'Subtraction', 3: 'Multiplication', 4: 'Division', 5: 'Exit'}
print(choice)
i = int(input('Enter your choice: '))
if i == 1:
    print(a, "+", b, "=", a + b)
elif i == 2:
    print(a, "-", b, "=", a - b)
elif i == 3:
    print(a, "*", b, "=", a * b)
elif i == 4:
    print(a, "/", b, "=", a / b)
else:
    print('Invalid choice')

########################################################################################
# Dictionary comprehension examples

lst = [1, 2, 3, 4]
squares = {i: i**2 for i in lst}
print(squares)

cubes_div4 = {i: i**3 for i in range(1, 10) if i**3 % 4 == 0}
print(cubes_div4)

########################################################################################
# Reverse key-value pairs in dictionary

d = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in d.items()}
print(reversed_dict)

########################################################################################
# Even or odd labeling using dictionary comprehension

d = {i: 'even' if i % 2 == 0 else 'odd' for i in range(1, 11)}
print(d)

########################################################################################
# Convert all keys in dictionary to uppercase

a = {'a': 1, 'b': 2}
upper_keys = {k.upper(): v for k, v in a.items()}
print(upper_keys)
