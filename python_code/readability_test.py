import codecs
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import LineTokenizer
from nltk.tokenize import word_tokenize
import re

index_num = 0

# NLTK's default French stopwords
default_stopwords = set(nltk.corpus.stopwords.words('french'))

input_files = ['la_tapisserie_de_sainte_genevieve.txt']
# 'la_tapisserie_notre_dame.txt',
# 'le_mystere_de_la_charite_de_jeanne_darc.txt',
# 'le_mystere_des_saints_innocents.txt',
# 'le_porche_du_mystere_de_la_deuxieme_vertu.txt',
# 'eve.txt']

#liv: percentage of 7+ letter words + avg num of words per sentence
# rix: 7+ / num of sentences

for f in input_files:

    long_words_document = []
    words_lines_document = []


    fp = codecs.open(f, 'r', 'utf-8')


    t = fp.read()

    new_lines = []

    tokenizer = nltk.data.load('tokenizers/punkt/PY3/french.pickle')

    lines_split = tokenizer.tokenize(t)
    num_sentences = len(lines_split)


    compiled_pattern = re.compile(r"([a-zA-ZÀ-Ÿ]+['’])([a-zA-ZÀ-Ÿ]*)")


    for line in lines_split:
        words = word_tokenize(line)
        num_words = len(words)

        words_lines_document.append(num_words)

        num_long_words = 0
        for x in words:
            if len(x) >= 7:
                num_long_words +=1
        #print(num_long_words)

        long_words_document.append(num_long_words)

    tuple_doc = list(zip(long_words_document, words_lines_document))
    print(tuple_doc)

    res = [i / j for i, j in tuple_doc]
    print(res)

    percentages = []
    for x in res:
        x *= 100
        percentages.append(x)

    print(percentages)

    total_percentage = 0
    for ele in range(0, len(percentages)):
        total_percentage = total_percentage + percentages[ele]


    liv = (total_percentage / len(percentages))
    print(liv)

    rix = (long_words_document[0] / words_lines_document[0])
    print(rix)


    # with open(('sentences_' + input_files[index_num]), 'w') as f:
    #             f.write('\n\n'.join(new_lines))
    #
    # index_num += 1
