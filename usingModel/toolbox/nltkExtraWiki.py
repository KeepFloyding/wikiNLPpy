# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:11:59 2016
NATURAL LANGUAGE PROCESSING TOOLKIT EXTRA

@author: Andris
"""

from createTokens import preprocess
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
import nltk

def cleanText(text,lang):
    
    stop = get_stop_words(lang)
    p_stemmer = PorterStemmer()
    
    textCln =[];
    
    for tweet in text:
        
        tokens = preprocess(tweet.lower());    
        
        clnTweet = [];    
        
        for word in tokens:
            
            if word not in stop and len(word) > 2 and not word.startswith('http'):
                
                clnTweet.append((word));
        
        textCln.append(clnTweet)
        
    return textCln

# Function that goes through multiple documents and returns most used words, hashtags and mentions
# Inputs are text and number of words desired
# Outputs are uni-,bi-,tri- grams, hashtags and mentions

def simpleWordCount(clnText,Nsave):
    
    # Arranging into list
    
    wordList = [];
    for tweet in clnText:
        
        for word in tweet:
            wordList.append(word);
        
    # ---------------------------------------------------------------------------
    # FINDING/COUNTING HASHTAGS
    # ---------------------------------------------------------------------------
    
    hashtag = [];
    mentions = [];
    
    for word in wordList:
        
        if word.startswith('#'):        
            hashtag.append(word);
            
        if word.startswith('@'):        
            mentions.append(word);
    
    cntHashtag = nltk.FreqDist(hashtag);
    cntMentions = nltk.FreqDist(mentions);
    
    commonHashtags = cntHashtag.most_common(Nsave)
    commonMentions = cntMentions.most_common(Nsave) ;
    
    # ---------------------------------------------------------------------------
    # WORD (UNI-,BI- AND TRI-) GRAM COUNT
    # ---------------------------------------------------------------------------
    
    bigrams  = nltk.ngrams(wordList,2)
    trigrams = nltk.ngrams(wordList,3)
    
    cntWord = nltk.FreqDist(wordList);
    cntBigram = nltk.FreqDist(bigrams);
    cntTrigram = nltk.FreqDist(trigrams);
    
    mostCommon = cntWord.most_common(Nsave);
    mostCommonBi = cntBigram.most_common(Nsave);
    mostCommonTri = cntTrigram.most_common(Nsave);
    
    return mostCommon,mostCommonBi,mostCommonTri, commonHashtags, commonMentions
    
