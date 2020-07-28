
from collections import Counter
import re
from wordcloud import WordCloud, STOPWORDS
from os import path
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

from operator import itemgetter


d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

class SoftwareCareerAnalysis:

    def __init__(self, word_rank):
        self.word_rank = word_rank

    def phonics_word_rank(self):

        # word_rank_csv = pd.read_csv (r'/Users/hannahroach/Desktop/software_career_analysis/software_keyword_visualization/word-rank.txt', header = None)
        # word_rank_csv.to_csv (r'/Users/hannahroach/Desktop/software_career_analysis/software_keyword_visualization/word-rank.csv', index=None)
        
        word_rank_df = pd.read_csv('/Users/hannahroach/Desktop/software_career_analysis/software_keyword_visualization/word-rank.csv')     
        word_rank_df[1] = word_rank_df.reset_index().index
        # print(word_rank_df)
        word_rank_df_sorted = word_rank_df.sort_index(axis=0, ascending=True)
        word_rank_df_sorted = word_rank_df_sorted.dropna(how='any').values.tolist()
        # word_rank_df_sorted.columns = ["word","cnt"]

        # max_frequency = max(word_rank_df_sorted["cnt"])
        # word_rank_df_sorted["freq"] = (max_frequency-word_rank_df_sorted["cnt"])/max_frequency
        # word_rank_df_sorted = word_rank_df_sorted[["word","freq"]]
        # word_rank_df_sorted_list = word_rank_df_sorted.values.tolist()
        # print(word_rank_df_sorted_list)
        new_list = []
        for x, y in word_rank_df_sorted:
            new_list.append((x,y))

        generate_wordcloud(new_list, "figures/word_rank_cloud.png")
    


def generate_wordcloud(words, name):
    """https://blog.goodaudience.com/how-to-generate-a-word-cloud-of-any-shape-in-python-7bce27a55f6e
    https://amueller.github.io/word_cloud/auto_examples/frequency.html
    https://pngtree.com/so/aircraft-carrier

    """
    # text = str(words[0])

    WordCloud(
        width=850, height=550,
        background_color='black',
        max_words = 2000,
        repeat = True,
        stopwords=STOPWORDS,
        min_font_size=1,
    ).generate_from_frequencies(words, is_list=True).to_file(path.join(d,name))


if __name__ == "__main__":
    """"""

    word_rank = "/Users/hannahroach/Desktop/software_career_analysis/software_keyword_visualization/word-rank1.txt"
    SoftwareCareerAnalysis(word_rank).phonics_word_rank()
