# --------------------------------------------------- Library management ---------------------------------------------------------------------------------------------------
# design a cls hierarchy to represent a library system. create a base cls Book that contains attr such as title,author,and isbn .
# then, create subcls for diff types of books ,such as fictionbook,nonfic, and magazine .each subcls should have an additional unique attr , 
# such as genre for fictionbook,subject for nonficbook , and issuenum for magazine .implement methods for printing the details of each type of book.

# in base book cls ,define common attr and methods like display_details().in each subcls ,
# introduce specific attr and override display_details() to reflect unique info


class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display_details(self):
        print(f'book title :- {self.title} \nbook author :- {self.author} \nbook isbn :- {self.isbn}')

class Ficition(Book):
    def __init__(self, title, author, isbn,genre):
        Book.__init__(self,title,author,isbn)
        self.genre=genre
    def display_details(self):
        print('-----ficitional book-------')
        print(f'book title :- {self.title} \nbook author :- {self.author} \nbook isbn :- {self.isbn}, \ngenre :- {self.genre}')

class Nonficition(Book):
    def __init__(self, title, author, isbn,subject):
        Book.__init__(self,title,author,isbn)
        self.subject=subject
    def display_details(self):
        print('-----non-ficitional book-------')
        print(f'book title :- {self.title} \nbook author :- {self.author} \nbook isbn :- {self.isbn},\nsubject :- {self.subject}')

class Magazine(Book):
    def __init__(self, title, author, isbn,issue_num):
        Book.__init__(self,title,author,isbn)
        self.issue_num=issue_num
    def display_details(self):
        print('-----Magazine------')
        print(f'book title :- {self.title} \nbook author :- {self.author} \nbook isbn :- {self.isbn},\nissue_num :- {self.issue_num}')
    
obj=Ficition(input('enter title of Book : '),input('enter author name : '),int(input('enter isbn num : ')),input('enter genre : '))

obj2=Nonficition(input('enter title of Book : '),input('enter author name : '),int(input('enter isbn num : ')),input('enter subject : '))

obj3=Magazine(input('enter title of Book : '),input('enter author name : '),int(input('enter isbn num : ')),int(input('enter issue_num: ')))

obj.display_details()
obj2.display_details()
obj3.display_details()
# ------------------------------------------- Employee ---------------------------------------------------------------------------------------------------------
# employee
# create a cls hierarchy to represent emply in a company. the basecls employee should have basic attri like name,position,salary.
# then create subcls such as manaager ,engineer and intern ,where each subcls has unique attributes like department for manager or
# project for engineer . demonstrate how inheritance allow common behaviour to be shared and specialized beh to be added.

# base cls employee , has common attr and method get_sal()
# in sub cls introduce specific attributes.show how each empl type have additional responsibilities and
#  how they inherit common functionality from employee

class Employee:
    def __init__(self,name,position,salary):
        self.n=name
        self.p=position
        self.s=salary
    def get_salary(self):
        print(f'salary : {self.s}')
class Manager(Employee):
    def __init__(self, name, position, salary,dep):
        Employee.__init__(self,name,position,salary)
        self.dep=dep
        print('department : ',dep)
class Engineer(Employee):
    def __init__(self, name, position, salary,project):
        Employee.__init__(self,name, position, salary)
        self.project=project
        print('project :',project)
class Intern(Employee):
    def __init__(self, name, position, salary,duration):
        Employee.__init__(self,name, position, salary)
        self.duration=duration
        print('duration : ',duration)
obj=Manager(input('enter name : '),input('enter position : '),int(input('enter salary : ')),input('enter department : '))
obj.get_salary()

obj1=Engineer(input('enter name : '),input('enter position : '),int(input('enter salary : ')),input('enter project: '))
obj1.get_salary()

obj2=Intern(input('enter name : '),input('enter position : '),int(input('enter salary : ')),input('enter duration: '))
obj2.get_salary()

# -----------------------------------------------------------------------------------------------------------------------------------------------------

# 1.create  a cls vehicle with attr brand and speed . write a method drive that prints 'driving at speed x'.
# derive a cls car from vehicle and add an attr seats ,write a method to display all details of the car.
# 2.create a base cls appliance with methods power on , derive two clss, washing machine and refrigerator that add specific attrs and methods
# 3.implement multilevel inheritance
# class device -- class phone --- class smartphone
# # add methods and attr at each level
# --------------------------------------------------------------------------------------------------
class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def drive(self):
        print(f'driving at speed {self.speed}')
class Car(Vehicle):
    def __init__(self,brand,speed,seats):
        Vehicle.__init__(self,brand,speed)
        self.seats=seats
    def car_details(self):
        print('-----------------------------------------------------------------------------')
        print(f'This car has {self.seats} seats \nbrand: {self.brand}')
obj=Car(input('enter car brand :'),int(input('enter speed : ')),int(input('enter no.of seats : ')))
obj.car_details()
obj.drive()
# ----------------------------------------------------------------------------------------------------

# # -------------------------------------------------------------------------------------------------------------------------------------------
# # class device -- class phone --- class smartphone
class Device:
    def __init__(self,mdate):
        self.mdate=mdate
    def details(self):
        print(f'The device is manufactured in {self.mdate} ')
class Phone(Device):
    def __init__(self,mdate,type):
        Device.__init__(self,mdate)
        self.type=type
    def Phone_details(self):
        print(f'by company : {self.type}')
class Smartphone(Phone):
    def __init__(self,mdate,type,model,color):
        Phone.__init__(self,mdate,type)
        self.color=color
        self.model=model
        self.details()
        self.Phone_details()
    def sdetails(self):
        print(f'model : {self.model} \ncolor : {self.color}')
obj=Smartphone(int(input('enter m-date : ')),input('enter brand : '),input('enter model : '),input('enter color : '))
obj.sdetails()

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# 4. you have 2 base classes ,shape and color . shape has a method area that returns the area and
#  color has a method fill that describes the color. create a subcls coloredshape that inherits from both
#   shape and color but doesnt override the fill or area methods

#   task:
#   define a shape cls with amethod area (eg. for a rect)
# define a color cls with a method fill that returns the color
# create a coloredshape cls that inherits from both shape and color but doent override their methods 
# instatiate an obj of coloredshape and demonstrate that it call both area and fill.

class Shape:
    def __init__(self,shape):
        self.shape=shape
    def Area(self):
        print(f'area of {self.shape} : 20cm ')
class Color:
    def __init__(self,color):
        self.color=color
    def fill(self):
        print(f'color : {self.color}')
class ColoredShape(Shape,Color):
    def __init__(self,shape,color):
        Shape.__init__(self,shape)
        Color.__init__(self,color)
        self.Area()
        self.fill()
    def cshape(self):
        print(f'{self.shape} shape filled with {self.color} color')
obj=ColoredShape(input('enter shape : '),input('enter color : '))
obj.cshape()

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Task:
# create a cls person with a greet method
# create a class worker with a work method
# create a manager cls that inherits from both person and worker .demonstrate that manager can use both greet and work methods

class Person:
    def greet(self):
        print('can greet')
class Worker:
    def work(self):
        print('can work')
class Manager(Person,Worker):
    def manage(self):
        self.greet()
        self.work()
        print('can manage')
obj=Manager()
obj.manage()
# -------------------------------------------------------------------------------------------------------------------------------

# 1. create an abstract base class employee with abstract methods like calculate_sal and concrete methods like get_details.
#  inherit  classes manager and developer from it and implement the abstract methods

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def cal_sal(self,sal):
        pass
        # print(f'salary :{sal} ')
    def get_details(self):
        print(f'Name : {self.name} , id : {self.id}')
class Manager(Employee):
    def __init__(self, name, id):
        Employee.__init__(self,name, id)
        self.cal_sal()
        self.get_details()
    def mang_details(self):
        print(f'is Manager Salary: {self.cal_sal()}')
class Developer(Employee):
    def developer(self):
        print('is developer')



# 2.hybrid inheritance
class A:
    def methodA(self):
        print('parent class: A')
class B(A):
    def methodB(self):
        print('Has properties of : ')
        self.methodA()
        print('child class B')
class C(A):
    def methodC(self):
        print('Has properties of : ')
        self.methodA()
        print('child class C')
    def methodCP(self):
        print('C parent class of D')
class D(C):
    def methodD(self):
        print('Has properties of : ')
        self.methodCP()
        self.methodA()
        print('properties of D')

print('-------------- hierarchical 1-------------------------')
obj1=C()
obj1.methodC()
print('--------------h 2-----------------')
obj3=B()
obj3.methodB()
print('--------------multilevel----------------')
obj2=D()
obj2.methodD()

# ------------------------------------------------------------------------------------------------------------------------------------
# super()


class A:
    def __init__(self):
        print('-------parent cls constructor --------')
        print('Arun')
    def fun1(self):
        print('-----parent cls method--------')
        print('varun')
class B(A):
    def __init__(self):
        print('-----child constructed is invoked when an obj of child cls is created and called-------')
        print('jerin')
    def fun2(self):
        print('----child class method-----')
        print('sam')
        super().__init__() #using super()
obj1=B()
obj1.fun1()
obj1.fun2()


# ---------------------------------------------------------------------------------------------------------------------------------------
# without super()

class A:
    def __init__(self):
        print('-------parent cls constructor --------')
        print('Arun')
    def fun1(self):
        print('-----parent cls method--------')
        print('varun')
class B(A):
    def __init__(self):
        print('-----child constructed is invoked when an obj of child cls is created and called-------')
        print('jerin')
    def fun2(self):
        print('----child class method-----')
        print('sam')
        A.__init__(self) #without super() , using parentcls name
obj1=B()
obj1.fun1()
obj1.fun2()

# ------------------------------------------Abstraction (hiding)--------------------------------------------------------------------------------------------------------
# Abstract

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def display(self):
        print('this is a shape')
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(f'area of rectangle : {self.l*self.b}')
    def perimeter(self):
        print(f'perimeter of rectangle :{2*(self.l+self.b)}')
obj1=Rectangle(10,20)
obj1.area()
obj1.perimeter()
# ---------------------------------------------------------------------------------------------------------------------------------------

# abstract base cls simple calculator

from abc import ABC,abstractmethod
class Simple_cal:
    @abstractmethod
    def add(self):
        pass
    def sub(self):
        pass
    def mult(self):
        pass
    def div(self):
        pass
class Calculator(Simple_cal):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(f'{self.a} + {self.b} = {self.a+self.b}')
    def sub(self):
        print(f'{self.a} - {self.b} = {self.a-self.b}')
    def mult(self):
        print(f'{self.a} * {self.b} = {self.a*self.b}')
    def div(self):
        print(f'{self.a} / {self.b} = {self.a/self.b}')
obj=Calculator(1,2)
obj.add()
obj.sub()
obj.mult()
obj.div()
# ----------------------------------------------- Polymorphism----------------------------------------------------------------------------------------------------
#method overriding

# same function  'make_sound' in parent cls is  overridden in child cls

class Animal:
    def make_sound(self):
        print('Animals can make sounds')
class Dog(Animal):
    def make_sound(self):
        print('can make woof sound')
class Cat(Animal):
    def make_sound(self):
        print('can make meow sound')
obj1=Cat()
obj1.make_sound()
obj2=Dog()
obj2.make_sound()
    

    # eg:2

class Parent:
    def greet(self):
        print('hello,Parent here')
class Child:
    def greet(self):
        print('hello,Child here')
obj=Child()
obj.greet()
obj1=Parent()
obj1.greet()





# -------------------------------------------------------------------------------------------------------------------------------------------------

# Polymorphism Calculator

class Basic_Cal:
    def Operations(self,a,b,op):
        self.a=a
        self.b=b
        self.op=op
        if self.op =='+':
            return f'{self.a+self.b}'
        elif self.op =='-':
            return f'{self.a-self.b}'
        elif self.op =='*':
            return f'{self.a*self.b}'
        elif self.op =='/':
            return f'{self.a/self.b}'
class Sci_cal(Basic_Cal):
    def Operations(self,a,b,op):
        # self.Operations()
        self.a=a
        self.b=b
        self.op=op
        if self.op=='**':
            print(f'{self.a} {self.op} {self.b}={self.a**self.b}')
sciobj=Sci_cal()
basicobj=Basic_Cal()
i=0
while i<5:
    a=int(input('enter first number : '))
    b=int(input('enter second number : '))
    op=input('enter operator : ')
    if op=='+' or op=='-' or op=='*' or op=='/':
        print(basicobj.Operations(a,b,op))
    elif op=='**':
        sciobj.Operations(a,b,op)
    elif op=='exit':
        break
