#!/bin/sh

# Script to train Wikipedia model, October 2016
#
# Written by Andris Piebalgs <andris@fifty.com>
#
# Only input required is name of .xml.bz2 file in var xmlFile
# Please run only in current directory
# Will take entire day or so to run (for whole english wikipedia)
#

# INPUT
xmlFile="wikiIni.xml.bz2"

# OUTPUT
wikiTextDir=$(python genWikiText.py $xmlFile)
bigramDir=$(python findBigrams.py $wikiTextDir)
python trainWikiText.py $wikiTextDir $bigramDir
