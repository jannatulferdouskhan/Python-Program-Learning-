with open("log.txt","r") as f:
     lines=f.readlines()
     
     
lineno = 1
for line in lines :     
     if "python" in line :
          print(f"Python is there and Line no is: {lineno}")
          break 
     lineno += 1
          
else:
     print("Python is not there")  