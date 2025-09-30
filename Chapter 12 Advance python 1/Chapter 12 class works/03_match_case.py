status=int(input("Enter the case: "))
def rok():
    match status:
         case 400:
              return 10
         case 300:
              return 20 
         case 200:
              return 30
         case _: 
              return "Hii"
a=rok()
print(a)         

