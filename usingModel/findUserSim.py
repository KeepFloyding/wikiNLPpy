import sys
import os
sys.path.append(os.getcwd()+"/toolbox")

from helpFilesWiki import readCSV as read, printToCSV as save
from nltkExtraWiki import cleanText
from charToolsWiki import labelText
import numpy as np
import logging
from gensim.models import Phrases,  Word2Vec as word2vec

reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':

	# --------------------------------------------------------------------
	# LOGGING/SET-UP
	# --------------------------------------------------------------------	

	# Logging
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)
	logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
	logging.root.setLevel(level=logging.INFO)
	logger.info("Starting %s" % ' '.join(sys.argv))

	# Inputs
	modelName   = sys.argv[1];
	bigramModel = sys.argv[2];
	themesFile  = sys.argv[3];
	tribeDir   =  sys.argv[4]; 
	
	# Retrieve themes from file
	themes = [];
	with open(themesFile, "r") as file:
		for line in file:
			for item in [' ','\n','\t']:
				newLine = line.replace(item,'');
				line = newLine;

			values = line.split(',');

			for value in values:
				if len(value) > 0:
					themes.append(value.lower());

	logger.info("List of themes to be analysed are : ")
	logger.info(themes)
	logger.info("If any term is not correct, please check the themes file!")

	# Word2Vec Model
	logger.info('Loading Word2Vec model...')
	model = word2vec.load_word2vec_format(modelName,binary=False)

	# Bigram model
	logger.info('Loading bigram model...')
	bigram = Phrases.load(bigramModel)

	# --------------------------------------------------------------------
	# SIMULATION ENGINE
	# --------------------------------------------------------------------	
	
	logger.info('Cycling through each file in the directory ' + tribeDir)
	files = [f for f in os.listdir(tribeDir) if os.path.isfile(os.path.join(tribeDir, f))];

	for tribeFile in files:

		# Creating Directory
		folderName = tribeDir+'/'+tribeFile[0:len(tribeFile)-4]

		if not os.path.exists(folderName):
			os.makedirs(folderName);

		# Loading the tribe data
		logger.info('Loading ' + tribeFile + '...')
		data = read(tribeDir+'/'+tribeFile);

		# --------------------------------------------------------------------
		# CLEANING AND PROCESSING DATA
		# --------------------------------------------------------------------

		# Cleaning and Processing Text
		logger.info('Cleaning data...')
		userName = [];
		name = [];
		descriptions = [];

		for term in data:
			if len(term) > 2:
				userName.append(term[0]);
				name.append(term[1]);
				descriptions.append(" ".join(term[2:len(term)]));

		# Getting rid of apostrophes in text
		newName = [term.replace("'"," ") for term in name]

		# Cleaning text
		clnName = cleanText(newName,'en')
		clnDescr = cleanText(descriptions,'en');

		# Checking for Bigrams 
		logger.info('Checking for bigrams...')
		biDescr = bigram[clnDescr];
		biName = bigram[clnName]

		# -----------------------------------------------------------------------------------------
		# FINDING SIMILARITY
		# -----------------------------------------------------------------------------------------

		# Finding similarity score for each user for each category
		logger.info('Finding similarity score for each category...')
		labels = labelText(biName,model,themes);
		descLabels = labelText(biDescr,model,themes)
 
		# -----------------------------------------------------------------------------------------
		# SAVING FILES TO OUTPUT
		# -----------------------------------------------------------------------------------------

		logger.info('Saving data to csv and numpy dictionaries...')

		# Saving to CSV files

		save(folderName + '/' + 'tribeScoreSummary.csv',[],name,descriptions,userName,labels,descLabels)

		# Saving dictionaries in np format

		np.save(folderName + '/' + 'labels.npy',labels)
		np.save(folderName + '/' + 'descLabels.npy',descLabels)

