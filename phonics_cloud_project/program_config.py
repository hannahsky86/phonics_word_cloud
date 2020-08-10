from os import path
import os

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

phonics_sound = "ph"
background_color = "black"
colormap = "bone"

mask_image  = path.join(d,'mask_image/ph.JPEG')
white_image = path.join(d,'mask_image/white.JPEG')
cloud_image = path.join(d,'mask_image/cloud.JPEG')
composite_image = path.join(d,"figures/phonics_cloud/CMRmap/ph.JPEG")


# Input/Output CSV files
text_input = path.join(d,'csv_input/text_files/ph(sample words- photo, dolphin).txt')

# csv_input = path.join(d,'csv_input/sightwords.csv') 
# csv_output = path.join(d,'csv_output/ph.csv')
csv_input = path.join(d,'csv_input/ph_words.csv') 
csv_output = path.join(d,'csv_output/ph_words.csv')


text_file_dir = path.join(d,'csv_input/text_files/') 
