#  Write a program to print the following star pattern:
#  *
#  **
#  *** for n = 3

a=int(input("Enter the value: "))

for i in range(1,a+1):
     print("*" * i ,end="" )
     print("")