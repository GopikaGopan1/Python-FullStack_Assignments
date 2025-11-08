# increasing tri
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()

# dec tri
n=5
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()

# right inc tri
n=5
for i in range(n):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

# right dec tri
n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()

# up hill
n=5
for i in range(n):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

# down hill
n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(n-i-1):
        print('*',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()


# diamond

n=5
for i in range(n-1):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(2*i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for j in range(2*(n-i)-1):
        print('*',end=' ')
    print()


# or

n=5
for i in range(n-1):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for j in range(n-i-1):
        print('*',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()


# diamond easy

n=5
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(2*i+1):
        print('*',end=' ')
    print()
for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(2*i+1):
        print('*',end=' ')
    print()
# --------------------------------------------------
n=10
for i in range(n):
    for j in range(n-i): 
        print(".",end=" ") 
    for j in range(2*i-1): 
        print(" ",end=" ")
    if i==0:
        for j in range(n-1):
            print('.',end=' ')
    else:
        for j in range(n-i): 
            print(".",end=" ") 
    print() 
for i in range(n-1,-1,-1):
    for j in range(n-i): 
        print(".",end=" ") 
    for j in range(2*i-1): 
        print(" ",end=" ")
    if i==0:
        for j in range(n-1):
            print('.',end=' ')
    else:
        for j in range(n-i): 
            print(".",end=" ") 
    print() 
# ----------------------------------
n = 10  # Size of the diamond (adjustable)
n=10
for i in range(n):
    for j in range(2 * n - 1):
        if j < n - i - 1 or j > n + i - 1:
            print(".", end=" ")  # Outer dots
        elif j == n - i - 1 or j == n + i - 1:
            print(".", end=" ")  # Diamond border
        else:
            print(" ", end=" ")  # Inside space
    print()

for i in range(n - 1, -1, -1):
    for j in range(2 * n - 1):
        if j < n - i - 1 or j > n + i - 1:
            print(".", end=" ")  # Outer dots
        elif j == n - i - 1 or j == n + i - 1:
            print(".", end=" ")  # Diamond border
        else:
            print(" ", end=" ")  # Inside space
    print()

# ---------------------------------------------------
scribbled='OLONSEIGHCET'
word='NOON'
for i in word:
    if scribbled.count(i)<word.count(i):
        print('ABSENT')
        break
    else:
        print('PRESENT')
        break
# check("MIND","INDM")
# check("NOON","OLONSEIGHCET")
