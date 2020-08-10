
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
from PIL import Image, ImageDraw, ImageFont, ImageFile
# import Image as imgs

import random

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

class SoftwareCareerAnalysis:

    # def __init__(self):


    def loop_through_text_files(self):

        directory = path.join(config.d,'csv_input/text_files/') 

        for filename in os.listdir(directory):
            prep_word_cloud(self,filename) 


def prep_word_cloud(self, filename):

    words_df = pd.read_csv(path.join(config.text_file_dir,filename) )     
    words_df.columns = ['word']
    words_df['len'] = words_df['word'].apply(len)
    words_df_sorted = words_df.sort_values(by=['len']).dropna(how='any').values.tolist()
    
    new_word_list = []
    for x,y in words_df_sorted:
        if len(x)>2:
            new_word_list.append((x,y))

    filename = filename.strip('picture noun ')
    filename = filename.strip('cvc medial ')
    phonics_sound = filename[1:filename[1:5].find("'")+1]

    save_to_csv(new_word_list, phonics_sound)

    generate_wordcloud(self, new_word_list, phonics_sound)
    
def save_to_csv(lst, phonics_sound):

    csv_output_filename = 'csv_output/'+str(phonics_sound)+'_words.csv'
    with open(path.join(config.d,csv_output_filename), 'w') as f:
        writer = csv.writer(f , lineterminator='\n')
        for tup in lst:
            writer.writerow(tup)

def generate_wordcloud(self, words, phonics_sound):

    W, H = (720,1080)
    msg = phonics_sound
    im = Image.new("CMYK",(W,H),"black")
    draw = ImageDraw.Draw(im)
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 400)
    w, h = draw.textsize(msg, font=fnt)
    draw.text(((W-w)/2,(H-h)/2), msg, fill="white", font=fnt)
    im.save(config.mask_image, "JPEG", quality=80, optimize=True, progressive=True)
    mask = np.array(Image.open(config.mask_image))

    wordcloud = WordCloud(
        width=720, height=1080,
        background_color= config.background_color,
        max_words = 200,
        repeat = True,
        stopwords=STOPWORDS,
        min_font_size=12,
        max_font_size=100,
        mask=mask, 
        margin=5,
       colormap='CMRmap'
    ).generate_from_frequencies(words, is_list=True).to_image().save(config.cloud_image, quality=100)

    # plt.figure( figsize=(24,36), facecolor='k')
    # plt.imshow(wordcloud)
    # plt.savefig(config.cloud_image, facecolor='k', bbox_inches='tight')

    # to_image().save(config.cloud_image, "JPEG", dpi=(900,900))

    first_image = Image.open(config.white_image)
    second_image = Image.open(config.cloud_image)
    mask = Image.open(config.mask_image).convert('L')
    im = Image.composite(first_image, wordcloud, mask)
    # .resize((7200,10800))
    image_output_filename = 'figures/phonics_cloud/CMRmap/'+str(phonics_sound)+'.jpg'
    im.save(path.join(d,image_output_filename), "JPEG", dpi=(900,900))


if __name__ == "__main__":
    """"""

    SoftwareCareerAnalysis().loop_through_text_files()

