i=float(input("Enter a number of your table: "))

table=[i*n for n in range(1,11)]

with open("table.txt","a") as f:
    f.write(f"Table of{i} is: {table}\n")