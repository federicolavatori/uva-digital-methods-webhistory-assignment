from utils import *
import matplotlib.pyplot as plt
from image_similarity_measures.quality_metrics import *

# Provide the path to the directory containing images
pathToDirectory = "../screen_linkedin_month_resize/"

# Call the function to read images and store them in a dictionary
images_dict = read_images_in_directory(pathToDirectory)

# Create a list of sorted dictionary keys
images = list(images_dict.values())

# Initialize a list to store the RMSE values
values = []

for i in range(len(images) - 1):
    value = ssim(images[i], images[i + 1])
    values.append(value)


# Create a line plot
plt.plot(values)
plt.show()
