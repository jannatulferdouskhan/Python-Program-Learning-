# a=open("file.txt")
# value=a.readlines()
# print(value,type(value))
# a.close()

# line1=a.readline()
# print(line1,type(line1))
# line2=a.readline()
# print(line2)
# line3=a.readline()
# print(line3)
# line4=a.readline()
# print(line4)
# line5=a.readline()
# print(line5)
# print(line5=="")


# a=open("file.txt")
# line= a.readline()
# while (line != ""):
#           print(line)
#           line=a.readline
# a.close()     
a = open("file.txt")
line = a.readline()

while line != "":
      print(line,end="")  # end="" দিলে অতিরিক্ত newline আসবে না
      line = a.readline()
a.close()      
