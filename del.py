import os

# Define path to input text file
input_file = "input_text_data_path"

# Define path to output text file
output_file = "output_text_data_path"

# Read in the input file
with open(input_file, "r") as f:
    input_lines = f.readlines()

# Replace all backslashes with forward slashes
output_lines = [line.replace("-dpt_next_vit_large_384", "") for line in input_lines]

# Write the modified lines to the output file
with open(output_file, "w") as f:
    f.writelines(output_lines)

# Print a confirmation message
print(f"Input file '{os.path.basename(input_file)}' was processed and saved as '{os.path.basename(output_file)}'.")
