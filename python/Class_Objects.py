# Demonstration of object creation and behavior in Python classes

# ----------------------------------------------------------
# Example 1: Without using parentheses ()

class Human:
    eyes = 2  # Class attribute
    legs = 2  # Class attribute

    def walking():
        print('Can walk')

    def talking():
        print('Can talk')


print("Example 1: Without parentheses in object creation")
anu = Human  # Missing parentheses () — refers to class, not instance
print(anu.legs)
print('------------------')
arun = Human
print(arun.legs)
print('*****************')
anu.legs = 1  # Changes class-level variable, affects both
print(anu.legs)
print(arun.legs)
print("\n---------------------------------------------\n")


# ----------------------------------------------------------
# Example 2: With parentheses () — correct object creation

class Human:
    eyes = 2
    legs = 2

    def walking():
        print('Can walk')

    def talking():
        print('Can talk')


print("Example 2: With parentheses")
anu = Human()  # Correct
print(anu.legs)
print('------------------')
arun = Human()  # Correct
print(arun.legs)
print('*****************')
anu.legs = 1
print(anu.legs)
print(arun.legs)
print("\n---------------------------------------------\n")


# ----------------------------------------------------------
# Example 3: Without parentheses () — methods still callable

class Human:
    eyes = 2
    legs = 2

    def walking():
        print('Can walk')

    def talking():
        print('Can talk')


print("Example 3: Without parentheses - method access")
anu = Human
anu.walking()
print('------------------')
arun = Human
arun.walking()
print("\n---------------------------------------------\n")


# ----------------------------------------------------------
# Example 4: With parentheses () — causes TypeError (no self)
# Corrected by adding 'self' in next example

print("Example 4: Error occurs without self parameter")
try:
    class Human:
        eyes = 2
        legs = 2

        def walking():
            print('Can walk')

        def talking():
            print('Can talk')

    anu = Human()
    anu.walking()  #  Error here
except TypeError as e:
    print("Error:", e)
print("\n---------------------------------------------\n")


# ----------------------------------------------------------
# Example 5: Correct version — using self

class Human:
    eyes = 2
    legs = 2

    def walking(self):
        print('Can walk')

    def talking(self):
        print('Can talk')


print("Example 5: Correct way using self")
anu = Human()
anu.walking()
print('------------------')
arun = Human()
arun.walking()
print("\n---------------------------------------------\n")


# ----------------------------------------------------------
# Example 6: Using any variable name instead of 'self'

class Human:
    eyes = 2
    legs = 2

    def walking(s):
        print('Can walk')

    def talking(self, a):
        print('Can talk')
        print(a)


print("Example 6: Using custom variable instead of self")
anu = Human()
anu.walking()
anu.talking(2)
print('------------------')
arun = Human()
arun.walking()
print("\n---------------------------------------------\n")


# ----------------------------------------------------------
# Example 7: Attributes & methods example

class Human:
    eyes = 2
    legs = 2

    def walking(self):
        print('Can walk')

    def talking(self):
        print('Can talk')


print("Example 7: Class attributes and object differences")
anu = Human()
print('-------- Anu ----------')
anu.walking()
print(anu.legs)

print('-------- Arun ----------')
arun = Human()
arun.walking()
print(arun.legs)

print('-------- Anu and Arun ----------')
anu.walking()
anu.legs = 1
print("Anu legs:", anu.legs)
arun.walking()
print("Arun legs:", arun.legs)
print("\n---------------------------------------------\n")


# ----------------------------------------------------------
# Example 8: Rectangle area and perimeter using class attributes

class Rectangle:
    l = 5
    w = 4

    def area(self):
        print('Area =', self.l * self.w)

    def perimeter(self):
        print('Perimeter =', 2 * (self.l + self.w))


print("Example 8: Rectangle using fixed attributes")
obj = Rectangle()
obj.area()
obj.perimeter()
print("\n---------------------------------------------\n")


# ----------------------------------------------------------
# Example 9: Rectangle using parameters

class Rectangle:
    def area(self, l, w):
        print('Area =', l * w)

    def perimeter(self, l, w):
        print('Perimeter =', 2 * (l + w))


print("Example 9: Rectangle using parameters")
obj = Rectangle()
obj.area(5, 4)
obj.perimeter(5, 4)
print("\n---------------------------------------------\n")


# ----------------------------------------------------------
# Example 10: Rectangle using constructor (__init__)

class Rectangle:
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def area(self):
        print('Area =', self.l * self.w)

    def perimeter(self):
        print('Perimeter =', 2 * (self.l + self.w))


print("Example 10: Rectangle using constructor")
obj = Rectangle(5, 4)
obj.area()
obj.perimeter()
print("\n---------------------------------------------\n")


# ----------------------------------------------------------
# Example 11: Human with constructor parameter

class Human:
    eyes = 2
    legs = 2

    def __init__(self, name):
        print('I am a human, my name is', name)

    def walking(self):
        print('Can walk')

    def talking(self):
        print('Can talk')


print("Example 11: Human class with constructor")
anu = Human('Anu Mol')
anu.walking()
print('------------------')
arun = Human('Arun S')
arun.walking()
print("\n---------------------------------------------\n")


# ----------------------------------------------------------
# Example 12: Constructor variable used inside methods

class Human:
    eyes = 2
    legs = 2

    def __init__(self, name):
        self.fname = name  # Instance variable

    def walking(self):
        print(f'{self.fname} can walk')

    def talking(self):
        print(f'{self.fname} can talk')


print("Example 12: Using constructor variables inside methods")
anu = Human('Anu')
anu.walking()
anu.talking()
print('------------------')
arun = Human('Arun')
arun.walking()
arun.talking()
