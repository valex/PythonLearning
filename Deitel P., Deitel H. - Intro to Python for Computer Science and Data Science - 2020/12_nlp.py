from textblob import TextBlob
from textblob import Word
from textblob.sentiments import NaiveBayesAnalyzer
from pathlib import Path
import nltk
from nltk.corpus import stopwords
from operator import itemgetter
import pandas as pd
import matplotlib.pyplot as plt
import imageio
from wordcloud import WordCloud
from textatistic import Textatistic
import spacy


# ----------------------------------------------------
# Similarity Detection
# ----------------------------------------------------

nlp = spacy.load('en_core_web_sm')

document1 = nlp(Path('RomeoAndJuliet.txt').read_text())

document2 = nlp(Path('EdwardTheSecond.txt').read_text())

# Comparing the Books’ Similarity 
print(document1.similarity(document2))
# 0.9404091194177555

# ----------------------------------------------------
# Named Entity Recognition with spaCy
# ----------------------------------------------------
# nlp = spacy.load('en_core_web_sm')

# nlp_ru = spacy.load('ru_core_news_sm')

# # Creating a spaCy Doc
# document = nlp('In 1994, Tim Berners-Lee founded the ' + 
#     'World Wide Web Consortium (W3C), devoted to ' +
#     'developing web technologies')
    
# # Getting the Named Entities
# for entity in document.ents:
#     print(f'{entity.text}: {entity.label_}')
# # 1994: DATE
# # Tim Berners-Lee: PERSON


# ----------------------------------------------------
# Readability Assessment with Textatistic
# ----------------------------------------------------
# text = Path('RomeoAndJuliet.txt').read_text()

# readability = Textatistic(text)

# print( readability.dict() )
# # {'char_count': 115142, 
# # 'word_count': 26120, 
# # 'sent_count': 3218, num sentences
# # 'sybl_count': 30166, syllables
# # 'notdalechall_count': 5824, a count of the words that are not on Dale-Chall list
# # 'polysyblword_count': 549, with three or more syllables
# # 'flesch_score': 100.89182573236114, Flesch Reading Easy score
# # 'fleschkincaid_score': 1.2033940973296282, Flesch-Kincaid score
# # 'gunningfog_score': 4.087472172703886, Gunning Fog index value
# # 'smog_score': 5.488698373484701, The Simple Measure of Gobbledygook (SMOG)
# # 'dalechall_score': 7.559805967485725} Dale-Chall score

# ----------------------------------------------------
# Visualizing Word Clouds
# https://matplotlib.org/stable/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py
# ----------------------------------------------------
# text = Path('RomeoAndJuliet.txt').read_text()

# mask_image = imageio.imread('mask_heart.png')

# # https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html
# wordcloud = WordCloud(colormap='prism', mask=mask_image, background_color='white')

# wordcloud = wordcloud.generate(text)

# wordcloud = wordcloud.to_file('RomeoAndJulietHeart.png')

# mask_image2 = imageio.imread('mask_star.png')
# wordcloud2 = WordCloud(width=1000, height=1000,
#             colormap='prism', mask=mask_image2, background_color='white')

# wordcloud2 = wordcloud2.generate(text)
# wordcloud2 = wordcloud2.to_file('RomeoAndJulietStar.png')
# plt.imshow(wordcloud2)
# plt.show()


# ----------------------------------------------------
# Visualizing Word Frequencies
# ----------------------------------------------------
# blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())
# stop_words = stopwords.words('english')

# items = blob.word_counts.items()

# items = [item for item in items if item[0] not in stop_words]

# sorted_items = sorted( items, key=itemgetter(1), reverse=True )

# top20 = sorted_items[1:21]

# df = pd.DataFrame(top20, columns=['word', 'count'])

# print ( df )
# #         word  count
# # 0      romeo    315
# # 1       thou    278
# # 2     juliet    190
# # 3        thy    170
# # 4    capulet    163
# # 5      nurse    149
# # 6       love    148
# # 7       thee    138
# # 8       lady    117
# # 9      shall    110
# # 10     friar    105
# # 11      come     94
# # 12  mercutio     88
# # 13  lawrence     82
# # 14      good     80
# # 15  benvolio     79
# # 16    tybalt     79
# # 17     enter     75
# # 18        go     75
# # 19     night     73

# axes = df.plot.bar(x='word', y='count', legend=False, color=['C0', 'C1', 'C2', 'C3', 'C4','C5', 'C6', 'C7', 'C8', 'C9'])

# # plt.show()

# plt.gcf().tight_layout()
# plt.show()



# ----------------------------------------------------
# n-grams
# is a sequence of n text items, such as letters in words or words in sentence
# ----------------------------------------------------

# text = 'Today is a beautiful day. Tomorrow looks like bad weather.'

# blob = TextBlob(text)

# print( blob.ngrams() )
# # [WordList(['Today', 'is', 'a']), 
# # WordList(['is', 'a', 'beautiful']), 
# # WordList(['a', 'beautiful', 'day']), 
# # WordList(['beautiful', 'day', 'Tomorrow']), 
# # WordList(['day', 'Tomorrow', 'looks']), 
# # WordList(['Tomorrow', 'looks', 'like']), 
# # WordList(['looks', 'like', 'bad']), 
# # WordList(['like', 'bad', 'weather'])]

# print( blob.ngrams(n=5) )
# # [WordList(['Today', 'is', 'a', 'beautiful', 'day']), 
# # WordList(['is', 'a', 'beautiful', 'day', 'Tomorrow']), 
# # WordList(['a', 'beautiful', 'day', 'Tomorrow', 'looks']), 
# # WordList(['beautiful', 'day', 'Tomorrow', 'looks', 'like']), 
# # WordList(['day', 'Tomorrow', 'looks', 'like', 'bad']), 
# # WordList(['Tomorrow', 'looks', 'like', 'bad', 'weather'])]



# ----------------------------------------------------
# Deleting Stop Words
# ----------------------------------------------------

# nltk.download('stopwords')

# stops = stopwords.words('english')

# print(stops)
# # ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# # stops = stopwords.words('russian')
# # print(stops)
# # # ['и', 'в', 'во', 'не', 'что', 'он', 'на', 'я', 'с', 'со', 'как', 'а', 'то', 'все', 'она', 'так', 'его', 'но', 'да', 'ты', 'к', 'у', 'же', 'вы', 'за', 'бы', 'по', 'только', 'ее', 'мне', 'было', 'вот', 'от', 'меня', 'еще', 'нет', 'о', 'из', 'ему', 'теперь', 'когда', 'даже', 'ну', 'вдруг', 'ли', 'если', 'уже', 'или', 'ни', 'быть', 'был', 'него', 'до', 'вас', 'нибудь', 'опять', 'уж', 'вам', 'ведь', 'там', 'потом', 'себя', 'ничего', 'ей', 'может', 'они', 'тут', 'где', 'есть', 'надо', 'ней', 'для', 'мы', 'тебя', 'их', 'чем', 'была', 'сам', 'чтоб', 'без', 'будто', 'чего', 'раз', 'тоже', 'себе', 'под', 'будет', 'ж', 'тогда', 'кто', 'этот', 'того', 'потому', 'этого', 'какой', 'совсем', 'ним', 'здесь', 'этом', 'один', 'почти', 'мой', 'тем', 'чтобы', 'нее', 'сейчас', 'были', 'куда', 'зачем', 'всех', 'никогда', 'можно', 'при', 'наконец', 'два', 'об', 'другой', 'хоть', 'после', 'над', 'больше', 'тот', 'через', 'эти', 'нас', 'про', 'всего', 'них', 'какая', 'много', 'разве', 'три', 'эту', 'моя', 'впрочем', 'хорошо', 'свою', 'этой', 'перед', 'иногда', 'лучше', 'чуть', 'том', 'нельзя', 'такой', 'им', 'более', 'всегда', 'конечно', 'всю', 'между']

# blob = TextBlob('Today is a beautiful day.')

# print( [word for word in blob.words if word not in stops] )
# # ['Today', 'beautiful', 'day']


# ----------------------------------------------------
# Getting Definitions, Synonyms and Antonyms from WordNet
# https://wordnet.princeton.edu/
# https://www.nltk.org/api/nltk.corpus.reader.html#module-nltk.corpus.reader.wordnet
# ----------------------------------------------------


# happy = Word('happy')

# print(happy.definitions)
# # ['enjoying or showing or marked by joy or pleasure', 'marked by good fortune', 'eagerly disposed to act or to be of service', 'well expressed and to the point']

# print( happy.synsets )
# # [Synset('happy.a.01'), Synset('felicitous.s.02'), Synset('glad.s.02'), Synset('happy.s.04')]

# synonims = set()
# for synset in happy.synsets:
#     for lemma in synset.lemmas():
#         synonims.add(lemma.name())

# print(synonims)
# # {'happy', 'glad', 'well-chosen', 'felicitous'}

# lemmas = happy.synsets[0].lemmas()

# print(lemmas)
# # [Lemma('happy.a.01.happy')]

# print(lemmas[0].antonyms())
# # [Lemma('unhappy.a.01.unhappy')]



# ----------------------------------------------------
# Word Frequencies
# ----------------------------------------------------
# blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())

# print( blob.word_counts['juliet'] )
# # 190

# print( blob.word_counts['romeo'] )
# # 315

# print( blob.word_counts['thou'] )
# # 278

# print( blob.words.count('joy') )
# # 14

# print( blob.noun_phrases.count('lady capulet') )
# # 46

# ----------------------------------------------------
# Normalization: Stemming and Lemmatization
# stemming removes a prefix or suffix from a word
# Lemmatization is similar but results in real word
# ----------------------------------------------------
# word = Word('varieties')

# print( word.stem() )
# # varieti

# print( word.lemmatize() )
# # variety

# ----------------------------------------------------
# Spell Checking and Correction
# ----------------------------------------------------
# word = Word('theyr')
# print( word.spellcheck() )
# # [('they', 0.5713042216741622), ('their', 0.42869577832583783)]

# print( word.correct() )
# # they

# sentence = TextBlob('Ths sentense has missplled wrds.')
# print( sentence.correct() )
# # The sentence has misspelled words.


# ----------------------------------------------------
# Inflection: Pluralization and Singularization
# ----------------------------------------------------
# index = Word('index')
# print( index.pluralize() )
# # indices

# cacti = Word('cacti')
# print( cacti.singularize() )
# # cactus

# animals = TextBlob('dog cat fish bird').words
# print( animals.pluralize() )
# # ['dogs', 'cats', 'fish', 'birds']



# ----------------------------------------------------
# Create a TextBlob
# ----------------------------------------------------

# text = 'Today is a beautiful day. Tomorrow looks like bad weather.'

# blob = TextBlob(text)

# print(blob)
# # Today is a beautiful day. Tomorrow looks like bad weather.

# # ----------------------------------------------------
# # Tokenizing Text
# # ----------------------------------------------------

# print(blob.sentences)
# # [Sentence("Today is a beautiful day."), Sentence("Tomorrow looks like bad weather.")]

# print(blob.words)
# # ['Today', 'is', 'a', 'beautiful', 'day', 'Tomorrow', 'looks', 'like', 'bad', 'weather']

# # ----------------------------------------------------
# # Parts-of-Speech (POS) Tagging
# # ----------------------------------------------------

# print(blob.tags)
# # [('Today', 'NN'), ('is', 'VBZ'), ('a', 'DT'), ('beautiful', 'JJ'), ('day', 'NN'), ('Tomorrow', 'NNP'), ('looks', 'VBZ'), ('like', 'IN'), ('bad', 'JJ'), ('weather', 'NN')]

# # ----------------------------------------------------
# # Extracting Noun Phrases
# # ----------------------------------------------------

# # print(blob.noun_phrases)
# # ['beautiful day', 'tomorrow', 'bad weather']

# # ----------------------------------------------------
# # Sentiment analysis
# # 
# # the process of computationally identifying and categorizing opinions 
# # expressed in a piece of text, especially in order to determine 
# # whether the writer's attitude towards a particular topic, product, etc. 
# # is positive, negative, or neutral.
# # ----------------------------------------------------

# print(blob.sentiment)
# # Sentiment(polarity=0.07500000000000007, subjectivity=0.8333333333333333)

# print( "{:.3f}".format(blob.sentiment.polarity) )
# # 0.075

# print( "{:.3f}".format(blob.sentiment.subjectivity) )
# # 0.833

# for sentence in blob.sentences:
#     print( sentence.sentiment )
# # Sentiment(polarity=0.85, subjectivity=1.0)
# # Sentiment(polarity=-0.6999999999999998, subjectivity=0.6666666666666666)

# # ----------------------------------------------------
# # Sentiment analysis with NaiveBayesAnalyzer
# # ----------------------------------------------------
# blob = TextBlob( text, analyzer=NaiveBayesAnalyzer() )

# print( blob )
# # Today is a beautiful day. Tomorrow looks like bad weather.

# print( blob.sentiment )
# # Sentiment(classification='neg', p_pos=0.47662917962091056, p_neg=0.5233708203790892)

# for sentence in blob.sentences:
#     print( sentence.sentiment )
# # Sentiment(classification='pos', p_pos=0.8117563121751951, p_neg=0.18824368782480477)
# # Sentiment(classification='neg', p_pos=0.174363226578349, p_neg=0.8256367734216521)


# # ----------------------------------------------------
# # Language detection and Translation
# # ----------------------------------------------------

# print( blob.detect_language() )
# # en

# russian = blob.translate(to='ru')
# print(russian)
# # Сегодня прекрасный день. Завтра похоже плохая погода.
# print(russian.detect_language())
# # ru

# chinese = blob.translate(to='zh')
# print(chinese)
# # 今天是美好的一天。明天看起来天气不好。

# print(chinese.detect_language())
# # zh-CN

# print( russian.translate() )
# # Today is a wonderful day. Tomorrow looks like bad weather.

# print( chinese.translate() )
# # Today is a beautiful day. The weather looks bad tomorrow.
