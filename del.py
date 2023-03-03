import os

# Define path to input text file
input_file = "C:/Users/user/monodepth2_remake/splits/EndoMapper/val_files.txt"

# Define path to output text file
output_file = "D:/result/dense"

# Read in the input file
with open(input_file, "r") as f:
    input_lines = f.readlines()

# Replace all backslashes with forward slashes
output_lines = [line.replace("-dpt_next_vit_large_384", "") for line in input_lines]
#output_lines2 = [line.replace("(", "") for line in input_lines]
#output_lines3 = [line.replace(")", "") for line in input_lines]
# Write the modified lines to the output file
with open(output_file, "w") as f:
    f.writelines(output_lines)
   # f.writelines(output_lines2)
    #f.writelines(output_lines3)

# Print a confirmation message
print(f"Input file '{os.path.basename(input_file)}' was processed and saved as '{os.path.basename(output_file)}'.")