import spacy
from spacy_lefff import LefffLemmatizer, POSTagger
import re
from compress_pickle import dump, load

index_num = 0


# Note: creating this many pickle files at once will be very slow
files = ['nostop_le_mystere_de_la_charite_de_jeanne_darc.txt', "nostop_le_mystere_des_saints_innocents.txt", "nostop_le_porche_du_mystere_de_la_deuxieme_vertu.txt", "nostop_peguy_eve.txt"]

nlp = spacy.load("fr_dep_news_trf")


for f in files:
    # Open our file
    with open(f) as file:
        text_data = file.read()


    # Specify the information we want
    doc = nlp(text_data)


    #doc_data = pickle.dumps(doc)
    fname1 = ("nlp_" + (files[index_num]) + ".pkl")
    fname2 = ("nlp_" + (files[index_num]) + ".gz")

    dump(doc,fname1)
    dump(doc, fname2)

    index_num += 1
