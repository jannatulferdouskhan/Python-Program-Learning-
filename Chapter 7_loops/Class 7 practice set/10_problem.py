# a=int(input("Enter the number: "))

# b=10
# while(b>=1):
#      print(f"{a}*{b}={a*b}")
#      b -=1




a = int(input("Enter the number: "))

for b in range(10, 0, -1):   # 10 থেকে শুরু করে 1 পর্যন্ত কমতে থাকবে
    print(f"{a} x {b} = {a*b}")