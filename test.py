from text_processing import Lite

meta = Lite('metamorphosis.txt')
print(meta.get_tokens()[:10]) # ['one', 'morning', 'when', 'gregor', 'samsa', 'woke', 'from', 'troubled', 'dreams', 'he']
print(meta.get_sentences()[:10])
#['one morning, when gregor samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin.'
# 'he lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections.'
# Etc. ]

print(meta.get_preproc_tokens()[:10]) # ['one', 'morning', 'gregor', 'samsa', 'woke', 'troubled', 'dream', 'found', 'transformed', 'bed']
print(meta.get_occurrences(list_of_words = ['father', 'sister', 'mother'])) #{'father': 96, 'sister': 96, 'mother': 83}
print(meta.get_sentiment_analysis(list_of_words = ['vermin']))
#{0: [('sentence', 'one morning, when gregor samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin.'), 
# ('positive', 0.107), ('negative', 0.258), ('neutral', 0.635), ('compound', -0.5859)]}

from text_processing import LiteDrawing

draw = LiteDrawing('metamorphosis.txt')

print(draw.get_sentiment_draw(list_of_words = ['father', 'mather']))
