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
# set destination file in subdirectory 
destination = os.path.join(folder_name, f"destination.txt")
# write to subdirectory
file2 = open(destination,"w")
file2.write(content)
file2.close()
