f= open("myfile.txt")
# line= f.read()
print(f.read())



#using with 
with open("file.txt") as a: 
     print(a.read()) 
# You don't have explictly close the file      