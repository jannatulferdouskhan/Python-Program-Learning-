with open("this.txt","r") as f :
     content1=f.read()
with open("file.txt","r") as m :
     content2=m.read()

if content1==content2 : 
     print("The files are identical")
else:
     print("The files are not identical")     