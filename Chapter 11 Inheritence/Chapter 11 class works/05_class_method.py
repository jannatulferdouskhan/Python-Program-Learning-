class Employee():
     a=45
     @classmethod
     def al(cls):
          print(f"The value of class: {cls.a}")

e=Employee()
e.a=1
e.al()
