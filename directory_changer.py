import os
import re

folder_path = "/path/to/folder"  # Replace with the path to your folder

# Create a regular expression to match folder names with the pattern "epX", where X is a number
folder_pattern = re.compile(r"^ep\d+$")

# Get the initial list of folder names in the folder_path directory
initial_folder_names = os.listdir(folder_path)

while True:
    # Get the updated list of folder names
    updated_folder_names = os.listdir(folder_path)

    # Find the difference between the initial list and the updated list
    diff = set(updated_folder_names) - set(initial_folder_names)

    # Check if any new folder names match the pattern
    for folder_name in diff:
        if folder_pattern.match(folder_name):
            print(f"Folder name changed to {folder_name}")

    # Update the initial list of folder names for the next iteration
    initial_folder_names = updated_folder_names