import os
#if you want file exist, use this
path = 'data_path'

if os.path.exists(path):
    print("File exists!")
else:
    print("File not found.")
