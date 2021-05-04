# Analyzing-Peguy
NLP on works by Peguy. This repository is an outgrowth of the [Non-English NLP Tutorial](https://github.com/ian-nai/Non-English-NLP-Tutorial).
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/3/32/Charles_P%C3%A9guy_by_Eug%C3%A8ne_Pirou.jpg" height="426" width="272"/>
</p>
## Getting Started
Install required dependencies:

```
pip3 install -r requirements.txt
```
## Scope
This repository is a starting point for using NLP to analyze and visualize various aspects of the poetry and plays of Charles Péguy. Code may be updated and added as necessary while the project progresses.

## What This Repository Contains
#### CSVs
A collection of .csv files containing data gleaned from analyzing the texts using NLP. The sub-folders in this section contain data for different models that were used to process the texts, the fr_core_news_lg and fr_dep_news_trf models from spaCy and the Stanza French model from Stanford's Stanza library. There is also a folder for data used in visualizing the texts using graphs.

#### Original Texts
The original texts of six works by Péguy:
Four poems:
* (1912). Le Porche du Mystère de la Deuxième Vertu.
* (1913). La Tapisserie de Sainte Geneviève et de Jeanne d'Arc.
* (1913). La Tapisserie de Notre-Dame.
* (1913). Ève.

And two plays:
* (1910). Le Mystère de la Charité de Jeanne d'Arc.
* (1912). Le Mystère des Saints Innocents.

#### Pickle Files
These are pickled NLP models (using the fr_dep_news_trf spaCy model) of the original texts, broken up into smaller chunks to avoid file size limitations.

#### Python Code
The Python files contained here perform the NLP used to generate the CSVs and visualizations. The files are as follows:
* csv_fr_core_news_lg.py - Run the spaCy csv_fr_core_news_lg model on the text(s) included in the code and output the results to a CSV file.
* csv_fr_dep_news_trf.py - Run the spaCy csv_fr_dep_news_trf model on the text(s) included in the code and output the results to a CSV file.
* csv_stanza.py - Run Stanford's Stanza library on the text(s) included in the code and output the results to a .csv file.
* line_tokenize_remove_stopwords.py - Tokenize the texts by lines and remove stopwords.
* liv_rix_readability_test.py - Perform the Liv and Rix readability tests on the text(s) included in the code and output the results in the terminal.
* make_pickles.py - Create the pickle files for uploading to GitHub.
* sentence_tokenize_remove_stopwords.py - Tokenize texts by sentences and remove stopwords.
* syllable_counting.py - An (imeprfect) algorithm to count syllables in French text.
* visualizations.py - Code to generate various visualizations of textual data using matplotlib.

#### Tokenized Lines and Sentences
These folders contain text files of the texts tokenized into lines and sentences.

#### Visualizations
Visualizations of textual data in PNG and interactive HTML/JS format. This folder may be added to in the future.
