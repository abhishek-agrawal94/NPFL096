import nltk
from nltk.corpus import brown
from nltk.probability import ConditionalProbDist, ConditionalFreqDist, ELEProbDist, FreqDist
import operator
from rules import noun_masc, noun_fem, noun_neut, adj_masc, adj_fem, adj_neut, verbs_conditional, verbs_imperative, verbs_indicative, verbs_subjunctive

def get_initial_pos_tag(word):
    dictionary = {'अघ': ['sin', 'fault', 'offense'],
                  'अग्रणी': ['principal', 'chief'],
                  'अघा': ['all', 'whole'],
                  'अग्नीज्वाळा': ['flame'],
                  'अंघोळ': ['bathing']}
    initial_pos_seed = {}
    if word in dictionary:
        # fdist = FreqDist(word.lower() for (word, tag) in brown.tagged_words(tagset='universal'))
        # print(fdist.B())

        cfdist = ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown.tagged_words(tagset='universal'))

        table = {'DET': 0, 'X': 0, 'VERB': 0, 'NOUN': 0, 'ADJ': 0, 'ADP': 0, '.': 0, 'CONJ': 0, 'PRT': 0, 'PRON': 0,
                 'NUM': 0, 'ADV': 0}
        tags = ['DET', 'X', 'VERB', 'NOUN', 'ADJ', 'ADP', '.', 'CONJ', 'PRT', 'PRON', 'NUM', 'ADV']
        for trans in dictionary[word]:
            for tag in tags:
                table[tag] += cfdist[trans].freq(tag)
        for k in table.keys():
            table[k] = table[k] / len(dictionary[word])
        initial_pos_seed[word] = max(table.items(), key=operator.itemgetter(1))[0]

        return initial_pos_seed
    else:
        print("word not available in dictionary")
        return initial_pos_seed



def get_possible_generations(initial_seed):
    possible_generations = {}

    for key, value in initial_seed.items():
        forms = {}
        if value is "NOUN":
            forms.update(noun_masc(key))
            forms.update(noun_fem(key))
            forms.update(noun_neut(key))
        elif value is "ADJ":
            forms.update(adj_masc(key))
            forms.update(adj_fem(key))
            forms.update(adj_neut(key))
        elif value is "VERB":
            forms.update(verbs_subjunctive(key))
            forms.update(verbs_indicative(key))
            forms.update(verbs_imperative(key))
            forms.update(verbs_conditional(key))
        possible_generations[key] = forms

    print(possible_generations)



if __name__=="__main__":
    initial_seed = get_initial_pos_tag("अघ")
    if initial_seed:
        get_possible_generations(initial_seed)
    else:
        print("try another word")

