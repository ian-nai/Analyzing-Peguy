import pandas as pd
import matplotlib.pyplot as plt, mpld3
import numpy as np
import csv
from nltk.tokenize import RegexpTokenizer
import codecs
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import LineTokenizer
from nltk.tokenize import word_tokenize
import re
from collections import Counter
import pylab

column_names = ["text", "pos", "total", "pos_unique"]

input_files_full = ['eve.txt']

# In chronological order...
# 'le_porche_du_mystere_de_la_deuxieme_vertu.txt'
#['la_tapisserie_de_sainte_genevieve.txt']
#['la_tapisserie_notre_dame.txt']
# 'eve.txt']
# 'le_mystere_de_la_charite_de_jeanne_darc.txt',
# 'le_mystere_des_saints_innocents.txt',

#input_files =
# POEMS:
# stanza_lines_le_porche_du_mystere_de_la_deuxieme_vertu.txt.csv 1912
# stanza_lines_la_tapisserie_de_sainte_genevieve.txt.csv 1913
# stanza_lines_la_tapisserie_notre_dame.txt.csv 1913
# stanza_lines_eve.txt.csv 1913
# PLAYS:
# 'stanza_lines_le_mystere_de_la_charite_de_jeanne_darc.txt.csv' 1910
# 'stanza_lines_le_mystere_des_saints_innocents.txt.csv' 1912


df = pd.read_csv('stanza_lines_eve.txt.csv', names=column_names)

print(df.text)

lines_list = []
words_list = []
pos_list = []
total_pos_list = []
unique_pos_list = []

for f in df.text:
    lines_list.append(f)

lines_list.pop(0)

for q in df.pos:
    pos_list.append(q)

pos_list.pop(0)

for f in df.total:
    total_pos_list.append(f)

total_pos_list.pop(0)

for f in df.pos_unique:
    unique_pos_list.append(f)

unique_pos_list.pop(0)

total_pos_sum = 0
for ele in range(0, len(total_pos_list)):
    total_pos_sum = total_pos_sum + int(total_pos_list[ele])

total_unique_pos_sum = 0
for ele in range(0, len(unique_pos_list)):
    total_unique_pos_sum = total_unique_pos_sum + int(unique_pos_list[ele])

line_lengths_list = []
num_long_words_per_line = []

for f in lines_list:
    words = f.split()
    for l in words:
        if l != "c'" and l != "est" and l != "qu'" and l != "n'" and l != "l'":
            words_list.append(l)
    line_lengths_list.append(len(words))

    num_long_words_counter = 0
    for x in words:
        if len(x) >= 7:
            num_long_words_counter += 1
    num_long_words_per_line.append(num_long_words_counter)

default_stopwords = set(nltk.corpus.stopwords.words('french'))

filtered_words = [w for w in words_list if not w in default_stopwords]

filtered_sentence = []

for w in words_list:
    if w not in default_stopwords:
        filtered_words.append(w)

total_words_graph = []
for x in words_list:
    total_words_graph.append(len(x))

for index, item in enumerate(pos_list):
    pos_list[index] = item.replace('[', '').replace(']', '')

for index, item in enumerate(pos_list):
    pos_list[index] = item.replace('"', '').replace("'", '')

for index, item in enumerate(pos_list):
    pos_list[index] = item.replace(',', '')

print(pos_list)

avg_line_length_list = []
long_words_document = []
words_lines_document = []

for f in input_files_full:

    fp = codecs.open(f, 'r', 'utf-8')


    t = fp.read()

    content_list = t.splitlines()

    new_lines = []

    tokenizer = nltk.data.load('tokenizers/punkt/PY3/french.pickle')

    lines_split = tokenizer.tokenize(t)
    num_sentences = len(lines_split)


    compiled_pattern = re.compile(r"([a-zA-ZÀ-Ÿ]+['’])([a-zA-ZÀ-Ÿ]*)")


    pattern = r"[dnl]['´`]|\w+|\$[\d\.]+|\S+"
    word_tokenizer = RegexpTokenizer(pattern)

    for line in content_list:
        words = word_tokenizer.tokenize(line)
        num_words = len(words)
        avg_line_length_list.append(num_words)

        for x in words:
            if x != 0:
                words_lines_document.append(num_words)

        num_long_words = 0
        for x in words:
            if len(x) >= 7:
                num_long_words +=1

        long_words_document.append(num_long_words)

    tuple_doc = list(zip(long_words_document, words_lines_document))
    print(tuple_doc)

    res = []
    try:
        for i, j in tuple_doc:
            res.append(i / j)
    except ZeroDivisionError:
        res.append(0)
        res.next()
        continue

    print(res)

    # Calculating readability scores
    percentages = []
    for x in res:
        x *= 100
        percentages.append(x)

    print(percentages)

    total_percentage = 0
    for ele in range(0, len(percentages)):
        total_percentage = total_percentage + percentages[ele]


    liv = (total_percentage / len(percentages))
    print('liv score: ' + str(liv))

    rix = (len(long_words_document) / len(words_lines_document))
    rix *= 100
    print('rix score: ' + str(rix))


line_length_sum = 0
for ele in range(0, len(avg_line_length_list)):
    line_length_sum = line_length_sum + avg_line_length_list[ele]

avg_line_length = (line_length_sum / len(avg_line_length_list))

unique_words = set(words_list)

# WORD CLOUD
from wordcloud import WordCloud, ImageColorGenerator

#convert list to string and generate
unique_string=(" ").join(filtered_words)
wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("la_tapisserie_de_sainte_genevieve_wordcloud.png", bbox_inches='tight')
plt.show()
plt.close()

'''
# most common words

Counter = Counter(words_list)

most_occur = Counter.most_common(20)

print(most_occur)
'''

# graph pos unique vs total
total_nums_list = []
total_unique_list  = []

for f in df.total[1:]:
    total_nums_list.append(int(f))

total_nums_list.pop(0)

for f in df.pos_unique[1:]:
    total_unique_list.append(int(f))

total_unique_list.pop(0)

print(total_nums_list)
print(total_unique_list)

# creating a list of tuples
tuple_list = list(zip(total_nums_list, total_unique_list))
print(tuple_list)

# get average num of words and unique pos
import statistics

avg_words = statistics.mean(total_nums_list)
avg_pos_unique = statistics.mean(total_unique_list)

print(avg_words)
print(avg_pos_unique)


labels = ['Ève (1913)']
x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, avg_words, width, label='Avg Words')
rects2 = ax.bar(x + width/2, avg_pos_unique, width, label='Unique POS')

ax.set_ylabel('Num Words')
ax.set_title('Avg Wordcount and Avg Unique POS Per Line')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.savefig("eve_pos_unique.png")
plt.show()
mpld3.save_html(fig,"eve_pos_unique.html")
mpld3.fig_to_html(fig,template_type="simple")


# num of unique words in a poem vs num of total words
unique_words = set(words_list)

labels = ['Ève (1913)']

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, len(words_list), width, label='Total Words')
rects2 = ax.bar(x + width/2, len(unique_words), width, label='Unique Words')

ax.set_ylabel('Num Words')
ax.set_title('Total Words and Unique Words')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.savefig("eve_words_unique.png")
plt.show()
mpld3.save_html(fig,"eve_words_unique.html")
mpld3.fig_to_html(fig,template_type="simple")

# length of lines across the text
print(len(avg_line_length_list))
print(len(total_words_graph))

fig, ax = plt.subplots()
ax.plot(total_words_graph)

ax.set(xlabel='Words', ylabel='Length of Words',
       title='Ève (1913)')
ax.grid()

plt.savefig("eve_words_total_words.png")
plt.show()

mpld3.save_html(fig,"eve_words_total_words.html")
mpld3.fig_to_html(fig,template_type="simple")

# avg line length
fig, ax = plt.subplots()
ax.plot(line_lengths_list)

ax.set(xlabel='Line Number', ylabel='Line Length',
       title='Ève (1913)')
ax.grid()

plt.savefig("eve_words_avg_words.png")
plt.show()

mpld3.save_html(fig,"eve_words_avg_words.html")
mpld3.fig_to_html(fig,template_type="simple")

# long words throughout the text
fig, ax = plt.subplots()
ax.plot(num_long_words_per_line)

ax.set(xlabel='Line Number', ylabel='Number of Long Words',
       title='Ève (1913)')
ax.grid()

plt.savefig("eve_words_long_words.png")
plt.show()

mpld3.save_html(fig,"eve_words_long_words.html")
mpld3.fig_to_html(fig,template_type="simple")

'''
# bar graph with length of lines across all texts

all_files = ['vis_test_le_porche_du_mystere_de_la_deuxieme_vertu.txt.csv',
'vis_test_la_tapisserie_de_sainte_genevieve.txt.csv',
'vis_test_la_tapisserie_notre_dame.txt.csv',
'vis_test_eve.txt.csv',
'vis_test_le_mystere_de_la_charite_de_jeanne_darc.txt.csv',
'vis_test_le_mystere_des_saints_innocents.txt.csv']


li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

print(frame)

avg_length_graph = []

for f in frame['avg length of lines']:
    avg_length_graph.append(f)


print(avg_length_graph)

from textwrap import wrap

data = {' Le Porche du Mystère de la Deuxième Vertu (1912)':avg_length_graph[0], 'La Tapisserie de Sainte Geneviève et de Jeanne d\'Arc (1913)':avg_length_graph[1], 'La Tapisserie de Notre-Dame (1913)':avg_length_graph[2],
        'Ève (1913)':avg_length_graph[3], 'Le Mystère de la Charité de Jeanne d\'Arc (1910)': avg_length_graph[4], 'Le Mystère des Saints Innocents (1912)': avg_length_graph[5]}

poems = list(data.keys())
values = list(data.values())
poems = [ '\n'.join(wrap(l, 20)) for l in poems ]

fig, ax = plt.subplots()
# creating the bar plot
ax.bar(poems, values, color ='blue',
        width = 0.4)

plt.xlabel("Texts")
plt.ylabel("Avg Line Length")
plt.title("Avg Line Lengths Across Texts")



plt.savefig("all_poems_length_graph.png")
plt.show()

mpld3.save_html(fig,"all_poems_length_graph.html")
mpld3.fig_to_html(fig,template_type="simple")
'''

# output data to csv
with open(('vis_test_' + input_files_full[0] + '.csv'), 'w') as csvfile:
        fieldnames = ['total words', 'total unique words', 'total pos', 'total unique pos', 'liv score', 'rix score', 'avg length of lines', 'num of long words']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'total words': len(words_lines_document), 'total unique words': len(unique_words), 'total pos': total_pos_sum, 'total unique pos': total_unique_pos_sum, 'liv score': str(liv), 'rix score': str(rix), 'avg length of lines': avg_line_length, 'num of long words': len(long_words_document)})
