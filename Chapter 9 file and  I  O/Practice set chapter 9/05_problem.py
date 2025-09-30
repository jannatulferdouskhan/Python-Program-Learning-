wards=["khela","puki","chut","nosto"]
with open("file.txt","r") as f:
     content=f.read()
for ward in wards:     
     content=content.replace(ward,"#"* len(ward))

with open("file.txt","w") as f:
     f.write(content) 
