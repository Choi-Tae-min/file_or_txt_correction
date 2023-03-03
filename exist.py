import os

path = 'C:\\Users\\user\\monodepth2_remake\\data\\ep4\\color\\image_-1.png'

if os.path.exists(path):
    print("File exists!")
else:
    print("File not found.")