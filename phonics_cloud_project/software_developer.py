
from collections import Counter
import re
from wordcloud import WordCloud, STOPWORDS
from os import path
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
from PIL import Image
from operator import itemgetter
import csv


d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

class SoftwareCareerAnalysis:

    def __init__(self):
        
        self.phonics_sound = "ph"
        self.background_color = "black"
        self.mask_image = path.join(d,'mask_image/ph_inv.png')
        self.save_image = path.join(d,"figures/phonics_cloud/white/ph_cloud.png")
        self.white_image = path.join(d,'mask_image/white.png')
        self.second_image = path.join(d,"figures/phonics_cloud/white/second_image9.png")
        
        self.csv_input = path.join(d,'csv_input/sightwords.csv') 
        self.csv_output = path.join(d,'csv_output/ph.csv')

    def phonics_word_rank(self):
        words_df = pd.read_csv(self.csv_input)
        words_df[1] = words_df.reset_index().index
        words_df_sorted = words_df.sort_index(axis=0, ascending=True).dropna(how='any').values.tolist()

        new_word_list = []
        for x,y in words_df_sorted:
            if self.phonics_sound in str(x) and len(x)>2:
                new_word_list.append((x,y))

        save_to_csv(self, new_word_list)

        generate_wordcloud(self, new_word_list)
    
def save_to_csv(self, lst):

    with open(self.csv_output, 'w') as f:
        writer = csv.writer(f , lineterminator='\n')
        for tup in lst:
            writer.writerow(tup)

def generate_wordcloud(self, words):
    """https://blog.goodaudience.com/how-to-generate-a-word-cloud-of-any-shape-in-python-7bce27a55f6e
    https://amueller.github.io/word_cloud/auto_examples/frequency.html
    https://pngtree.com/so/aircraft-carrier

    """
    phonics_image = np.array(Image.open(self.mask_image))

    WordCloud(
        width=850, height=550,
        background_color=self.background_color,
        max_words = 1000,
        repeat = True,
        stopwords=STOPWORDS,
        min_font_size=1,
        mask=phonics_image, 
        # colormap='bone'
        colormap = 'winter'
    ).generate_from_frequencies(words, is_list=True).to_file(self.save_image)


    first_image = Image.open(self.white_image)
    second_image = Image.open(self.save_image)
    # mask_image = Image.open(self.mask_image)

    mask = Image.open(self.mask_image).convert('L').resize(first_image.size)
    im = Image.composite(first_image, second_image, mask)
    
    # mask = Image.new("L", mask_image.size, "white")
    # im = Image.composite(second_image, first_image,  mask)
    # im = Image.blend(im1, im2, 0.5)

    # first_image.paste(second_image, box=(0,0), mask=second_image)
    # paste() modifies the first PIL.Image.Image
    im.save(self.second_image)


if __name__ == "__main__":
    """"""

    SoftwareCareerAnalysis().phonics_word_rank()
