import os
from PIL import Image

# Set the directory containing the images
image_dir = "Data_path"

# Loop over all image files in the directory
for i in range(len(os.listdir(image_dir))):
    # Construct the file path for the current image
    image_path = os.path.join(image_dir, f"{i+1}.png")

    # Load the image
    img = Image.open(image_path)

    # Calculate the new height that is a multiple of 32
    new_height = (img.height // 32 + 1) * 32
    print(new_height)
    # Resize the image to the new height while maintaining the aspect ratio
    new_size = (img.width, new_height)
    resized_img = img.resize(new_size, resample=Image.BICUBIC)

    # Save the resized image with a new name
    new_image_path = os.path.join(image_dir, f"{i}.png")
    resized_img.save(new_image_path)
