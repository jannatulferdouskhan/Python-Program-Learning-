a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
if b==0 :
    raise ZeroDivisionError("You can not Enter zero ")
else:
    print(f"The Division of Two number is: {a/b}")