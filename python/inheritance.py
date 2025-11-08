# single inheritance
# --------------------
class Human:
    def walking(self):
        print('can walk')
    def talking(self):
        print('can talk')
class Teacher(Human):
    def teach(self):
        print('can teach')
Anjana=Teacher()
Anjana.walking()
Anjana.talking()
Anjana.teach()

# multiple inheritance
# ----------------------
class Father:
    age=45
    def __init__(self,fname):
        self.fname=fname
        print(f'name of father {fname}')
    def show_father(self):
        print('im father')
class Mother:
    age=45
    def __init__(self,mname):
        self.mname=mname
        print(f'name of mother {mname}')
    def show_mother(self):
        print('im mother')
class Child(Father,Mother):
    def __init__(self, fname,mname,cname):
        Father.__init__(self,fname)
        Mother.__init__(self,mname)
        self.cname=cname
        print(f'my name is {cname}')
    def show_child(self):
        print('im the child')
Anu=Child('manu','shiny','anu mol')
Anu.show_child()

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# multilevel inheritance
    
class Grandfather:
    age=75
    def __init__(self,gname):
        self.gname=gname
        print(f'name of grandfather {gname}')
    def show_gfather(self):
        print('im grandfather')
class Father(Grandfather):
    age=45
    def __init__(self,fname):
        self.fname=fname
        print(f'name of father {fname}')
    def show_father(self):
        print('im mother')
class Child(Father):
    def __init__(self,gname,fname,cname):
        Grandfather.__init__(self,gname)
        Father.__init__(self,fname)
        self.cname=cname
        print(f'my name is {cname}')
    def show_child(self):
        print('im the child')
Anu=Child('nadaraj','manu','anu mol')
Anu.show_gfather()
Anu.show_child()
