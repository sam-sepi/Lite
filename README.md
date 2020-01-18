# Lite
Python library for new forms of literary criticism

# Getting Started

git clone https://github.com/sam-sepi/Lite.git

```python
from text_processing import Lite

```
# Prerequisites

Dependencies:

```python
import string
import re
import json
# https://www.nltk.org/
import nltk
from nltk.corpus import stopwords # stopwords
from nltk.stem.porter import PorterStemmer # porter stemming
from nltk.stem import WordNetLemmatizer
# collections
from collections import Counter
# Sentiment Analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# plot
import matplotlib.pyplot as plt
```

# API

Lite 

```python
lite = Lite('metamorphosis.txt') # INIT.

lite.get_lines() # get text lines
lite.get_text() # get text, no lines
lite.get_tokens() # get tokens
lite.get_sentences() # get sentences
# get preproc. tokens, without sw, after lemmatizz. or stemming
lite.get_preproc_tokens(self, add_stopwords = [], stemming = False)
lite.get_pos_tag(tokens = []) # get tags of tokens
lite.get_occurrences(list_of_words = [], p_tokens = True, words_num = 20) # return occurrences of a word 
lite.get_sentiment_analysis(list_of_words = []) # get vader sa of a text or a list of words
lite.get_api_json(my_data, file_name) # write a json file

```

LiteDrawing
```python
draw = LiteDrawing('metamorphosis.txt') # INIT.
draw.get_occurrences_draw(list_of_words = [], p_tokens = True, words_num = 20) # draw occurr. graph
draw.get_pos_tag_draw(grammar ="NP: {<DT>?<JJ>*<NN>}", tokens = []) # draw tags posit.
draw.get_sentiment_draw(list_of_words=[]) # draw vader sa
```

# Running the tests

```python
from text_processing import Lite

meta = Lite('metamorphosis.txt') # INIT.
print(meta.get_tokens()[:10]) 
# print: ['one', 'morning', 'when', 'gregor', 'samsa', 'woke', 'from', 'troubled', 'dreams', 'he']

draw = LiteDrawing('metamorphosis.txt')

print(draw.get_sentiment_draw(list_of_words = ['father', 'mather']))

```
View file test.py

# Authors

Sam Sepi

# License

This project is licensed under the MIT License - see the LICENSE.md file for details

