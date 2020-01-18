# modules
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

# Text Preprocessing
class Lite:

    # Text Path
    def __init__(self, txt_path):
        
        with open(txt_path, mode='r') as text:
            
            self.lines = text.read().splitlines()
            
            self.text = j = ' '.join(self.lines)

    # return lines [list]
    def get_lines(self):

        return self.lines

    # returns the whole text [str]
    def get_text(self):

        return self.text

    # get tokens [list]
    def get_tokens(self):
        text = re.sub('[-,:;?!".“”_]+', " ", self.text)
        # get tokens
        return text.lower().split()
        
    # get sentences [list]        
    def get_sentences(self):
        #oh gosh
        text = self.text.lower().replace('mr.', 'mr').replace('mrs.', 'mrs').replace('_', ' ')
        #get sentences
        return re.split('(?<=[.";]) +', text)

    # get tokens preproc. w nltk stopword and stemming
    # add_stopwords [add stopwords list]
    # stemming False -> Lemmatization
    # stemming True -> Stemming
    def get_preproc_tokens(self, add_stopwords = [], stemming = False):
        # stopwords
        en_stops = set(stopwords.words('english'))

        for word in add_stopwords:
            en_stops.add(word)

        sw = []
        # stop words
        for word in self.get_tokens(): 
            if word not in en_stops:
                sw.append(word)    

        self.preproc_tokens = []

        # Porter stemming
        if stemming == True:
            porter_stemmer = PorterStemmer()

            for s_porter in sw:
                self.preproc_tokens.append(porter_stemmer.stem(s_porter))
            
            return self.preproc_tokens
        # Lemmatization
        else:
            lemmatizer = WordNetLemmatizer()
            for lemm in sw:
                self.preproc_tokens.append(lemmatizer.lemmatize(lemm))

            return self.preproc_tokens

    # get pos tag [list]
    # tokens [no. tokens]
    # Ex: meta = Lite('metamorphosis.txt')
    # print(meta.get_pos_tag(tokens = meta.get_tokens()[:10]))
    def get_pos_tag(self, tokens = []):
        
        if len(tokens) < 1:
            tags = nltk.pos_tag(self.get_tokens(), tagset='universal')
        else:
            tags = nltk.pos_tag(tokens, tagset='universal')
        
        pos_tags = []

        for x in tags:
            pos_tags.append([x[0], x[1]])

        return pos_tags

    # return occurrences [dict]
    # list_of_words [occurrences of word's list]
    # p_tokens bool (Preproc. or not)
    # words_num [number of words]
    def get_occurrences(self, list_of_words = [], p_tokens = True, words_num = 20):
        
        if p_tokens == True:
            tokens = self.get_preproc_tokens()
        else:
            tokens = self.get_tokens()

        if len(list_of_words) < 1:
            occurrences = Counter(tokens).most_common(int(words_num))
        else:
            occ = []
            for word in tokens:
                if word in list_of_words:
                    occ.append(word)
            occurrences = Counter(occ).most_common()
        
        dictionary = {}

        for x in occurrences:
            dictionary[x[0]] = x[1]
  
        return dictionary
    
  
    # sentiment analysis [list of tuple]
    # [('sentence', sentence),('positive', vs['pos']), ('negative', vs['neg']), ('neutral', vs['neu']), ('compound', vs['compound'])]
    # list_of_words [selected words]
    def get_sentiment_analysis(self, list_of_words = []):

        analyzer = SentimentIntensityAnalyzer()
        sentiments = {}
        sentences = self.get_sentences()
        words = []

        if len(list_of_words) < 1:
            for sentence in sentences:
                vs = analyzer.polarity_scores(sentence)
                sentiments[sentences.index(sentence)] = [('sentence', sentence),('positive', vs['pos']), ('negative', vs['neg']), ('neutral', vs['neu']), ('compound', vs['compound'])]
                
            return sentiments

        else:
            for sentence in sentences:
                for word in list_of_words:
                    if word in sentence:
                        words.append(sentence)
                        
            # remove duplicate
            rem = list(dict.fromkeys(words))     

            for sentence in rem:
                vs = analyzer.polarity_scores(sentence)
                sentiments[rem.index(sentence)] = [('sentence', sentence),('positive', vs['pos']), ('negative', vs['neg']), ('neutral', vs['neu']), ('compound', vs['compound'])]

        return sentiments

    # get_api_json
    def get_api_json(self, my_data, file_name):
        with open(file_name, 'w') as api_json:
            json.dump(my_data, api_json, indent = 4)

# Ereditarietà
class LiteDrawing(Lite):
    
    # get_pos_tag_draw
    # Ex.:
    # text = TextDrawing("metamorphosis.txt")
    # print(text.get_chunk_draw(tokens = text.get_tokens()[:20]))
    def get_pos_tag_draw(self, grammar ="NP: {<DT>?<JJ>*<NN>}", tokens = []):

        sentence = self.get_pos_tag(tokens)
        cp = nltk.RegexpParser(grammar)
        result = cp.parse(sentence)
        result.draw()

    # get_occurrences_draw
    # Ex:
    # draw = TextDrawing('metamorphosis.txt')
    # print(draw.get_occurrences_draw(list_of_words=['mother', 'father', 'sister', 'gregor']))
    def get_occurrences_draw(self, list_of_words = [], p_tokens = True, words_num = 20):
        x = []
        y = []

        if len(list_of_words) < 1:
            for key, value in self.get_occurrences(p_tokens = p_tokens, words_num = words_num).items():
                x.append(key)
                y.append(value)
        else:
            for key, value in self.get_occurrences(list_of_words = list_of_words, p_tokens = p_tokens).items():
                x.append(key)
                y.append(value)
        
        plt.plot(x, y, marker='x')

        plt.show()

    # get sentiment draw
    def get_sentiment_draw(self, list_of_words=[]):
        x = []
        y = []

        lw = self.get_sentiment_analysis(list_of_words)

        for key, value in lw.items():
            x.append(key)
            y.append(value[4][1])

        plt.plot(x, y, marker='x')

        plt.show()
