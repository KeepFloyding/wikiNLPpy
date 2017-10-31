#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import os.path 
import logging
import sys
from gensim.corpora import WikiCorpus
 
if __name__ == '__main__':

    # ------------------------------------------------------------------
    # LOGGING/SET-UP
    # ------------------------------------------------------------------
	
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("Starting %s" % ' '.join(sys.argv))
 
    input = sys.argv[1];
    output = str(input[0:len(input)-8]) + '.txt' 
    fileWrite = open(output, 'w')
 
    # ------------------------------------------------------------------
    # EXTRACTING WIKIPEDIA TEXTS
    # ------------------------------------------------------------------
	 
    it = 0 
    
    # Use WikiCorpus to extract text from .xml.bz2 file
    wiki = WikiCorpus(input, lemmatize=False, dictionary={})
    
    for text in wiki.get_texts():
	
	# Write text to file
        fileWrite.write(' '.join(text) + "\n")
		
	# Update progress
        it += 1
        if (it % 10000 == 0):
            logger.info("Saved " + str(it) + " articles")
 
    # Close file
    fileWrite.close()
    print output
