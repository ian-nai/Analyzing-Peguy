import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

column_names = ["text", "pos", "total", "pos_unique"]

df = pd.read_csv("stanza_lines_la_tapisserie_de_sainte_genevieve.txt.csv", names=column_names)

print(df.text)

lines_list = []
words_list = []
pos_list = []

for f in df.text:
    lines_list.append(f)

lines_list.pop(0)

for q in df.pos:
    pos_list.append(q)

pos_list.pop(0)


for f in lines_list:
    words = f.split()
    for l in words:
        if l != "c'" and l != "est" and l != "qu'" and l != "n'" and l != "l'":
            words_list.append(l)

for index, item in enumerate(pos_list):
    pos_list[index] = item.replace('[', '').replace(']', '')

for index, item in enumerate(pos_list):
    pos_list[index] = item.replace('"', '').replace("'", '')

for index, item in enumerate(pos_list):
    pos_list[index] = item.replace(',', '')

print(pos_list)

'''
# WORD CLOUD


from wordcloud import WordCloud, ImageColorGenerator

#convert list to string and generate
unique_string=(" ").join(words_list)
wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("testing_images"+".png", bbox_inches='tight')
plt.show()
plt.close()

'''
'''
# most common words

from collections import Counter

# Pass the split_it list to instance of Counter class.
Counter = Counter(words_list)

# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(4)

print(most_occur)
'''
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


labels = ['poem1']
# poem_avg = [20, 34, 30, 35, 27]
# poem_unique_avg = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, avg_words, width, label='Men')
rects2 = ax.bar(x + width/2, avg_pos_unique, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
'''
'''
# num of unique words in a poem

from collections import Counter


unique_words = set(words_list)
print(len(unique_words))

# values, counts = np.unique(words_list, return_counts=True)
#
# print(values, counts)
'''

# liv and rix readability formulas
# liv: percentage of 7+ letter words + avg num of words per sentence
# rix: 7+ / num of sentences
