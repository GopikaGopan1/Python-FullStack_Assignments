# __________________________________________WORKOUT PROBLEMS USING FUNCTIONS______________________________________________

# 1) Cube of any number
def cubeofnum(n):
    b = n ** 3
    return b
c = cubeofnum(2)
print("Cube:", c)

# 2) Diameter, circumference, and area of a circle
def circle(r):
    d = 2 * r
    area = 3.14 * (r ** 2)
    c = 2 * 3.14 * r
    print('Diameter:', d)
    print('Area:', area)
    print('Circumference:', c)
circle(2)

# 3) Find max and min between two numbers
def find(a, b):
    if a < b:
        print(a, 'is min', b, 'is max')
    else:
        print(b, 'is min', a, 'is max')
find(125, 50)

# 4) Even or odd
def evenorodd(a):
    if a % 2 == 0:
        print(a, 'is even')
    else:
        print(a, 'is odd')
evenorodd(7)

# 5) Prime, Armstrong, Perfect numbers
def number(a):
    flag = 0
    sum1 = 0
    for i in range(2, a):
        if a % i == 0:
            flag = 1
    if flag == 0:
        print(a, "is prime")
    for i in range(1, a):
        if a % i == 0:
            sum1 += i
    if sum1 == a:
        print('Perfect number')
    n = a
    count = 0
    while n > 0:
        n //= 10
        count += 1
    res = 0
    b = a
    while b > 0:
        r = b % 10
        b //= 10
        res += r ** count
    if a == res:
        print("Armstrong")
number(153)

# __________________________________________LARGEST ELEMENT IN LIST_____________________________________________________

def largest(list1):
    print('Largest is:', max(list1))
n = int(input('Enter limit: '))
print('Enter array elements:')
l = [int(input()) for i in range(n)]
largest(l)

# __________________________________________ANAGRAM CHECK_____________________________________________________

def anagram(a, b):
    if sorted(a) == sorted(b):
        print('Is anagram')
    else:
        print('Not anagram')
anagram('spear', 'pears')

# __________________________________________PRIME NUMBERS UPTO LIMIT_____________________________________________________

def prime(l1):
    for i in l1:
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
        if flag == 0 and i > 1:
            print(i)
a = int(input('Enter start limit: '))
b = int(input('Enter stop limit: '))
list1 = [i for i in range(a, b + 1)]
prime(list1)

# __________________________________________STRONG NUMBER_____________________________________________________

def strong(a):
    list1 = [i for i in str(a)]
    sum1 = 0
    for n in list1:
        fact = 1
        for i in range(int(n), 0, -1):
            fact *= i
        sum1 += fact
    if sum1 == a:
        print('Strong')
    else:
        print('Not strong')
strong(145)

# __________________________________________ALL ARMSTRONG NUMBERS TO LIMIT_____________________________________________________

def armstronglimit(l1):
    for i in l1:
        b = i
        sum1 = 0
        c = len(str(b))
        while b > 0:
            r = b % 10
            b //= 10
            sum1 += r ** c
        if i == sum1:
            print(i)
a = int(input('Enter start limit: '))
b = int(input('Enter stop limit: '))
list1 = [i for i in range(a, b + 1)]
armstronglimit(list1)

# __________________________________________PERFECT NUMBERS TO LIMIT_____________________________________________________

def perfectlimit(l):
    for i in l:
        sum1 = 0
        for j in range(1, i):
            if i % j == 0:
                sum1 += j
        if sum1 == i:
            print(i)
a = int(input('Enter start limit: '))
b = int(input('Enter stop limit: '))
list1 = [i for i in range(a, b + 1)]
perfectlimit(list1)

# __________________________________________RECURSION FUNCTIONS__________________________________________________________

# Factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial:", factorial(5))

# Natural numbers using recursion
def natural_numbers(n):
    if n > 0:
        natural_numbers(n - 1)
        print(n)
natural_numbers(5)

# Power using recursion
def power(n, p):
    if p == 0:
        return 1
    else:
        return n * power(n, p - 1)
print("Power:", power(2, 3))

# Even and odd numbers using recursion
def print_even(start, end):
    if start > end:
        return
    if start % 2 == 0:
        print(start, end=' ')
    print_even(start + 1, end)

def print_odd(start, end):
    if start > end:
        return
    if start % 2 != 0:
        print(start, end=' ')
    print_odd(start + 1, end)

print("\nEven numbers:")
print_even(1, 10)
print("\nOdd numbers:")
print_odd(1, 10)

# Sum of natural numbers
def natural_sum(n):
    if n == 0:
        return 0
    return n + natural_sum(n - 1)
print("Sum of natural numbers:", natural_sum(5))

# Sum of even and odd numbers in range
def sum_even(start, end):
    if start > end:
        return 0
    if start % 2 == 0:
        return start + sum_even(start + 1, end)
    return sum_even(start + 1, end)

def sum_odd(start, end):
    if start > end:
        return 0
    if start % 2 != 0:
        return start + sum_odd(start + 1, end)
    return sum_odd(start + 1, end)

print("Sum of even numbers:", sum_even(1, 10))
print("Sum of odd numbers:", sum_odd(1, 10))

# Reverse of a number using recursion
def reverse_num(n, rev=0):
    if n == 0:
        return rev
    else:
        r = n % 10
        rev = rev * 10 + r
        return reverse_num(n // 10, rev)
print("Reverse:", reverse_num(1234))

# Fibonacci series
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
print("Fibonacci(6):", fib(6))

# __________________________________________PALINDROME CHECK______________________________________________________________

def is_palindrome(num, rev=0):
    if num == 0:
        return rev
    else:
        return is_palindrome(num // 10, rev * 10 + num % 10)
a = 121
v = is_palindrome(a)
if a == v:
    print(a, "is palindrome")
else:
    print(a, "not palindrome")

# Sum of digits using recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    return abs(n % 10) + sum_of_digits(n // 10)
print("Sum of digits:", sum_of_digits(1234))

# __________________________________________ARRAY OPERATIONS USING RECURSION_____________________________________________

def display_array(a, i=0):
    if i == len(a):
        return []
    return [a[i]] + display_array(a, i + 1)
l = [10, 20, 30, 40, 50]
print("Array elements:", display_array(l))

def print_array_recursively(a, i=0):
    if i == len(a):
        return
    print(a[i])
    print_array_recursively(a, i + 1)
print("Printing array:")
print_array_recursively(l)

def sum_array(a, i=0):
    if i == len(a):
        return 0
    return a[i] + sum_array(a, i + 1)
print("Sum of array:", sum_array(l))

def find_max(a):
    if len(a) == 1:
        return a[0]
    return max(a[0], find_max(a[1:]))

def find_min(a):
    if len(a) == 1:
        return a[0]
    return min(a[0], find_min(a[1:]))

print("Max:", find_max(l))
print("Min:", find_min(l))

# __________________________________________HIGHER ORDER FUNCTIONS________________________________________________________

def first(a, b):
    print('Inside first function')
    def second(c):
        print('Inside second function')
        print(a, b, c)
        s = a + b + c
        print('Sum:', s)
    return second
val = first(2, 5)
val(4)

def sum_func(a, b):
    def avg(c):
        d = (a + b) / c
        print('Average:', d)
    return avg
v = sum_func(6, 3)
v(2)
