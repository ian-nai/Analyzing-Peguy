'''
import stanza

nlp = stanza.Pipeline('fr') # initialize English neural pipeline
doc = nlp("Ce jeu, c'est tres bien.")

#print(doc)

dicts = doc.to_dict() # dicts is List[List[Dict]], representing each token / word in each sentence in the document

for sent in doc.sentences:
    for word in sent.words:
        print(word.text + ':::' + word.upos)

with open('stanza.txt', 'w') as f:
            #f.write("%s\n" % item)
        f.write(str(doc))
'''

import stanza
from collections import Counter
import csv

files = ["la_tap_test.txt"] #, "nostop_le_mystere_des_saints_innocents.txt", "nostop_le_porche_du_mystere_de_la_deuxieme_vertu.txt", "nostop_peguy_eve.txt"]


list_keys = []
list_nums = []
list_nums_unique = []
text_bits = []
perm_pos = []

nlp = stanza.Pipeline('fr') # initialize English neural pipeline
#nlp = stanza.Pipeline(lang='fr', processors='tokenize', tokenize_pretokenized=True)


for f in files:
    # Open our file
    with open(f) as file:
        text_data = file.read()

    testing_list = text_data.splitlines()
    '''
    with open( "splitlines_" + (files[index_num]), "w" ) as q:
        for line in testing:
            q.write(line + '\n')

        index_num += 1
    '''
    #print(testing_list)

    #print(doc)

    word_list = []
    pos_list = []

    final_sents = []
    final_pos = []

    sent_word = []
    #num_list = []

    for x in testing_list:

        doc = nlp(x)

        for sent in doc.sentences:
        #text_bits.append(sent)

            for word in sent.words:
                print(word.text, word.upos)
                word_list.append(word.text)
                pos_list.append(word.upos)


            sent_word.append(word_list)
            final_pos.append(pos_list)

            print(sent_word)
            print(final_pos)

'''
            pos_nums = Counter(pos_list).values() # counts the elements' frequency
               # print(pos_nums)
               # print(pos_keys)


            total_num = str(len(pos_nums))
            list_nums.append(total_num)


            pos_keys = Counter(pos_list).keys()
            q = str(len(pos_keys))
        #q = len(Counter(actual_pos).most_common())
        #print(q)

        #if q != 0:
            list_nums_unique.append(q)

        #list_nums.append(total_num)

        print(len(word_list))
        print(len(pos_list))

    #print(len(list_nums))
        print(len(list_nums_unique))

    #print(list_nums)
        print(list_nums_unique)

        for x in sent_word:
            final_sents.append(x)

        for x in final_pos:
            final_pos.append(x)



    #     perm_pos.append(actual_pos)
    #
    # print(len(perm_pos)) # 1707
    # print(len(text_bits)) #1707 - total nums
    # print(len(list_nums)) #1707 - how many pos
    # print(len(list_nums_unique)) #1707 -
    #doc_data = pickle.dumps(doc)

    # pickle.dump(doc, open( "nlp_" + (files[index_num]) + ".p", "wb" ))
#     index_num += 1


# Output our tagged data into a CSV
# with open('stanza_text_testing.csv', 'w') as csvfile:
#         fieldnames = ['text', 'pos', ]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # writer.writeheader()
        # for word in sent.words:
        #     print(word.text, word.upos)
        #     writer.writerow({'text': word.text, 'pos': word.upos})


    with open('stanza_GITHUB.csv', 'w') as csvfile:
        fieldnames = ['text', 'pos', 'total', 'pos_unique']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        x = 0
        for d in testing_list:
            writer.writerow({'text': final_sents[x], 'pos': final_pos[x], 'total': list_nums[x], 'pos_unique': list_nums_unique[x]})
            x += 1
'''
