#!/usr/bin/python3.5 

# I. 
# Class 
''' 
    Class: 
        Class is a kind of factories to manufacture instances. 
    
        [Note] 
        1. Calling a class object like a function makes new instance object. 

        2. Each instance inherits class attributes and get its own namespace. 

        3. Assignments to attributes of self in methods make per-instance attributes. 
           Inside the class's method funtion, the first argument "self" references the instance object being processed. 
           Assignments to attributes of self create or change data in instance not the class. 

''' 
# First example 
class FirstClass():
    def setdata(self,value): 
        self.data = value 
    def display(self): 
        print(self.data) 

# Create different namespaces, or different instance. Both inherits the FirstClass.  
x = FirstClass() 
y = FirstClass() 

x.setdata("Caeser") 
y.setdata(3.14159) 

x.display() 
y.display() 

# Change instance attribute outside the class by assigning to self in method. 
x.data = "Assign outside the class" 
x.display() 
# Create new attributes outside the class's method function by assignment to self. 
y.CreateNewValueOutsideClass = 'Create New Value Outside the Class' 
print(y.CreateNewValueOutsideClass) 
''' 
    [Note]
    1. Classes usually create all of the instance's attributes by assigment to the self argument. 
    2. The argument self is the instance itself. 
    3. The instance can create new attributes outside the class's method function by assigment to self. 
        i.e. Object.NewVariable = 100, where .NewVariable is not defined in the class. 
''' 

# II. 
''' 
    Class:
        Classes are customized by inheritance. 

        [Note] 
        1. Superclass are listed in parenthese in a class header. 
        2. Classes inherit attributes from their superclass. 
        3. Instances inherit attributes from all accessible classes. 
            Each instance gets names from the class it is generated from, ae well as all of that class's superclass. 
            When looking for a name, Python checks the instance, then its class, the all superclass. 
        4. Each object.attribute reference invokes a new, independent search. 
        5. Logic changes are made by subclassing, not by changing suoerclass. 


''' 

# Second Example 
class SecondClass(FirstClass): 
    def display(self): 
        # By definning attribute with same name in FirstClass, SecondClass' display overrides the attribute in FirstClass. 
        # Searching attributes stops by first appearance of the name that it finds. 
        print("Current value = '%s'"%(self.data)) 

z = SecondClass() 
z.setdata("Inheritance of the attribute setdata.") # Inherit the attribute setdata from superclass FirstClass. 
z.display() # Override the attribute in FirstClass. 
x.display() # x is still odd value. 
''' 
    Class are attributes in Modules

        $ import modulename                             # or from modulename import FirstClass 
        $ class SecondClass( modulename.FirstClass ): 
        $   def function_name(self): 
        $       .... 
        
        [Note] 
            1. Where modulname and class name can be the same. i.e. abc.abc(),
            2. class name should begin with an uppercase letter conventionally. i.e. abc.Abc() 

''' 

# III. Operator overloading 
''' 
    Classes can intercept Python operators. 
        Operator overloading is that let the objects coded with classes intercept and respond to operations that work on build-in type: 
            addition, slicing, printing, qualification and so on. 
        Operator overloading lets objects be more tightly integrated with Python's object model and makes classes like build-in. 

        [Note] 
        1. Methods named with double underscores are special, i.e. __X__ 
            This spacial method is implemented on operator overloading. 
            Python classes define a fixed and unchangeable mapping from each of these operations. 
        2. Such methods are called automatically when instances appear in built-in operation. 
            If an instance object inherits an __add__ method, that method is called whenever the object appears in a + expression. 
        3. Classes may override most built-in type operation. 
        4. If a class doesn't define or inherit an operator overloading methods, 
            it just means that the corresponding operation is not supported for the class's instances. 
                i.e. If there is no __add__, + expression raise exception. 
        
        [Note] 
        __init__ method, which is known as the constructor method and used to initiailize object's state, which is optional. 
        
''' 
# Third Example with operator overloading.  
class ThirdClass( SecondClass ): 
    def __init__(self,value): 
        self.data = value 

    def __add__(self, other): # Called if + expression appears. 
        #return self.data+other # Just return a objects of self.data+other  
        return ThirdClass(self.data+other) # Return an instance of ThirdClass. 

    def __str__(self): # Called if print() appears. 
        return "[ThirdClass: %s]"%self.data 

    def mul(self,other): 
        self.data *= other 


a = ThirdClass('abc') 
a.display() # Inherit from FirstClass, because .display appears first at FirstClass. 
print(a) # Call the __str__ method.  
b = a+'xyz' 
''' 
    .__add__(self,other):
              ^     ^
            　|     | 
              |     |
              a  + 'xyz' 

    return ThirdClass( self.data + other ) 
                          ^         ^   
                          |         | 
                          |         |   
                        'abc'      'xyz' -----> Initialize another instance of ThirdClass with 'abcxyz' 

''' 
b.display() # __add__ makes a new instance that hass all ThirdClass attributes. 
print(b) 

a.mul(3) 
print(a) 


# Other example 
class rec: 
    pass # An empty namespace 


rec.name = 'Bob' 
rec.age = 40 
print(rec.name) 
''' 
    Above works even though there is no instance of the class yet. 
    Classes are objects in their own right, even without instances. 
''' 

x = rec() 
y = rec()
print( x.name, y.name ) # Because of add new attribute above. 

x.name = 'Sue' 
print( x.name, y.name ) # x is another namespace.  
''' 
    Actually, the attributes of a namespace objects are usually implemented as dictionary. 
''' 

