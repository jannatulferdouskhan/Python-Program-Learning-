ward="khela"
with open("file.txt","r") as f:
     content=f.read()
content_new=content.replace("khela","#####")

with open("file.txt","w") as f:
     f.write(content_new) 
