#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import logging
import os.path
import sys
import multiprocessing
 
from gensim.models import Word2Vec, Phrases
from gensim.models.word2vec import LineSentence
 
if __name__ == '__main__':

    # ------------------------------------------------------------------
    # LOGGING/SET-UP
    # ------------------------------------------------------------------
    
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("Starting %s" % ' '.join(sys.argv))
	
    # Inputs
    wikiTextFile = sys.argv[1];
    bigramFile = sys.argv[2];
	
    # Load Bigram File
    logger.info('Loading the bigram model...')
    bigram = Phrases.load(bigramFile)

    # ------------------------------------------------------------------
    # FIND SENTENCES, LOOK FOR BIGRAMS AND TRAIN TEXT
    # ------------------------------------------------------------------
	
    # Find the sentences
    logger.info('Accessing sentences with gensim.LineSentence...')
    sentences = LineSentence(wikiTextFile);

    # Analyse text for bigrams 
    logger.info('Looking in text for bigrams...')
    newSentences = bigram[sentences];
	
    # Training text
    model = Word2Vec(newSentences, size=400, window=5, min_count=5,
            workers=multiprocessing.cpu_count())
 
    #model.init_sims(replace=True)
    model.save('Word2VecModel_'+wikiTextFile[0:len(wikiTextFile)-4]+'.model')
    model.save_word2vec_format('Word2VecModel_'+wikiTextFile[0:len(wikiTextFile)-4]+'.vector', binary=False)
