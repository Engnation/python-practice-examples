from asyncore import write
import os

# read file
f = open("test_file.txt","r")
content = f.readline()
f.close()

# make folder if it doesn't already exist
folder_name = "subfolder"
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
#do whatever and send to this folder:  os.path.join(folder_name)
destination = os.path.join(folder_name, f"destination.txt")
file2 = open(destination,"w")
file2.write(content)
file2.close()
