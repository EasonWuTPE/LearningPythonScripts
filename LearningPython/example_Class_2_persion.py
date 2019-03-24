#!/usr/bin/python3.6 

# Implements on class. 

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

class Manager(Person): # Inherite from superclass Person. 
    def __init__(self,name,pay): 
        Person.__init__(self,name,'mgr',pay) 
    def giveRise(self,percent, bonus = .10): # Redefine to customize. 
        # A bad way to copy codes may double your maintaince time in the future, if changing the way raises are given.  
        #self.pay = int(self.pay*(1+percent+bonus)) 
        return Person.giveRise(self,percent+bonus) # Good one. Good to maintance in the future where the "self" is required. 
        ''' 
            [Note] 
            You must remeber to pass along the instance manually if you call through the class directly. 
                instance.method(args, ...) == class.method(instance,args,...) 
                    where the instance in class.classmethod is "self" in class scope. 

            Another way to inherit method from superclass is to use __super__() implicitly. 
        ''' 


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

''' 
    [Conclusion] 
        1. __init__() can be inherited from the superclass. 
        2. 

''' 


''' 
    Introspection tools: 
        A set of special functions and attributes that give us access to some of the internals of objects' implementations. 
        These are generally used more by people writing tools for other programmers to use than by programmers developing Apps. 
''' 
bob = Person('Bob Jones') 
print(bob) 
print(bob.__class__)
print(bob.__dict__)
print(bob.__dict__.keys())
for key in bob.__dict__: 
    print( key,"=>",getattr(bob,key)) 
print(getattr(bob,'name')) 


