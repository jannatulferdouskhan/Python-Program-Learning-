class Employee: 
     name="Ark"
     salary=1200
     language="Python"
     def boss(self): #self parameter , class er kichu method a use korte hole "self" use korte hoy 
          print(f"Tor salary holo {self.salary}")
     @staticmethod    #static method ,jokhon class er kichu method a proyojon hoy na tokhon use korte hoy 
     def greet():
          print("Good Morning")


baan=Employee()
# baan.name="Alu"
# print(Employee.salary)
# print(Employee.name)
baan.boss()
baan.greet()