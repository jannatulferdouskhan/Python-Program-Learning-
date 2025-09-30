def greatest(a,b,c):
     if (a>b and b>c):
          print(f"Number 1 {a} is the greatest number")
     elif(b>a and a>c):
          print(f"Number 2 {b} is the greatest number")
     else:
          print(f"Number 3 {c} is the greatest number") 

a=int(input("Enter the value of number1: "))
b=int(input("Enter the value of number2: "))
c=int(input("Enter the value of number3: "))

greatest(a,b,c)






