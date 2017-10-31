#!/bin/sh
#
# Script to use Wikipedia Model to calculate user affinity for each tribe, October 2016
#
# Written by Andris Piebalgs <andris@fifty.com>
#
# Inputs required:
# Word2Vec Model File Name
# Bigram File Name 
# Themes file name (text file that contains themes to analyse for each user)
# Tribe directory (folder that contains tribe csv files, each containing screen name, user name and description)
#
# Outputs:
# Folders are created in tribe directory that correspond to each csv file. Every user has a dictinary of scores for every theme given in the theme file.
#
# Note, loading the word2vec model may take a long time, ~30 mins for english wikipedia, so make sure you have everything ready
 
# INPUTS
modelFile='/home/andris/pythonFiles/ngramTxtModel.vector'
bigramFile='/home/andris/pythonFiles/bigramCatcher.model'
themesFile='themesList.txt'
tribeFile='tribeFiles'

# COMMAND
python findUserSim.py $modelFile $bigramFile $themesFile $tribeFile

# INPUTS
N_CLUSTER=5
limits=4
themeArray=['fashion','politics','music','news','business','sport','comedy','entertainment','travel','food','luxury']
indCorp=[0,1,2]

#python usingModel/userTribeClassification.py $tribeFile $N_CLUSTER $limits $themeArray $indCorp

#less $tribeFile/tribeCharExam/clusterLabeled.csv