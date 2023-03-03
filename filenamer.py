import os

# remove whitespace but you edit your filename too
def remove_whitespace(filename):
    return filename.replace("_", "_")

#if you want num_digit filename ex)00000.jpg you use this.
num_digits = 10


def rename_files(directory):
    i=0 #if you want start 1 or another num you change the number.
    for filename in os.listdir(directory):
        new_filename = '{:0{}}.jpg'.format(i, num_digits)# you do not edit num_digit, delete num_digit.
                        #remove_whitespace(filename) if you want to delete specific letter or sentence
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        i+=1
        
# directory_path
directory_path ="data_path"

# rename all of files with this format
rename_files(directory_path)
