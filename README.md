# NPFL096

Assignment for the class NPFL096

---

Run the program by running tagger.py. The program first finds the initial POS tag or the seed tag for any marathi word. It does this by looking up the word in a Marathi-English bilingual dictionary a part of which has been manually added to the file tagger.py. It searches the English translations of the words in the Brown corpus and gets the probabilities 
of POS tags given the english words. An average of all the probabilities over all the translations is taken and the POS tag corresponding to the maximum probability is chosen as the initial tag for the Marathi word.

A set of inflection rules have been writing in the file rules.py. The grammar rules have been written using a reference of the two grammar books present in the repository. Using these rules we get a list of marathi inflected word forms with their corresponding morphological analysis. Then using the unique tokens from 3 different monolingual Marathi corpora, we search for a few words which are quite similar to our word. We compare these similar words with the various inflected forms that we generated previously and if we have the similarity of any of those two words greater than 0.8, then we substitute the word from the corpora in place of the word we generated as our generations might have some faults. To calculate the similarity of words, the python library difflib has been used.
