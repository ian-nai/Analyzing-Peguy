import stanza
from collections import Counter
import csv
from nltk.tokenize import LineTokenizer

files = ['lines_la_tapisserie_de_sainte_genevieve.txt',
'lines_la_tapisserie_notre_dame.txt',
'lines_le_mystere_de_la_charite_de_jeanne_darc.txt',
'lines_le_mystere_des_saints_innocents.txt',
'lines_le_porche_du_mystere_de_la_deuxieme_vertu.txt',
'lines_eve.txt']


list_keys = []
list_nums = []
list_nums_unique = []
text_bits = []
perm_pos = []

index_num = 0

nlp = stanza.Pipeline('fr') # initialize English neural pipeline

for f in files:
    # Open our file
    with open(f) as file:
        text_data = file.read()

    #testing_list = text_data.splitlines()
        testing_list = LineTokenizer(blanklines='discard').tokenize(text_data)

    final_pos = []

    sent_word = []
    #num_list = []

    for x in testing_list:
        print(x)

        doc = nlp(x)

        for sent in doc.sentences:
            word_list = []
            pos_list = []
            for word in sent.words:
                print(word.text, word.upos)
                word_list.append(word.text)
                pos_list.append(word.upos)




        pos_nums = Counter(pos_list).values() # counts the elements' frequency

        total_num = str(len(pos_nums))
        list_nums.append(total_num)


        sent_word.append(str(word_list))
        final_pos.append(pos_list)


    print(len(sent_word))
    print(len(final_pos))
    print(len(list_nums))

    for x in final_pos:
        print(x)
        pos_keys = Counter(x).keys()
        q = str(len(x))
        list_nums_unique.append(q)

    print(len(list_nums_unique))



    with open(('stanza_' + files[index_num] + '.csv'), 'w') as csvfile:
            fieldnames = ['text', 'pos', 'total', 'pos_unique']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            x = 0
            for d in testing_list:
                writer.writerow({'text': sent_word[x], 'pos': final_pos[x], 'total': list_nums_unique[x], 'pos_unique': list_nums[x]})
                x += 1

    index_num += 1
    list_keys.clear()
    list_nums.clear()
    list_nums_unique.clear()
    text_bits.clear()
    perm_pos.clear()
