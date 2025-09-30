a="wors"
if "k" in a :
     print("yes")
else:
     print("no")


with open("poem.txt") as a :
     a= a.read()
     if "twinkle" in a :
          print("Yes the ward is there")
     else:
          print("The ward is not there")     
import os

folder = "tables"


if os.path.exists(folder):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        if os.path.isfile(file_path) and file_name.endswith(".txt"):
            os.remove(file_path)
            print(f"Deleted: {file_name}")
else:
    print("Folder does not exist.")



wards=["khela","puki","chut","nosto"]
for ward in wards:
     print(ward)