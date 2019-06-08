import pandas as pd
import numpy as py
import string
import wordcloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from stop_words import get_stop_words

file=pd.read_csv('Dice_US_jobs_utf81.csv',error_bad_lines=False)
print(file.columns)

type(string.punctuation)
temp='Microsoft Dynamics AX, Project Manager'
temp=temp.translate(str.maketrans('', '', string.punctuation))
temp.split()

word_freq={}
for job in file['job_title']:
    try:
        job=job.translate(str.maketrans('', '', string.punctuation))
        words=job.split()
        for word in words:
            if word in word_freq:
                word_freq[word]=word_freq[word]+1
            else:
                word_freq[word]=1
    except:
        pass

most_freq=sorted(word_freq.items(),key=lambda x: x[1],reverse=True)[0:40]
most_freq=dict(most_freq)
print(dict(most_freq))

wc = WordCloud(background_color='white',
               width=4000,
               height=3200,
               ).generate_from_frequencies(most_freq)
wc.to_file('jobcloud.png') 
plt.imshow(wc)  
plt.axis('off') 
plt.show() 
