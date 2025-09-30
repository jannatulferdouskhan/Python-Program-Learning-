l=[3,94,45,6]

# It is a general form 
index=0

for item in l:
    print(f"The index is {index} and value is {item} ")
    index += 1

#using enumerate functions 

print("New Process is going on")

for index,item in enumerate(l):
    print(f"The index is {index} and value is {item} ")
