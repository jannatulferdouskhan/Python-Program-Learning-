class Employee():
     a=1
class Manager(Employee):
     b=2
class Programmer(Manager):
     c=3
m=Employee()

print(m.a)
#shows error because b & c not in class Employee
# print(m.b)
# print(m.c)
n=Manager()
print(n.a,n.b)
#Error because c not in manager 
# print(n.c)
o=Programmer()
print(o.a,o.b,o.c)