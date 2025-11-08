# unordered collection, mutable, no duplicate elements, elements must be immutable
a = {100, 1, 2, 3, 4}

# create an empty set
a = set()
print(a)  # prints empty set
print(type(a))  # prints <class 'set'>

# set with mixed immutable types
a = {1, 2, (1, 2, 3), 8, 4, 10, 't'}

# sets cannot have mutable elements like lists or other sets (uncommenting below causes error)
# a = {1, 2, [1, 2, 3]}  # list not allowed inside set
# a = {1, 2, {1, 2, 3}}  # set not allowed inside set

# create set from tuple
a = set((1, 2, 3, 4, 5, 6, 7, 8))

# sets do not support indexing (uncommenting below causes error)
# print(a[0])
print(a)  # prints the set
print(type(a))  # confirms it is a set

# duplicates in set are automatically removed
a = {1, 2, 3, 4, 5, 3, 4, 4, 9}
print(a)  # prints set without duplicates

# converting list to set removes duplicates
j = [2, 7, 3, 7, 5, 6, 8, 4, 8, 6]
print(set(j))

# sets do not allow mutable elements like other sets (uncommenting below causes error)
# j = {7, 8, 'hai', 'hai', {2}}
# print(set(j))

# Adding elements to a set
k = set()
print(k)
k.add(4)  # add single element
print(k)
# k.add(7, 8, 9)  # error, add accepts only one argument
print(k)
k.add((7, 8, 9))  # adding a tuple as a single element
print(k)
k.update((7, 8, 9))  # add each element of iterable separately
print(k)
# k.add([7, 6, 5])  # error, list not allowed inside set
print(k)
k.update([7, 8, 9])  # add each element separately
print(k)
k.add('wdnd')  # add entire string as one element
print(k)
k.update('wdnd')  # add each character separately, duplicates removed
print(k)

# Removing elements from a set
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
# del set1  # deletes entire set (uncomment to use)
set1.remove(5)  # removes element, error if not present
print(set1)
set1.remove(8)
print(set1)
# set1.remove(100)  # error if element not found
print(set1)

# discard removes element, no error if not present
set1.discard(5)
print(set1)
set1.discard(8)
print(set1)
set1.discard(100)  # no error even if element missing
print(set1)

set1.clear()  # empties the set
print(set1)

# pop removes and returns an arbitrary element (no arguments allowed)
set1 = {2, 3, 4, 5, 8, 4, 5}
print(set1)
print(set1.pop())  # removes random element
print(set1)
# print(set1.pop(5))  # error, pop takes no arguments
print(set1)

# Set operations examples
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("union =", a | b)  # union of sets
print("intersection =", a & b)  # common elements
print("difference a-b =", a - b)  # elements in a but not in b
print("difference b-a =", b - a)  # elements in b but not in a
print("symmetric difference =", a ^ b)  # elements in either set but not both

# Mutation operators (update sets in-place)
a |= b  # union update
print(a)
a &= b  # intersection update
print(a)
a -= b  # difference update (remove elements present in b)
print(a)
b -= a  # difference update on b
print(b)
a ^= b  # symmetric difference update
print(a)

# Using update methods on sets
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'msworld', 'apple'}
set1.update(set2)  # add all elements from set2 to set1
print(set1)
set1 = {'apple', 'banana', 'cherry'}
set1.intersection_update(set2)  # keep only common elements
print(set1)
set1 = {'apple', 'banana', 'cherry'}
set1.difference_update(set2)  # remove elements found in set2
print(set1)
set1 = {'apple', 'banana', 'cherry'}
set1.symmetric_difference_update(set2)  # keep elements not common in both
print(set1)

# Assigning union of two sets to a new variable
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)  # union returns a new set
print(z)

# Intersection, difference, and symmetric difference examples
set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'msworld', 'apple'}
set3 = set1.intersection(set2)
print(set3)
set3 = set1.difference(set2)
print(set3)
set3 = set1.symmetric_difference(set2)
print(set3)

# Workout question: students not placed
student = {'dan', 'jai', 'san', 'uma', 'amar', 'loh', 'pra', 'ash'}
placedstudent = {'uma', 'dan', 'amar'}
studentnotplaced = student.difference(placedstudent)  # students not in placedstudent set
print(studentnotplaced)

# Placed students from multiple companies (union of sets)
tcs = {'uma', 'dhanish', 'amritha'}
infosys = {'lohitha', 'dhanish', 'aswathy'}
vipro = {'sangeetha', 'jaison', 'prasath', 'amritha'}
placedstudents = list(tcs | infosys | vipro)  # union of all sets
print(placedstudents)
print(len(placedstudents))  # count of unique placed students

# Students placed in both TCS and Vipro (intersection)
both = tcs & vipro
print(both)

# Count of unique students placed in Vipro or Infosys
print(len(vipro | infosys))

# Difference of sets example
set1 = {1, 2, 3, 6}
set2 = {4, 5}
elements = set1 - set2  # elements in set1 not in set2
print(elements)

# Union update example
a = {1, 2, 3, 4}
b = {5, 7}
a.update(b)  # add elements from b to a
print(a)

# Union example assigning to new set
c = a.union(b)  # union returns new set
print(c)

# Remove duplicates by converting list to set
list1 = [1, 2, 3, 4, 4, 4, 5]
a = set(list1)
print(list(a))

# Intersection example
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.intersection(set2)
print(set3)

# Using '&' operator for intersection
set3 = set1 & set2
print(set3)

# Difference update removes elements found in other set
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)

