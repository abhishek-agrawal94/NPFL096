import nltk
from nltk.corpus import brown
from nltk.probability import ConditionalProbDist, ConditionalFreqDist, ELEProbDist, FreqDist
import operator
from difflib import get_close_matches
from rules import noun_masc, noun_fem, noun_neut, adj_masc, adj_fem, adj_neut, verbs_conditional, verbs_imperative, verbs_indicative, verbs_subjunctive

def get_initial_pos_tag(word):
    dictionary = {'अघ': ['sin', 'fault', 'offense'],
                  'अग्रणी': ['principal', 'chief'],
                  'अघा': ['all', 'whole'],
                  'अग्नीज्वाळा': ['flame'],
                  'अंघोळ': ['bathing'],
                  'अघाडी': ['the front', 'the van', 'before'],
                  'अघोरी': ['vile', 'horrible', 'loathsome'],
                  'अचकट': ['indecent', 'foul', 'obscene'],
                  'अचपळ': ['wild', 'restless', 'lively'],
                  'अचल': ['a mountain', 'fixed'],
                  'अजन्म':['unborn', 'eternal'],
                  'अजाणता': ['ignorant', 'simple'],
                  'अटपविणें': ['dispose of', 'gather together'],
                  'अट': ['hindrance', 'condition', 'obstinacy'],
                  'आठवण': ['recollection', 'memory'],
                  'अडथळणें': ['stop', 'hinder'],
                  'अंत:करण': ['the heart', 'the conscience'],
                  'अंतिम': ['final', 'last'],
                  'अंथरणें': ['spread', 'overspread'],
                  'अदावत': ['enmity', 'hatred', 'spite', 'grudge'],
                  'अधिक': ['more', 'greater', 'above'],
                  'अनपेक्शित': ['undesired', 'unwished', 'unwanted'],
                  'अवतार': ['incarnation'],
                  'अंश': ['a part', 'a fraction'],
                  'असंतोष': ['displeasure', 'discontent', 'unrest'],
                  'इषारा': ['a hint', 'a signal'],
                  'उघडा': ['open', 'uncovered', 'clear', 'naked', 'public']}
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
    return possible_generations



if __name__=="__main__":
    initial_seed = get_initial_pos_tag("अंघोळ")
    if initial_seed:
        possible_generations = get_possible_generations(initial_seed)
    else:
        print("try another word")
    corpus_unique_tokens = set()
    with open("data/mr.tok") as f:
        text = f.read()
    lines = text.split("\n")
    for line in lines:
        corpus_unique_tokens.update(line.split(" "))
    with open("data/mr_1.tok") as f:
        text = f.read()
    lines = text.split("\n")
    for line in lines:
        corpus_unique_tokens.update(line.split(" "))
    with open("data/mr_2.tok") as f:
        text = f.read()
    lines = text.split("\n")
    for line in lines:
        corpus_unique_tokens.update(line.split(" "))
    #print(corpus_unique_tokens)

    '''Not exactly weighted levenshtein distance but a similar concept as the paper for correcting generated analysis'''
    close_matches = get_close_matches("अंघोळ", list(corpus_unique_tokens), n=6, cutoff=0.7)
    print(close_matches)
    for key, value in possible_generations.items():
        possible_matches = close_matches
        for item in close_matches:
            if item in value.keys():
                possible_matches.remove(item)
        #print(possible_matches)
        post_distance={}

        for item in value.keys():
            if possible_matches:
                new_term = get_close_matches(item, possible_matches, n=1, cutoff=0.8)
                if new_term:
                    post_distance[new_term[0]] = possible_generations[key][item]
                else:
                    post_distance[item] = possible_generations[key][item]

        print(post_distance)
