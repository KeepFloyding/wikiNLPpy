import logging
import sys
import os.path
from gensim.models.word2vec import LineSentence
from gensim.models import Phrases, Word2Vec

if __name__ == '__main__':

	# ------------------------------------------------------------------
    	# LOGGING/SET-UP
    	# ------------------------------------------------------------------
	
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)
	logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
	logging.root.setLevel(level=logging.INFO)
	logger.info("Starting %s" % ' '.join(sys.argv))

	# Find the sentences
	logger.info('Accessing sentences with gensim.LineSentence...')
	fname = sys.argv[1]
	sentences = LineSentence(fname);

	# ------------------------------------------------------------------
    	# LOGGING/SET-UP
    	# ------------------------------------------------------------------
	
	# Train for bigrams
	logger.info('Training for bigrams...')
	bigram = Phrases(sentences);
	logger.info('Saving models...')
	bigramFile = str(fname[0:len(fname)-8])+'_bigramCatcher.model' 
	bigram.save(bigramFile)

	logger.info('All done! Bigram algorithm ran succesfully. Closing program')
	print bigramFile
