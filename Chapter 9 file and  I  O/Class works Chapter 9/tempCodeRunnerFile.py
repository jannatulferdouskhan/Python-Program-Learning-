import os

folder = "tables"

# যদি ফোল্ডার থাকে
if os.path.exists(folder):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        if os.path.isfile(file_path) and file_name.endswith(".txt"):
            os.remove(file_path)
            print(f"Deleted: {file_name}")
else:
    print("Folder does not exist.")