try:
    a=float(input("Enter the value of a: "))
    b=float(input("Enter the value of b: "))
    print(a/b)
except ZeroDivisionError as p:
    print("Infinite")    