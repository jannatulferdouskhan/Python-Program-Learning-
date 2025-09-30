class Calculator():
     def __init__(self,n):
          self.n=n
     def square(self):
          print(f"The squre={self.n*self.n}")
     def cube(self):
          print(f"The cube={self.n*self.n*self.n}")
     def square_root(self):
          print(f"The squre_root={self.n**(1/2)}")
          
         
a=Calculator(4568)
a.square()
a.cube()
a.square_root()
          
            
                    

