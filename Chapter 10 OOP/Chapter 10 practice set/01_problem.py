import pyttsx3 
engine=pyttsx3.init()
class Programer():
     company="Microsoft"
     def __init__(self,name,salary,pin):
          self.name=name
          self.salary=salary
          self.pin=pin

p=Programer("Fagun",120000,24434)
print(p.name,p.salary,p.pin,p.company)
p=Programer("Maruf",150000,4578)
# l=p.name,p.salary,p.pin,p.company
engine.say(f"{p.name,p.salary,p.pin,p.company}")
engine.runAndWait()          