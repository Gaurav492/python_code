import os
from PIL import Image

# Set the path to the folder containing the images
folder_path = 'D:/Jimit/posts/wall'  # Modify this with your folder path

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Initialize a counter for renaming
counter = 1

# Iterate through all files in the folder
for file_name in files:
    # Check if the file is an image file (you may want to add more checks here if needed)
    if file_name.endswith('.jpg') or file_name.endswith('.png') or file_name.endswith('.jpeg'):
        # Construct the new file name
        new_file_name = str(counter) + '.webp'
        
        # Construct the full path for the old and new file names
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_file_name)
        
        # Convert the image to WebP format
        with Image.open(old_path) as img:
            img.save(new_path, 'WEBP')
        
        # Increment the counter
        counter += 1
        
        # Remove the old image file
        os.remove(old_path)

print("Conversion to WebP format completed.")