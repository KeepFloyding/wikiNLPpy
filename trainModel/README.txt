Training Wikipedia Model

runAll.sh is the script that will launch all python files.
1) Grabbing text from .xml file.
2) Search for bigrams in the text.
3) Run text through bigram checker and train model.

Input needed in script is the file name of the .xml.bz2 Wikipedia file.
This can be downloaded from :
https://dumps.wikimedia.org/backup-index.html

e.g. wget 'https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract.xml'

# Once edited, launch script with
./runAll.sh

# If you only need to launch a single python script then just copy and paste the correspondong line from the shell script,
make sure the inputs are correct.

Details

