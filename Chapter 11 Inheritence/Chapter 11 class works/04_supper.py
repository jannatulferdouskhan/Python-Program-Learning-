class Employee():
     a=1
     def __init__(self):
          print("Priniting constructor of Employee")
class Manager(Employee):
     def __init__(self):
          print("Printing constructor of Manager")
     b=2
class Programmer(Manager):
     def __init__(self):
          super().__init__() 
          print("Constructor of Programmer")
     c=3


# a=Employee() #print only Employe  
# b=Manager() # print only Manager 
c=Programmer() #Print manager & programmer constructor because Supper init 