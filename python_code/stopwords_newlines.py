import codecs
import nltk
from nltk.corpus import stopwords
import re

index_num = 0

# NLTK's default French stopwords
default_stopwords = set(nltk.corpus.stopwords.words('french'))

input_files = ['la_tapisserie_de_sainte_genevieve.txt',
'la_tapisserie_notre_dame.txt',
'le_mystere_de_la_charite_de_jeanne_darc.txt',
'le_mystere_des_saints_innocents.txt',
'le_porche_du_mystere_de_la_deuxieme_vertu.txt',
'eve.txt']

for f in input_files:
    fp = codecs.open(f, 'r', 'utf-8')


    words = nltk.word_tokenize(fp.read())

    # remove punctuation
 #    from nltk.tokenize import RegexpTokenizer
#     tokenizer2 = RegexpTokenizer(r'\w+')
#     for word in words:
#         tokenizer2.tokenize(word)

    # Remove single-character tokens (mostly punctuation)
    words = [word for word in words if len(word) > 1]

    # Remove numbers
    words = [word for word in words if not word.isnumeric()]

    # Lowercase all words (default_stopwords are lowercase too)
    words = [word.lower() for word in words]


    # Remove stopwords
    words = [word for word in words if word not in default_stopwords]

    for word in words:
        word = [item.replace("_", "") for item in word]
        word = [item.replace("|", "") for item in word]
        pattern = '[0-9]'
        word = [re.sub(pattern, '', i) for i in word]

    # Save our new file as 'cleaned_text.txt'
    with open(('cleaned_' + input_files[index_num]), 'w') as f:
        for item in words:
            f.write("%s\n" % item)

    index_num += 1
