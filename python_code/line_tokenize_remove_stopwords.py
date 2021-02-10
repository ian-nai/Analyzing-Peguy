import codecs
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import LineTokenizer
from nltk.tokenize import word_tokenize
import re
import string


index_num = 0

# NLTK's default French stopwords
default_stopwords = set(nltk.corpus.stopwords.words('french'))

compiled_pattern = re.compile(r"([a-zA-ZÀ-Ÿ]+['’])([a-zA-ZÀ-Ÿ]*)")

input_files = ['la_tapisserie_de_sainte_genevieve.txt']
'''
,
'la_tapisserie_notre_dame.txt',
'le_mystere_de_la_charite_de_jeanne_darc.txt',
'le_mystere_des_saints_innocents.txt',
'le_porche_du_mystere_de_la_deuxieme_vertu.txt',
'peguy_eve.txt']
'''
for f in input_files:
    fp = codecs.open(f, 'r', 'utf-8')
    text = fp.read()
    lines = LineTokenizer(blanklines='discard').tokenize(text)

    final_lines = []

    for line in lines:
# Replace the target string
        words_list = []
        final_words = []

        tokens = word_tokenize(line)
        new_tokens = []
        for token in tokens:
            search_results = re.findall(r"['’]",token)
            if search_results and len(search_results) == 1:
                new_tokens.extend(re.split(compiled_pattern,token)[1:3])
            else:
                new_tokens.append(token)


        words_list.append(new_tokens)
        print(words_list)

        for words in words_list:


    # remove punctuation
      #   from nltk.tokenize import RegexpTokenizer
#         tokenizer2 = RegexpTokenizer(r'\w+')
#         for word in words:
#             tokenizer2.tokenize(word)

    # Remove single-character tokens (mostly punctuation)

            words = [word for word in words if len(word) > 1]

    # Remove numbers
            words = [word for word in words if not word.isnumeric()]

    # Lowercase all words (default_stopwords are lowercase too)
            words = [word.lower() for word in words]


    # Remove stopwords
            words = [word for word in words if word not in default_stopwords]

            for word in words:
                word = word.replace('_', '')
            for word in words:
                word = "".join(l for l in word if l not in string.punctuation)

            line = ' '.join(words)
            final_lines.append(line)

    #print(final_lines)
        #print(words)
# Write the file out again
    with open(('line2_' + input_files[index_num]), 'w') as f:
            #f.write("%s\n" % item)
        f.write('\n'.join(final_lines))


    index_num += 1
