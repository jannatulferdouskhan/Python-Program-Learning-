class Employee():
     a=45
     @classmethod
     def al(cls):
          print(f"The value of class: {cls.a}")
     @property 
     def name(self):
          return f"{self.lname}{self.fname}"
     @name.setter
     def name(self, value):
             self.fname= value.split(" ")[0] 
             self.lname= value.split(" ")[1] 
            
          
e=Employee()
e.name="Amar Sotto"
print(e.fname,e.lname)


