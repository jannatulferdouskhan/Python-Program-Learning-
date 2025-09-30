def pattrn(n):
     if(n==0):
         return
     
     print("*" * n)
     pattrn(n-1)
n=int(input("Enter the value of n: "))
pattrn(n)     