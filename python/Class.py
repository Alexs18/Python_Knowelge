
#this is a normal class

class MyClass:
    #we need a self is something like this is javascript
    def HelloWorld(self):
        print('hello world...!')

#We can instance this class:

Intance1 = MyClass()
Intance1.HelloWorld()

#this is a class with constructor
class MyfirstClass:
    #this is the constuctor
    def __init__(self, age, name):
        self.age = age
        self.name = name
        
    def sayMyName(self):
        print(self.name)
        
    def SayMyAge(self):
        print(self.age)


instancia = MyfirstClass(26, 'Alex')
instancia.sayMyName()
instancia.SayMyAge()

edadinstancie = instancia.age
print(edadinstancie)

#We can create a new atribute with a amy value

instancia.profetion = 'developer'

print(instancia.profetion)