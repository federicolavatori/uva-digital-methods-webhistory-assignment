import os
import cv2
import re
import numpy as np
def resize_image(input_path, output_path, width, height):
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # List all files in the input directory
    for filename in os.listdir(input_path):
        if filename.endswith('.png'):
            input_file_path = os.path.join(input_path, filename)
            output_file_path = os.path.join(output_path, filename)

            # Read the image
            image = cv2.imread(input_file_path)

            # Resize the image
            resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

            # Save the resized image
            cv2.imwrite(output_file_path, resized_image)

def extract_and_convert_numbers(s):
    # Use regular expression to find leading numbers
    match = re.match(r'^\d+', s)

    if match:
        leading_numbers = match.group()
        # Convert to integer to remove leading zeros
        return int(leading_numbers)
    else:
        return None

def read_images_in_directory(directory_path):
    # Initialize empty list
    images_dict = {}

    # List all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):  # Adjust extensions as needed
            full_path = os.path.join(directory_path, filename)

            # Read the image using cv2.imread
            image = cv2.imread(full_path)

            # Create a custom key using regular expression
            key = extract_and_convert_numbers(filename)

            # Store the image in the dictionary and in the list
            images_dict[key] = image

    # Sort the dictionary based on keys
    sorted_dict = dict(sorted(images_dict.items()))

    return sorted_dict

def rmse(img1, img2):
    return np.sqrt(((img1 - img2) ** 2).mean())