# Write a program to calculate the grade of a student from his marks from the 
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F
a=float(input("Enter the mark:  "))
if(a>100):
     print("Input a valid number please")
elif(a>=90):
     print("Your Grade is Ex")
elif(a>=80):
     print("Your Grade is A")    
elif(a>=70):
     print("Your Grade is B")  
elif(a>=60):
     print("Your Grade is c")
elif(a>=50):
     print("Your Grade is D")
else:
     print("Your Grade is F ")                   
