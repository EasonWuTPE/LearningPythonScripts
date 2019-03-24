#1/usr/bin/python3.6 

''' 
    [Note] 
        Composites not inheritance. 
''' 
# Embedding-based Manager alternative. 
class Person: 
    def __init__(self,name,job=None,pay=0): 
        # Called when the instance is made. 
        self.name = name 
        self.job = job 
        self.pay = pay 
        # The name, jobs and pay become state information -- descriptive data saved on an object for latter use. 

    def lastName(self): 
        return self.name.split()[-1] 

    #@rangetest(percent=(0.0,1.0)) # An function decorator.  
    def giveRise(self, percent): 
        #self.pay = int(self.pay *(1+percent)) 
        return int(self.pay*(1+percent)) 

    def __repr__(self): 
        return "[Persion: %s, %s]"%(self.name,self.pay) 

    def __add__(self, x ): 
        return self.pay + x 

''' 
    [Note] 
        Delegation -- a composite-based structure that manages a wrapped object and propagates method calls to it. 
''' 
class Manager: 
    def __init__(self, name, pay): 
        self.person = self.Person(name,'mgr',pay) # Embed a Person object.  
    
    def giveRise(self, percent, bonus = 0.1): 
        self.person.giveRise( percent+bonus ) # Intercept and delegate. 

    def __getattr__(self,attr): 
        return getattr(self.person,attr) # Delegate all other attris. 

    def __repr__(self): 
        return str(self.person) # Overload again. 

class Department: 
    def __init__(self,*args): 
        self.members = list(args) 

    def addMember(self, person): 
        self.members.append(person) 

    def giveRise(self,percent): 
        for person in self.members: 
            person.giveRise(percent)

    def showAll(self): 
        for person in self.members: 
            print(person) 


if __name__ == '__main__': 
    # When this script is executed, then the attribute of__name__ is '__main__'. 
    Bob = Person('Bob') 
    Sue = Person("Sue",job = 'dev', pay = 100000) 
    print( Bob.name, Sue.job, sep='\n' ) 
    print( Bob.lastName(), Sue.lastName() ) 
    print( Sue.pay ) 
    print( Sue.giveRise(0.03) ) 
    print("Operator Overloading __repr__():", Sue ) 
    print("Operator Overloading __add__():", Sue+100 ) 
    print("Operator Overloading __repr__():", Bob ) 
    ''' 
        [Note] 
             __init__() can be inherited from its superclass "Person". 
    '''  
    #Tom = Manager("Tom Jones", 'mgr', 50000) 
    Tom = Manager("Tom Jones", 50000) 
    print( Tom ) # Runs inherited __repr__ 
    print(Tom.giveRise(.1)) 
    #print(Tom.pay) 

    print("All there.") 
    for obj in [Bob,Sue,Tom]: 
        obj.giveRise(0.1) 
        print(obj) 
