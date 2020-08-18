
from collections import Counter
import re
from wordcloud import WordCloud, STOPWORDS
from os import path
import os
import matplotlib.colors as clrs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
from operator import itemgetter
import csv
import program_config as config
import palettable
from PIL import Image, ImageDraw, ImageFont, ImageFile, ImageFilter

import random

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

class SoftwareCareerAnalysis:

    # def __init__(self):


    def loop_through_text_files(self):

        directory = path.join(config.d,'csv_input/text_files/todo/') 
        phonics_sound='al'
        directory_list = os.listdir(directory)
        for filename in sorted(directory_list):
            print(filename)
            file_path = path.join(directory, filename) 
            prep_word_cloud(self,file_path, phonics_sound) 


def prep_word_cloud(self, file_path, phonics_sound):

    words_df = pd.read_csv(file_path) 
    words_df.columns = ['word']
    words_df['len'] = words_df['word'].apply(len)
    words_df_sorted = words_df.sort_values(by=['len']).dropna(how='any').values.tolist()
    
    new_word_list = []
    for x,y in words_df_sorted:
        if len(x)>2:
            new_word_list.append((x,y))

    # filename = filename.strip('picture noun ')
    # phonics_sound = filename[1:filename.find("'")+1]

    save_to_csv(new_word_list, phonics_sound)

    generate_wordcloud(self, new_word_list, phonics_sound)
    
def save_to_csv(lst, phonics_sound):

    csv_output_filename = 'csv_output/'+str(phonics_sound)+'_words.csv'
    with open(path.join(config.d,csv_output_filename), 'w') as f:
        writer = csv.writer(f , lineterminator='\n')
        for tup in lst:
            writer.writerow(tup)

def generate_wordcloud(self, words, phonics_sound):

    W, H = (7200,10800)
    msg = phonics_sound
    im = Image.new("L",(W,H),0)
    draw = ImageDraw.Draw(im)
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 4000)
    w, h = draw.textsize(msg, font=fnt)
    draw.text(((W-w)/2,(H-h)/2), msg, fill="white", font=fnt)
    im.save(config.mask_image, dpi=(300,300))    
    mask = np.array(Image.open(config.mask_image))
    # cmap = palettable.scientific.sequential.Hawaii_20.mpl_colormap
    # cmap = palettable.colorbrewer.diverging.nipy_spectral.mpl_colormap
    # newcmap = cmap.from_list('newcmap',list(map(cmap,range(30,256))), N=256) 

    WordCloud(
        width=W, height=H,
        background_color= config.background_color,
        max_words = 2000,
        repeat = True,
        stopwords=STOPWORDS,
        min_font_size=120,
        max_font_size=1000,
        mask=mask, 
        margin=50,
       colormap='Spectral'
    ).generate_from_frequencies(words, is_list=True).to_image().save(config.cloud_image, dpi=(300,300))

    first_image = Image.open(config.white_image).resize((W,H))
    second_image = Image.open(config.cloud_image).resize((W,H))
    mask = Image.open(config.mask_image).convert('L').resize((W,H))
    final_image = Image.composite(first_image, second_image, mask)
    image_output_filename = 'figures/phonics_cloud/CMRmap/'+str(phonics_sound)+'.PNG'
    final_image.save(path.join(d,image_output_filename), dpi=(300,300))


if __name__ == "__main__":
    """"""

    SoftwareCareerAnalysis().loop_through_text_files()

