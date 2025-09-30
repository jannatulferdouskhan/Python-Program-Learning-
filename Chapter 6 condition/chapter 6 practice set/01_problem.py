a=int(input("Enter the number1: "))
b=int(input("Enter the number2: "))
c=int(input("Enter the number3: "))
e=int(input("Enter the number4: "))
if(a>b and a>c and  a>e):
     print(a,"is the largest number")
elif(b>a and b>c and b>e):
     print(b,"is the largest number")
elif(c>a and a>b and c>e):
     print(c,"is the largest number")
elif(e>a and e>b and e>c):
     print(e,"is the largest number")          