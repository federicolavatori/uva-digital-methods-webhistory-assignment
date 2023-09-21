from utils import *

# Set input and output paths
inputPath = "../screen_linkedin_month_clean/"
outputPath = "../screen_linkedin_month_resize/"
width = 800  # Set the desired width
height = 600  # Set the desired height

# Call the function to resize images and save them to the output directory
resize_image(inputPath, outputPath, width, height)
