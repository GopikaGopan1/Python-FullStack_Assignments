# -------------------------------
# Heart pattern

n = 10  
for i in range(n // 2, n + 1, 2):
    for j in range(1, n - i, 2):          
        print(" ", end=" ")

    for j in range(1, i + 1):             
        print("*", end=" ")
    
    for j in range(1, (n - i) + 1):        
        print(" ", end=" ")
    
    for j in range(1, i + 1):              
        print("*", end=" ")
    print()
for i in range(n, 0, -1):
    for j in range(n, i, -1):
        print(" ", end=" ")
    for j in range(1, (i * 2)):
        print("*", end=" ")
    print()
# --------------------------------------------------------
# number cross pattern
n = 5
for i in range(1,(2*n)):
    if i<n:
        t=i  
    else:
        t=2* n-i
    for j in range(1,(2*n)):
        if i == j or i + j == (2 * n):
            print(t, end="")
        else:
            print(" ", end="")
    print()
# ------------------------------------------------
# hallow diamond pattern
n = int(input("enter the number of rows:")) 
for i in range(n,0,-1): 
    for j in range(i,0,-1): 
        print(".",end=" ") 
    for j in range(2*(n-i)): 
        print(" ",end=" ") 
    for j in range(i,0,-1): 
        print(".",end=" ") 
    print() 
for i in range(n): 
    for j in range(i+1): 
        print(".",end=" ") 
    for j in range (2*(n-i-1)): 
        print(" ",end=" ") 
    for j in range(i+1): 
        print(".",end=" ") 
    print()
# ------------------------------------------------
# number pattern
n = 7
for i in range(1, n + 1):
    num = i
    for j in range(1, i + 1):
        print(num, end=" ")
        num += (n - j)
    print()

# --------------------------------------------
# scribbled

def check(word,scribbled):
    for i in word:
        if scribbled.count(i)<word.count(i):
            print('ABSENT')
            break
    else:
        print('PRESENT')
check("TRAVIDUX","VRIDAUTX")
check("NOON","OLONSEIGHCET")

# ---------------------------------------------------- Output ------------------------------------------------------------------------------------------------
"""
    * * * * *           * * * * * 
  * * * * * * *       * * * * * * *
* * * * * * * * *   * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
  * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * *
      * * * * * * * * * * * * *
        * * * * * * * * * * *
          * * * * * * * * *
            * * * * * * *
              * * * * *
                * * *
                  *

1       1
 2     2
  3   3
   4 4
    5
   4 4
  3   3
 2     2
1       1

enter the number of rows:10
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . .     . . . . . . . . .
. . . . . . . .         . . . . . . . .
. . . . . . .             . . . . . . .
. . . . . .                 . . . . . .
. . . . .                     . . . . . 
. . . .                         . . . .
. . .                             . . .
. .                                 . .
.                                     .
.                                     .
. .                                 . .
. . .                             . . .
. . . .                         . . . .
. . . . .                     . . . . .
. . . . . .                 . . . . . .
. . . . . . .             . . . . . . .
. . . . . . . .         . . . . . . . .
. . . . . . . . .     . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .

1
2 8
3 9 14
4 10 15 19
5 11 16 20 23
6 12 17 21 24 26
7 13 18 22 25 27 28

PRESENT
ABSENT """   
