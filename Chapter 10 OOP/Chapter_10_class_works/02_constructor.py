class Employee: 
     name="Ark"
     salary=1200
     language="Python"
     def __init__(self,name,salary,language):
          self.name=name
          self.salary=salary
          self.language=language
          print("I am here without calling ") #dunder method, ata autometecly call kore nijeke 
     
     def boss(self): #self parameter , class er kichu method a use korte hole "self" use korte hoy 
          print(f"Tor salary holo {self.salary}")
     @staticmethod    #static method ,jokhon class er kichu method a proyojon hoy na tokhon use korte hoy 
     def greet():
          print("Good Morning")


baan=Employee("Anna",1250,"C+") #parameter thik rakhte hobe 
# baan.name="Alu"
# print(Employee.salary)
# print(Employee.name)
# baan.boss()
# baan.greet()
# baan.greet()
# print(Employee())
print(baan.name,baan.salary,baan.language)