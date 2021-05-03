# Analyzing-Peguy
NLP on works by Peguy. This repository is an outgrowth of the [Non-English NLP Tutorial](https://github.com/ian-nai/Non-English-NLP-Tutorial).

## Getting Started
Install required dependencies:

```
pip3 install -r requirements.txt
```
## Scope
This repository is a starting point for using NLP to analyze and visualize various aspects of the poetry and plays of Charles Péguy. Code may be updated and added as necessary while the project progresses.

## What This Repository Contains
#### CSVs
A collection of .csv files containing data gleaned from analyzing the texts using NLP. The sub-folders in this section contain data for different models that were used to process the texts, the core_news_lg and dep_news_trf models from spaCy and the Stanza French model from Stanford's Stanza library. There is also a folder for data used in visualizing the texts using graphs.

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
#### Tokenized Lines and Sentences
#### Visualizations

