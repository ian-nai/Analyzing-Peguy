import spacy
from spacy_lefff import LefffLemmatizer, POSTagger
#import pickle
import re
from compress_pickle import dump, load

index_num = 0



files = ['simple_test.txt']#"nostop_le_mystere_de_la_charite_de_jeanne_darc.txt", "nostop_le_mystere_des_saints_innocents.txt", "nostop_le_porche_du_mystere_de_la_deuxieme_vertu.txt", "nostop_peguy_eve.txt"]

nlp = spacy.load("fr_dep_news_trf")
# pos = POSTagger()
# french_lemmatizer = LefffLemmatizer(after_melt=True, default=True)
# nlp.add_pipe(pos, name='pos', after='parser')
# nlp.add_pipe(french_lemmatizer, name='lefff', after='pos')

for f in files:
    # Open our file
    with open(f) as file:
        text_data = file.read()


    # Specify the information we want
    doc = nlp(text_data)
    #for d in doc:
     #   print(d.text, d.pos_, d._.melt_tagger, d._.lefff_lemma, d.tag_, d.lemma_)


    #doc_data = pickle.dumps(doc)
    fname1 = ("nlp_" + (files[index_num]) + ".pkl")
    fname2 = ("nlp_" + (files[index_num]) + ".gz")

    dump(doc,fname1)
    dump(doc, fname2)

    index_num += 1
'''
# Output our tagged data into a CSV
with open('text_data.csv', 'w') as csvfile:
    fieldnames = ['text', 'pos', 'melt', 'lefff_lemma', 'tag', 'lemma']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for d in doc:
        if d.pos_ != "SPACE":
            writer.writerow({'text': d.text, 'pos': d.pos_, 'melt': d._.melt_tagger, 'lefff_lemma': d._.lefff_lemma, 'tag': d.tag_, 'lemma': d.lemma_})
'''
