import pandas as pd
import matplotlib.pyplot as plt, mpld3
import numpy as np
import csv
from nltk.tokenize import RegexpTokenizer

column_names = ["text", "pos", "total", "pos_unique"]

input_files_full = ['le_porche_du_mystere_de_la_deuxieme_vertu.txt']

# chronological order...

# 'le_porche_du_mystere_de_la_deuxieme_vertu.txt'
#['la_tapisserie_de_sainte_genevieve.txt']
#['la_tapisserie_notre_dame.txt']
# 'eve.txt']
# 'le_mystere_de_la_charite_de_jeanne_darc.txt',
# 'le_mystere_des_saints_innocents.txt',

#input_files =
# stanza_lines_le_porche_du_mystere_de_la_deuxieme_vertu.txt.csv 1912
# stanza_lines_la_tapisserie_de_sainte_genevieve.txt.csv 1913
# stanza_lines_la_tapisserie_notre_dame.txt.csv 1913
# stanza_lines_eve.txt.csv 1913
# 'stanza_lines_le_mystere_de_la_charite_de_jeanne_darc.txt.csv' 1910
# 'stanza_lines_le_mystere_des_saints_innocents.txt.csv' 1912


# ['vis test.csv']#"stanza_lines_la_tapisserie_de_sainte_genevieve.txt.csv"]
# 'stanza_lines_la_tapisserie_notre_dame.txt.csv',
# 'stanza_lines_le_mystere_de_la_charite_de_jeanne_darc.txt.csv',
# 'stanza_lines_le_mystere_des_saints_innocents.txt.csv',
# 'stanza_lines_le_porche_du_mystere_de_la_deuxieme_vertu.txt.csv',
# 'stanza_lines_eve.txt.csv']

# redo this with stanza csv...
df = pd.read_csv("stanza_lines_le_porche_du_mystere_de_la_deuxieme_vertu.txt.csv", names=column_names)

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



# total_words_graph = 0
# for ele in range(0, len(words_list)):
#     total_words_graph = total_words_graph + len(words_list[ele])
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



# readability

import codecs
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import LineTokenizer
from nltk.tokenize import word_tokenize
import re


# NLTK's default French stopwords
default_stopwords = set(nltk.corpus.stopwords.words('french'))


#liv: percentage of 7+ letter words + avg num of words per sentence
# rix: 7+ / num of sentences

avg_line_length_list = []
long_words_document = []
words_lines_document = []

for f in input_files_full:




    fp = codecs.open(f, 'r', 'utf-8')


    t = fp.read()

    content_list = t.splitlines()
    # for f in content_list:
    #     avg_line_length_list.append(len(f))

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
        #avg_line_length_list.append(num_words)

        for x in words:
            if x != 0:
                words_lines_document.append(num_words)

        num_long_words = 0
        for x in words:
            if len(x) >= 7:
                num_long_words +=1
        #print(num_long_words)

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



    # with open(('sentences_' + input_files[index_num]), 'w') as f:
    #             f.write('\n\n'.join(new_lines))
    #
    # index_num += 1

line_length_sum = 0
for ele in range(0, len(avg_line_length_list)):
    line_length_sum = line_length_sum + avg_line_length_list[ele]

avg_line_length = (line_length_sum / len(avg_line_length_list))

unique_words = set(words_list)

# WORD CLOUD


from wordcloud import WordCloud, ImageColorGenerator

#convert list to string and generate
unique_string=(" ").join(words_list)
wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("deuxieme_vertu_wordcloud.png", bbox_inches='tight')
plt.show()
plt.close()


'''
# most common words

from collections import Counter

# Pass the split_it list to instance of Counter class.
Counter = Counter(words_list)

# most_common() produces k frequently encountered
# input values and their respective counts.
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



labels = ['Le Porche du Mystère de la Deuxième Vertu (1912)']
# poem_avg = [20, 34, 30, 35, 27]
# poem_unique_avg = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

# ax.hist(long_words_document, 30, histtype='stepfilled', fc='blue', alpha=0.5);
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, avg_words, width, label='Avg Words')
rects2 = ax.bar(x + width/2, avg_pos_unique, width, label='Unique POS')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Num Words')
ax.set_title('Avg Wordcount and Avg Unique POS Per Line')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
mpld3.save_html(fig,"deuxieme_vertu_pos_unique.html")
mpld3.fig_to_html(fig,template_type="simple")


# num of unique words in a poem vs num of total words

from collections import Counter


unique_words = set(words_list)
#print(len(unique_words))


labels = ['Le Porche du Mystère de la Deuxième Vertu (1912)']
# poem_avg = [20, 34, 30, 35, 27]
# poem_unique_avg = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

# ax.hist(long_words_document, 30, histtype='stepfilled', fc='blue', alpha=0.5);
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, len(words_list), width, label='Total Words')
rects2 = ax.bar(x + width/2, len(unique_words), width, label='Unique Words')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Num Words')
ax.set_title('Total Words and Unique Words')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
mpld3.save_html(fig,"deuxieme_vertu_words_unique.html")
mpld3.fig_to_html(fig,template_type="simple")
#words_lines_document

# length of lines/sentences individually and across poems (total doc--
# not just stopwords)--use line graph since many lines to graph at once



# num of longwords vs num total words;
#long_words_document vs words_lines_document
'''

# LENGTH OF LINES ACROSS DOCUMENT - FULL VS STOPWORDS

print(len(avg_line_length_list))
print(len(total_words_graph))

import pylab

# y = range(len(avg_line_length_list))
# # define data values
# plt.scatter(avg_line_length_list, y)
#   # Plot the chart
# plt.show()  # display

'''

## EDIT THIS FOR LINES
fig, ax = plt.subplots()
ax.plot(total_words_graph)

ax.set(xlabel='Words', ylabel='Length of Words',
       title='Le Porche du Mystère de la Deuxième Vertu (1912)')
ax.grid()

#fig.savefig("test.png")
plt.show()

#y2 = range(len(total_words_graph))
# define data values
#plt.plot(total_words_graph)

mpld3.save_html(fig,"deuxieme_vertu_words_total_words.html")
mpld3.fig_to_html(fig,template_type="simple")

  # Plot the chart

# AVG LINE LENGTH - same as above

fig, ax = plt.subplots()
ax.plot(line_lengths_list)

ax.set(xlabel='Line Number', ylabel='Line Length',
       title='Le Porche du Mystère de la Deuxième Vertu (1912)')
ax.grid()

#fig.savefig("test.png")
plt.show()

#y2 = range(len(total_words_graph))
# define data values
#plt.plot(total_words_graph)

mpld3.save_html(fig,"deuxieme_vertu_words_avg_words.html")
mpld3.fig_to_html(fig,template_type="simple")

# LONG WORDS THROUGHOUT DOCUMENT - pretty much the same, except a scatter
#long_words_document vs words_lines_document

# define data values
#y2 = range(len(words_lines_document))
#plt.scatter(y2, words_lines_document)

fig, ax = plt.subplots()
ax.plot(num_long_words_per_line)

ax.set(xlabel='Line Number', ylabel='Number of Long Words',
       title='Le Porche du Mystère de la Deuxième Vertu (1912)')
ax.grid()

#fig.savefig("test.png")
plt.show()

#y2 = range(len(total_words_graph))
# define data values
#plt.plot(total_words_graph)

mpld3.save_html(fig,"deuxieme_vertu_words_long_words.html")
mpld3.fig_to_html(fig,template_type="simple")

  # Plot the chart
plt.show()  # display
'''

#define data values
#plt.plot(long_words_document)

# Histogram with modified axes/grid

'''
'''
# bar graph with length of lines total

all_files = ['stanza_lines_le_porche_du_mystere_de_la_deuxieme_vertu.txt.csv',
'stanza_lines_la_tapisserie_de_sainte_genevieve.txt.csv',
'stanza_lines_la_tapisserie_notre_dame.txt.csv',
'stanza_lines_eve.txt.csv',
'stanza_lines_le_mystere_de_la_charite_de_jeanne_darc.txt.csv',
'stanza_lines_le_mystere_des_saints_innocents.txt.csv']


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



data = {'C':avg_length_graph[0], 'C++':avg_length_graph[1], 'Java':avg_length_graph[2],
        'Python':avg_length_graph[3], 'test': avg_length_graph[4], 'test2': avg_length_graph[5]}

poems = list(data.keys())
values = list(data.values())

fig, ax = plt.subplots()
# creating the bar plot
ax.bar(poems, values, color ='blue',
        width = 0.4)

plt.xlabel("poems")
plt.ylabel("avg line length")
plt.title("avg line lengths across texts")

import numpy as np

plt.show()

#plt.plot(words_lines_document)
  # Plot the chart
#plt.show()

mpld3.save_html(fig,"test.html")
mpld3.fig_to_html(fig,template_type="simple")
'''


# stuff to graph: num unique words vs num total words - done, length of lines/sentences individually and across poems (total doc--
#not just stopwords)--use line graph since many lines to graph at once - individual done;
# num of longwords vs num non-long words - done; liv and rix readability scores across poems--do this in csvs

# values, counts = np.unique(words_list, return_counts=True)
#
# print(values, counts)


# liv and rix readability formulas
# liv: percentage of 7+ letter words + avg num of words per sentence
# rix: 7+ / num of sentences

'''
with open(('vis_test_' + input_files_full[0] + '.csv'), 'w') as csvfile:
        fieldnames = ['total words', 'total unique words', 'total pos', 'total unique pos', 'liv score', 'rix score', 'avg length of lines', 'num of long words']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'total words': len(words_lines_document), 'total unique words': len(unique_words), 'total pos': total_pos_sum, 'total unique pos': total_unique_pos_sum, 'liv score': str(liv), 'rix score': str(rix), 'avg length of lines': avg_line_length, 'num of long words': len(long_words_document)})
'''
