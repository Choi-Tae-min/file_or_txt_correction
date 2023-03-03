import os

# set the number of digits you want to use for the new filename
num_digits = 5

# set the file extension of the files you want to rename
file_ext = '.png'
directory_path ="C:/Users/user/monodepth2_remake/data/ep0/color"
# get the list of files in the directory
files = os.listdir(directory_path)
# filter out files that do not have the specified file extension
files = [filename for filename in files if filename.endswith(file_ext)]

# sort the files alphabetically (assuming the filenames are in the format "image_xxxx.png")
files.sort()
i=0
print(files)
# loop over the files and rename them
for i, filename in enumerate(files):
    # get the file extension (assuming it's always ".png")
    extension = os.path.splitext(filename)[1]
    
    # create the new filename with leading zeros
    new_filename = "img_{:0{}}{}".format(i, num_digits, extension)
    
    # rename the file
    os.rename(filename, new_filename)