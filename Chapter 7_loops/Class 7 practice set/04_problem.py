a=int(input("Enter the number: "))
b=1
c=0
while(b<=a):
      if ((a%b)==0):
          c += 1
      else: 
           pass    
      b +=1     
if c==2:
     print(f"{a} is a prime number") 
else:
     print(f"{a} is not a prime number")  
     