import os
directory="lab6"
file_name="files.p"
file_path=os.path.join(directory, file_name)
if os.path.exists(file_path) and os.path.isfile(file_path):
    print("file jok dne")
else:
    print("file bar exists")