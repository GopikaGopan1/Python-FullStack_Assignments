# ============================================================================================================
#  MULTITHREADING IN PYTHON — Examples
# ------------------------------------------------------------------------------------------------------------
#  Example 1 — Without Threading
# ------------------------------------------------------------------------------------------------------------

a = [1, 2, 3, 4, 5]
def Square(l):
    for i in l:
        print(i, 'square', i**2)

def Cube(l):
    for i in l:
        print(i, 'cube', i**3)

Square(a)
Cube(a)

'''
Without threading:
First, the `Square()` function completes execution, then only `Cube()` starts.
This is a line-by-line sequential execution.
'''

# ------------------------------------------------------------------------------------------------------------
#  Example 2 — With Multithreading
# ------------------------------------------------------------------------------------------------------------

import threading
import time

a = [1, 2, 3, 4, 5]
def Square(l):
    for i in l:
        print(i, 'square', i**2)
        time.sleep(1)  # pause this thread temporarily for 1 sec

def Cube(l):
    for i in l:
        print(i, 'cube', i**3)
        # time.sleep(1)

# Creating two threads for parallel execution
t1 = threading.Thread(target=Square, args=(a,))
t2 = threading.Thread(target=Cube, args=(a,))

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

'''
With threading:
CPU switches between `Square` and `Cube`, allowing parallel execution.
So both threads run simultaneously instead of one after another.
'''

# ------------------------------------------------------------------------------------------------------------
#  Example 3 — Using Lock to Avoid Race Conditions
# ------------------------------------------------------------------------------------------------------------

import threading

x = 0
lock = threading.Lock()

def increment(lock):
    """Increment global variable 'x' safely using lock."""
    global x
    for i in range(5):
        lock.acquire()
        x += 1
        print('x +=', x)
        lock.release()

def function_1():
    """Create and start two threads safely updating shared variable x."""
    global x
    x = 0
    lock = threading.Lock()
    
    t1 = threading.Thread(target=increment, args=(lock,))
    t2 = threading.Thread(target=increment, args=(lock,))
    
    t1.start()
    print('t1 is working...')
    t2.start()
    print('t2 is working...')
    
    t1.join()
    t2.join()

# Run once
function_1()
print(f'Final increment value of x: {x}')

# ------------------------------------------------------------------------------------------------------------
#  Example 4 — Repeating Thread Execution Multiple Times
# ------------------------------------------------------------------------------------------------------------

import threading

x = 0
lock = threading.Lock()

def increment(lock):
    """Increment global variable 'x' multiple times with lock protection."""
    global x
    for i in range(5):
        lock.acquire()
        x += 1
        print('x +=', x)
        lock.release()

def function_1():
    """Create two threads that increment x safely."""
    global x
    x = 0
    lock = threading.Lock()
    
    t1 = threading.Thread(target=increment, args=(lock,))
    t2 = threading.Thread(target=increment, args=(lock,))
    
    t1.start()
    print('t1 is working...')
    t2.start()
    print('t2 is working...')
    
    t1.join()
    t2.join()

# Run multiple times to observe thread-safe incrementing
for i in range(10):
    function_1()
    print(f'Iteration {i+1}: Final increment x = {x}')

