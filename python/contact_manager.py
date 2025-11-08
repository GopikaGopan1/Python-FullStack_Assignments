'''1: Add new contact
2: View : Enter the contact to view(user)
3: Update :
    new_name
    new_email
    new_phone
    add all the above to the current dictionary
4: Delete :
    name of contact to be deleted(user)'''
# _______________________________________________________________________________________________________

# contact={'name':'gopika','email':'gopika1@gmail.com','phone':[9900,6392]}
# contact={'name':'anu','email':'anu1@gmail.com','phone':[6650,6392]}
# _______________________________________________________________________________________________________

contact={}
choice={1:'add contact',2:'view',3:'update',4:'delete',5:'exit'}
print(choice)
n=0
while n!=5:
    i=int(int(input('enter the choice : ')))
    if i==1:
        name=input('enter your name : ')
        email=input('enter your email : ')
        phone=int(input('enter phone number : '))
        mincontact={'name':name,'email':email,'phone':phone}
        contact[name]=mincontact
        print(contact)
    elif i==2:
        c=input('enter the contact name to view : ')
        if c in contact:
            print(contact[c])
        else:
            print('enter valid contact')
    elif i==3:
        c=input('update contact : ')
        if c in contact:
            print(contact[c])
        else:
            print('enter valid contact')
        contact.pop(c)
        new_name=input('enter your name : ')
        new_email=input('enter your email : ')
        new_phone=int(input('enter phone number : '))
        mincontact={'name':new_name,'email':new_email,'phone':new_phone}
        contact[new_name]=mincontact
        print(contact)
    elif i==4:
        c=input('enter the contact to delete : ')
        if c in contact:
            print(contact[c])
        else:
            print('enter valid contact')
        contact.pop(c)
        print(contact)
    elif i==5:
        print('exiting')
        break
    else:
        print('index out of range')
        break
    


