from os import path
import os

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

phonics_sound = "ph"
background_color = "black"

mask_image = path.join(d,'mask_image/ph_inv.png')
white_image = path.join(d,'mask_image/white.png')
cloud_image = path.join(d,"figures/phonics_cloud/black/cloud.png")
composite_image = path.join(d,"figures/phonics_cloud/black/ph_wc.png")


# Input/Output CSV files
csv_input = path.join(d,'csv_input/sightwords.csv') 
csv_output = path.join(d,'csv_output/ph.csv')