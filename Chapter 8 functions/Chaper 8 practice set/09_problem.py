def table(n,p):
     
     if(p==0):
          return 0
     table(n,p-1)
     print(f"{n}*{p}={n*p}")
      

   
p=10 
n=int(input("Enter the number: "))
table(n,p)
