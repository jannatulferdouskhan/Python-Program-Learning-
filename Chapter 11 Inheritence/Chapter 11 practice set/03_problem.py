class Employee():
    salary=200
    increment=20
    @property
    def salary_after_increment(self):
        return (self.salary + (self.salary * (self.increment/100)))
    @salary_after_increment.setter
    def salary_after_increment(self,salary):
        self.increment=((salary/self.salary)-1)*100

a=Employee()
salary=240
print(a.salary_after_increment)
b=a.increment
print(b)       
