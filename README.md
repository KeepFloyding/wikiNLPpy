# wikiTrainPy: Training Word2Vec model on wikipedia data
 A python library to train and store a word2vec model trained on wiki data. Model includes most common bigrams.

## Getting Started

### Prerequisites

* Python 3.x with Anaconda
* Gensim
* Wikipedia .xml.bz2 file

Wikipedia file can be downloaded from https://dumps.wikimedia.org/backup-index.html
File needs to be of type .xml.bz2 (for storage)

For instance, file can be downloaded with 

```
wget 'https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2'
```

### Training Model

In the trainModel folder, runAll.sh is the script that will launch all relevant python files.
Only input needed is the name of the wikipedia file

```
# INPUT
xmlFile="wikiIni.xml.bz2"

# OUTPUT
wikiTextDir=$(python genWikiText.py $xmlFile)
bigramDir=$(python findBigrams.py $wikiTextDir)
python trainWikiText.py $wikiTextDir $bigramDir
```

* genWikiText.py uses WikiCorpus from gensim to extract text from wikipedia file. All articles are joined and written to text file. 
* findBigrams.py goes through text file and finds the most common bigrams in the text. Bigram model is saved in vector format. 
* trainWikiText.py trains wikiCorpus on Word2Vec after passing model through bigrams. 

End result is a Word2Vec model, saved in a vector format to be loaded and used in another instance. 

### Using model

Here we use the model to determine the similarity of a sentence to a particular theme using the Word2Vec model.

This is done by using the runAll.py file in the usingModel folder. 
The inputs are the wiki file, the bigram model, a text file of themes to examine and a folder that contains csvs of data.

Main Inputs:
1) A trained Word2Vec model
2) A trained phrase colocation model (trained to find bigrams)
3) A .txt file that has a list of all the themes that need to be investigated
4) A folder with CSVs, where each CSV represents a key and a sample of text to analyse

The interests (or themes) are defined in a seperate text file and the similarity of each word in the second column of the csv is used.

```
# INPUTS
modelFile='[/path/to/wikiModel].vector'
bigramFile='[/path/to/bigramModel].model'
themesFile='[/path/to/list/of/themes/].txt'
folderName='[folder_containts_csv_data]'

# COMMAND
python findTextSim.py $modelFile $bigramFile $themesFile $folderName
```

Outputs is a folder for each csv that contains affinity of sample text for every theme. 


