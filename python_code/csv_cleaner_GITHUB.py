import spacy
from spacy_lefff import LefffLemmatizer, POSTagger
import pickle
import re
from collections import Counter
import csv

index_num = 0

files = ["la_tapisserie_de_sainte_genevieve.txt"] #, "nostop_le_mystere_des_saints_innocents.txt", "nostop_le_porche_du_mystere_de_la_deuxieme_vertu.txt", "nostop_peguy_eve.txt"]


nlp = spacy.load("fr_dep_news_trf")
# pos = POSTagger()
# #french_lemmatizer = LefffLemmatizer(after_melt=True, default=True)
# nlp.add_pipe(pos, name='pos', after='parser')
# nlp.add_pipe(french_lemmatizer, name='lefff', after='pos')


list_keys = []
list_nums = []
list_nums_unique = []
text_bits = []
perm_pos = []

for f in files:
    # Open our file
    with open(f) as file:
        text_data = file.read()
    #print(text_data)
    testing_list = text_data.splitlines()

    # print(testing_list)
    for x in testing_list:
        doc = nlp(x)
        pos_elements = []
        actual_pos = []

        for d in doc:
            print(d.text, d.pos_)
            pos_elements.append(d)
            actual_pos.append(d.pos_)

    # Specify the information we want
    # for x in testing_list:
    #
    #     doc = nlp(x)
    #     pos_elements = []
    #     actual_pos = []
    #
    #     for q in nlp.pipe(doc):
    #         # Do something with the doc here
    #         print([(ent.text, ent.label_) for ent in doc.ents])

        pos_keys = Counter(actual_pos).keys() # equals to list(set(words))
        pos_nums = Counter(pos_elements).values() # counts the elements' frequency


        list_keys.append(pos_elements)

        total_num = str(len(pos_nums))



        text_bits.append(pos_elements)
        q = str(len(pos_keys))

        list_nums_unique.append(q)

        list_nums.append(total_num)

        perm_pos.append(actual_pos)

    print(len(perm_pos))
    print(len(text_bits))
    print(len(list_nums))
    print(len(list_nums_unique))

# Output our tagged data into a CSV
    with open('text_testing_SPACY3.csv', 'w') as csvfile:
        fieldnames = ['text', 'pos', 'total', 'pos_unique']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        x = 0
        for d in testing_list:
            writer.writerow({'text': text_bits[x], 'pos': perm_pos[x], 'total': list_nums[x], 'pos_unique': list_nums_unique[x]})
            x += 1
