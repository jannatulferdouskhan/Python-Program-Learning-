def convert(c):
     f=((c/100)*180)+32
     return f
c=float(input("Enter the value of Temperature in Celcious: "))
Temp=convert(c)
print(f"The temeperature in farenhite scale is : {Temp}")