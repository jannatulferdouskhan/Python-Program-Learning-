with open("log.txt","r") as f:
     content=f.read()
     if "python" in content :
          print("Python is there")
     else:
          print("Python is not there")     