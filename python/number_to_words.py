a1=['zero','one','two','three','four','five','six','seven','eight','nine']
a2=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
a3=['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety','hundred']
n=int(input('enter the number :'))
if n<10:
    print(a1[n])
elif n>=10 and n<20:
     print(a2[n%10])
elif n>=20 and n<=99:
    c=n//10
    r=n%10
    if n%10==0:
        print(a3[c-2])
    else:
        print(a3[c-2]+' '+a1[r])
else:
    q=n//100
    r=n%100
    if n%100==0:
        print(a1[q]+' '+a3[-1])
    elif n%100<10:
        print(a1[q]+' '+a3[-1]+' and '+a1[r])
    elif n%100>=10 and n%100<20:
        print(a1[q]+' '+a3[-1]+' and '+a2[r-10])
    else:
        c=r//10
        d=r%10
        if r%10==0:
            print(a1[q]+' '+a3[-1]+' and '+a3[c-2])
        else:
            print(a1[q]+' '+a3[-1]+' and '+a3[c-2]+''+a1[d])
