import os
from PIL import Image
import time
import random
import string

# Start the timer
start_time = time.time()

# Function to generate a random label for recognizing new files
def generate_random_label():
    # Define the characters that can be used in the random string
    characters = string.ascii_uppercase + string.digits

    # Generate a random string with six characters
    random_string = ''.join(random.choice(characters) for _ in range(6))

    return random_string

# Function to parse image files and save channels in png files
def image_channel_split(folder_path, procedure_label='', include_subfolders=True):

    # Get file list
    image_files = []
    for root, dirs, files in os.walk(folder_path):
        if not include_subfolders:
            # Exclude subfolders
            dirs.clear()
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                image_files.append(os.path.join(root, file))

    for image_file in image_files:

        # Open image file
        im = Image.open(image_file)

        # Save the color map without the alpha channel
        im_rgb = im.convert('RGB')
        im_rgb.save(os.path.join(os.path.splitext(image_file)[0] + '_ColorMap_' + procedure_label + '.png'))

        # Extract and save R, G, B channels
        im_red = Image.new('RGBA', im.size, (255, 255, 255, 255))
        im_red.putalpha(im.split()[0])
        im_red.save(os.path.join(os.path.splitext(image_file)[0] + '_RedChannel_' + procedure_label + '.png'))
        im_green = Image.new('RGBA', im.size, (255, 255, 255, 255))
        im_green.putalpha(im.split()[1])
        im_green.save(os.path.join(os.path.splitext(image_file)[0] + '_GreenChannel_' + procedure_label + '.png'))
        im_blue = Image.new('RGBA', im.size, (255, 255, 255, 255))
        im_blue.putalpha(im.split()[2])
        im_blue.save(os.path.join(os.path.splitext(image_file)[0] + '_BlueChannel_' + procedure_label + '.png'))

        # If the image has an alpha channel, create an alpha map
        if im.mode == 'RGBA':
            im_alpha = Image.new('RGBA', im.size, (255, 255, 255, 255))
            im_alpha.putalpha(im.split()[3])
            im_alpha.save(os.path.join(os.path.splitext(image_file)[0] + '_AlphaChannel_' + procedure_label + '.png'))

        print('Saved channels for ' + image_file)

# Call the function with the current folder path
label = generate_random_label()
image_channel_split('.', procedure_label = label, include_subfolders=True) # Set include_subfolders to False to exclude subfolders

# Stop the timer and display the elapsed time
elapsed_time = time.time() - start_time
print('Finished in {:.4f} seconds'.format(elapsed_time) + ' with label ' + label)