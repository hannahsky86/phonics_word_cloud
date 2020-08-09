
from collections import Counter
import re
from wordcloud import WordCloud, STOPWORDS
from os import path
import os
import matplotlib.colors as clrs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
from PIL import Image
from operator import itemgetter
import csv
import program_config as config
from PIL import Image, ImageDraw, ImageFont

import random

# d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

class SoftwareCareerAnalysis:

    # def __init__(self):


    def phonics_word_rank(self):
     
        words_df = pd.read_csv(config.text_input)     
        words_df.columns = ['word']
        words_df['len'] = words_df['word'].apply(len)
        words_df_sorted=words_df.sort_values(by=['len']).dropna(how='any').values.tolist()
        
        new_word_list = []
        for x,y in words_df_sorted:
            if config.phonics_sound in str(x) and len(x)>2:
                new_word_list.append((x,y))

        save_to_csv(self, new_word_list)

        generate_wordcloud(self, new_word_list)
    
def save_to_csv(self, lst):

    with open(config.csv_output, 'w') as f:
        writer = csv.writer(f , lineterminator='\n')
        for tup in lst:
            writer.writerow(tup)




def generate_wordcloud(self, words):

    def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
        return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

    W, H = (720,1080)
    msg = "ph"
    im = Image.new("RGBA",(W,H),"black")
    draw = ImageDraw.Draw(im)
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 400)
    w, h = draw.textsize(msg, font=fnt)
    draw.text(((W-w)/2,(H-h)/2), msg, fill="white", font=fnt)
    im.save(config.mask_image, "PNG")
    mask = np.array(Image.open(config.mask_image))


    from matplotlib.colors import LinearSegmentedColormap
    colors = ["#003366","#ffffcc"]
    cmap = LinearSegmentedColormap.from_list("mycmap", colors)

    WordCloud(
        width=W, height=H,
        background_color= config.background_color,
        max_words = 2000,
        repeat = True,
        stopwords=STOPWORDS,
        min_font_size=12,
        max_font_size=100,
        mask=mask, 
        margin=5,
       colormap='CMRmap'
    ).generate_from_frequencies(words, is_list=True).to_file(config.cloud_image)

    first_image = Image.open(config.white_image).resize((720,1080))
    second_image = Image.open(config.cloud_image)
    mask = Image.open(config.mask_image).convert('L')
    im = Image.composite(first_image, second_image, mask)
    im = im.resize((7200,10800))
    im.save(config.composite_image, "png", dpi=(900,900))


if __name__ == "__main__":
    """"""

    SoftwareCareerAnalysis().phonics_word_rank()
