from utils import *
import matplotlib.pyplot as plt
from image_similarity_measures.quality_metrics import *

# Provide the path to the directory containing images
pathToDirectory = "../screen_linkedin_month_resize/"

# Call the function to read images and store them in a dictionary
images_dict = read_images_in_directory(pathToDirectory)

print(images_dict.keys())

# Create a list of sorted dictionary keys
images = list(images_dict.values())

# Initialize a list to store the RMSE values
rmse_values = []

for i in range(len(images) - 1):
    rmse_value = uiq(images[i], images[i + 1])
    rmse_values.append(rmse_value)

print(rmse_values)
# Create a line plot
plt.plot(rmse_values)
plt.show()
