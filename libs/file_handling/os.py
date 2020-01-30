import os

#================================================================================================
file_extension = ".001"

for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith(file_extension):
            print(file)     # print the file name with extension
            print(os.path.join(root, file))     # print the filename with root path