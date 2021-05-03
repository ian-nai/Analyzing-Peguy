import spacy
from spacy_lefff import LefffLemmatizer, POSTagger
import pickle
import re
from collections import Counter
import csv

index_num = 0

files = ['lines_la_tapisserie_de_sainte_genevieve.txt',
'lines_la_tapisserie_notre_dame.txt',
'lines_le_mystere_de_la_charite_de_jeanne_darc.txt',
'lines_le_mystere_des_saints_innocents.txt',
'lines_le_porche_du_mystere_de_la_deuxieme_vertu.txt',
'lines_eve.txt']

nlp = spacy.load("fr_core_news_lg")


list_keys = []
list_nums = []
list_nums_unique = []
text_bits = []
perm_pos = []

for f in files:
    with open(f) as file:
        text_data = file.read()

    testing_list = text_data.splitlines()

    for x in testing_list:
        doc = nlp(x)
        pos_elements = []
        actual_pos = []

        for d in doc:
            print(d.text, d.pos_)
            # pos_elements.append(d)
            # actual_pos.append(d.pos_)
            if d.text != '.' and d.text != ',' and d.text != '...' and d.text != '-' and d.text != '--':
                pos_elements.append(d.text)
            if d.pos_ != 'PUNCT':
                actual_pos.append(d.pos_)

        print('gack ' + str(pos_elements))
        pos_keys = Counter(actual_pos).keys()
        pos_nums = Counter(pos_elements).values()


        list_keys.append(pos_elements)

        total_num = str(len(pos_nums))

        test_list_test = []

        for x in pos_elements:
            test_list_test.append(str(x))

        new_list = ' '.join(test_list_test)
        text_bits.append(new_list)

        q = str(len(pos_keys))

        list_nums_unique.append(q)

        list_nums.append(total_num)

        perm_pos.append(actual_pos)

    print(len(perm_pos))
    print(len(text_bits))
    print(len(list_nums))
    print(len(list_nums_unique))



    with open('pos_spacy' + files[index_num] + '.csv', 'w') as csvfile:
        fieldnames = ['text', 'pos', 'total', 'pos_unique']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        x = 0
        for d in testing_list:
                writer.writerow({'text': text_bits[x], 'pos': perm_pos[x], 'total': list_nums[x], 'pos_unique': list_nums_unique[x]})
                x += 1
        index_num += 1
