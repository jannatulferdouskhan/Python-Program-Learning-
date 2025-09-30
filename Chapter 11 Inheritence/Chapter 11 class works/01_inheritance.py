class Animal():
       def __init__(self,name):
           self.name=name
       def speak(self):
           print(f"{self.name} makes sound ")

                       
class Dog(Animal):
       def speak(self):
            print(f"{self.name} says woof !")
class Cat(Animal):
       def speak(self):
            print(f"{self.name} sayes Moew !") 
d=Dog("Tommy")

d.speak()


c=Cat("Mini")
c.speak()             
