# ----------------------------------- File Methods: open, write, read, close -----------------------------------

# 'r' → Read mode
# f = open('abc.txt', 'r')  # Error if file does not already exist
# FileNotFoundError: [Errno 2] No such file or directory: 'abc.txt'

# 'w' → Write mode
f = open('abc.txt', 'w')  # Creates new file if it doesn't exist already
f.write('hello world')    # Rewrites / overwrites existing content
f.writelines(['hi', 'hello'])  # Takes a list
f.close()

# 'a' → Append mode
f = open('cdf.txt', 'a')  # Creates new file if it doesn't exist already
f.write('hello world')    # Appends without removing already written content
f.write('python')
f.close()

# Create file in another directory or path
# f = open(r'D:\folder1\abcd.txt', 'w')


# ----------------------------------- Read File -----------------------------------

f = open('cdf.txt', 'r')
print(f.read())
f.close()

f = open('cdf.txt', 'r')
print(f.read(7))  # Reads only first 7 characters
f.close()

f = open('cdf.txt', 'r')
print(f)  # Gives address of file and mode
# <_io.TextIOWrapper name='cdf.txt' mode='r' encoding='cp1252'>
f.close()

f = open('cdf.txt', 'r')
for i in f:
    print(i)  # Even '\n' (new line) is printed as an element
f.close()

f = open('cdf.txt', 'r')
b = f.readline()   # Reads until newline \n or EOF 
c = f.readlines()  # Reads all lines as a list with \n, e.g. ['hello world\n', 'python']
print(b)
print(c)
f.close()

f = open('cdf.txt', 'r')
for i in f:
    s = i.split(' ')
    print(s)
f.close()


# ----------------------------------- File Handling Exercises -----------------------------------

# 1️ Write a Python program that takes a string input from the user and writes it to a file notes.txt.
# If the file already exists, it should overwrite the content using 'w' method.

i = input('Enter a string: ')
f = open('notes.txt', 'w')
f.write(i)
f.close()


# 2️ Append a new line to an existing file using append mode ('a').
i = input('Enter a string to append: ')
f = open('notes.txt', 'a')
f.write(i)
f.close()

i = input('Enter another string for text.txt: ')
f = open('text.txt', 'a')
f.write(i)
f.close()


# 3️ Read entire content of a file and count number of characters.
f = open('text.txt', 'r')
v = f.read()
print("Full content:", v)
print("Total characters:", len(v))
count = 0
for i in v:
    if i.isalpha():
        count += 1
print("Alphabetic characters:", count)
f.close()


# 4️ Reverse the order of lines and write to a new file.
f = open('text.txt', 'r')
v = f.readlines()
nf = open('newfile.txt', 'a')
for i in v[::-1]:
    nf.write(i)
    print(i)
f.close()
nf.close()


# 5️ Combine content of two files and write into a third.
f1 = open('text.txt', 'r')
f2 = open('notes.txt', 'r')
v = f1.read() + f2.read()
f3 = open('third.txt', 'w')
f3.write(v)
f1.close()
f2.close()
f3.close()


# 6️ Read a file and write all alphabets to one file, numbers to another.
f = open('file1.txt', 'r')
v = f.read()
print(v)
f1 = open('f_alpha.txt', 'a')
f2 = open('f_num.txt', 'a')
for i in v:
    if i.isalpha():
        f1.write(i)
    if i.isnumeric():
        f2.write(i)
f1.close()
f2.close()
f.close()


# 7️ Search for a specific word in a file and replace it with another word.
f = open('file1.txt', 'r')
v = f.read()
l = v.split()
f = open('file1.txt', 'w')
if 'who' in l:
    l[l.index('who')] = 'how'
for i in l:
    f.write(i + ' ')
f.close()


# 8️ Split two words in a file and store them in two different files.
f = open('file1.txt', 'r')
v = f.read()
l = v.split(' ')
f1 = open('file11.txt', 'w')
f2 = open('file12.txt', 'w')
if len(l) >= 2:
    f1.write(l[0])
    f2.write(l[1])
f1.close()
f2.close()
f.close()
