

def noun_masc(lemma):
    forms = {}
    forms[lemma] = [lemma, "NOUN", "masc", "sing", "nom"]
    if lemma[-1] in "ाआ":
        forms[lemma[:-1] + "े"] = [lemma, "NOUN", "masc", "plur", "nom"]
        forms[lemma + "ला"] = [lemma, "NOUN", "masc", "sing", "acc"]
        forms[lemma + "ंना"] = [lemma, "NOUN", "masc", "plur", "acc"]
        forms[lemma + "नें"] = [lemma, "NOUN", "masc", "sing", "inst"]
        forms[lemma + "ंनीं"] = [lemma, "NOUN", "masc", "plur", "inst"]
        forms[lemma + "ला"] = [lemma, "NOUN", "masc", "sing", "dat"]
        forms[lemma + "ंना"] = [lemma, "NOUN", "masc", "plur", "dat"]
        forms[lemma + "हून"] = [lemma, "NOUN", "masc", "sing", "abl"]
        forms[lemma + "ंहून"] = [lemma, "NOUN", "masc", "plur", "abl"]
        forms[lemma + "चा"] = [lemma, "NOUN", "masc", "sing", "gen"]
        forms[lemma + "ंचा"] = [lemma, "NOUN", "masc", "plur", "gen"]
        forms[lemma + "त"] = [lemma, "NOUN", "masc", "sing", "loc"]
        forms[lemma + "त"] = [lemma, "NOUN", "masc", "plur", "loc"]
        forms[lemma] = [lemma, "NOUN", "masc", "sing", "voc"]
        forms[lemma + "ंनों"] = [lemma, "NOUN", "masc", "plur", "voc"]
    else:
        forms[lemma] = [lemma, "NOUN", "masc", "plur", "nom"]
        forms[lemma + "ाला"] = [lemma, "NOUN", "masc", "sing", "acc"]
        forms[lemma + "ांना"] = [lemma, "NOUN", "masc", "plur", "acc"]
        forms[lemma + "ानें"] = [lemma, "NOUN", "masc", "sing", "inst"]
        forms[lemma + "ांनीं"] = [lemma, "NOUN", "masc", "plur", "inst"]
        forms[lemma + "ाला"] = [lemma, "NOUN", "masc", "sing", "dat"]
        forms[lemma + "ांना"] = [lemma, "NOUN", "masc", "plur", "dat"]
        forms[lemma + "ाहून"] = [lemma, "NOUN", "masc", "sing", "abl"]
        forms[lemma + "ांहून"] = [lemma, "NOUN", "masc", "plur", "abl"]
        forms[lemma + "ाचा"] = [lemma, "NOUN", "masc", "sing", "gen"]
        forms[lemma + "ांचा"] = [lemma, "NOUN", "masc", "plur", "gen"]
        forms[lemma + "ात"] = [lemma, "NOUN", "masc", "sing", "loc"]
        forms[lemma + "ात"] = [lemma, "NOUN", "masc", "plur", "loc"]
        forms[lemma + "ा"] = [lemma, "NOUN", "masc", "sing", "voc"]
        forms[lemma + "ांनों"] = [lemma, "NOUN", "masc", "plur", "voc"]

    return forms




def noun_fem(lemma):
    forms = {}
    forms[lemma] = [lemma, "NOUN", "fem", "sing", "nom"]
    forms[lemma + "ी"] = [lemma, "NOUN", "fem", "plur", "nom"]
    forms[lemma + "ीला"] = [lemma, "NOUN", "fem", "sing", "acc"]
    forms[lemma + "ींना"] = [lemma, "NOUN", "fem", "plur", "acc"]
    forms[lemma + "ीनें"] = [lemma, "NOUN", "fem", "sing", "inst"]
    forms[lemma + "ींनीं"] = [lemma, "NOUN", "fem", "plur", "inst"]
    forms[lemma + "ीला"] = [lemma, "NOUN", "fem", "sing", "dat"]
    forms[lemma + "ींना"] = [lemma, "NOUN", "fem", "plur", "dat"]
    forms[lemma + "ीहून"] = [lemma, "NOUN", "fem", "sing", "abl"]
    forms[lemma + "ींहून"] = [lemma, "NOUN", "fem", "plur", "abl"]
    forms[lemma + "ीचा"] = [lemma, "NOUN", "fem", "sing", "gen"]
    forms[lemma + "ींचा"] = [lemma, "NOUN", "fem", "plur", "gen"]
    forms[lemma + "ीत"] = [lemma, "NOUN", "fem", "sing", "loc"]
    forms[lemma + "ींत"] = [lemma, "NOUN", "fem", "plur", "loc"]
    forms[lemma + "ी"] = [lemma, "NOUN", "fem", "sing", "voc"]
    forms[lemma + "ींनों"] = [lemma, "NOUN", "fem", "plur", "voc"]
    return forms


def noun_neut(lemma):
    forms = {}
    if lemma[-1] in "ीईेए":
        forms[lemma] = [lemma, "NOUN", "neut", "sing", "nom"]
        forms[lemma[:-1] + "्यें"] = [lemma, "NOUN", "neut", "plur", "nom"]
        forms[lemma + "ीला"] = [lemma, "NOUN", "neut", "sing", "acc"]
        forms[lemma + "्यांना"] = [lemma, "NOUN", "neut", "plur", "acc"]
        forms[lemma + "्यानें"] = [lemma, "NOUN", "neut", "sing", "inst"]
        forms[lemma + "्यांनीं"] = [lemma, "NOUN", "neut", "plur", "inst"]
        forms[lemma + "्याला"] = [lemma, "NOUN", "neut", "sing", "dat"]
        forms[lemma + "्यांला-ना"] = [lemma, "NOUN", "neut", "plur", "dat"]
        forms[lemma + "्याहून"] = [lemma, "NOUN", "neut", "sing", "abl"]
        forms[lemma + "्यांहून"] = [lemma, "NOUN", "neut", "plur", "abl"]
        forms[lemma + "्याचा"] = [lemma, "NOUN", "neut", "sing", "gen"]
        forms[lemma + "्यांचा"] = [lemma, "NOUN", "neut", "plur", "gen"]
        forms[lemma + "्यात"] = [lemma, "NOUN", "neut", "sing", "loc"]
        forms[lemma + "्यांत"] = [lemma, "NOUN", "neut", "plur", "loc"]
        forms[lemma + "्या"] = [lemma, "NOUN", "neut", "sing", "voc"]
        forms[lemma + "्यांनों"] = [lemma, "NOUN", "neut", "plur", "voc"]
    else:
        forms[lemma] = [lemma, "NOUN", "neut", "sing", "nom"]
        forms[lemma] = [lemma, "NOUN", "masc", "plur", "nom"]
        forms[lemma + "ाला"] = [lemma, "NOUN", "masc", "sing", "acc"]
        forms[lemma + "ांना"] = [lemma, "NOUN", "masc", "plur", "acc"]
        forms[lemma + "ानें"] = [lemma, "NOUN", "masc", "sing", "inst"]
        forms[lemma + "ांनीं"] = [lemma, "NOUN", "masc", "plur", "inst"]
        forms[lemma + "ाला"] = [lemma, "NOUN", "masc", "sing", "dat"]
        forms[lemma + "ांना"] = [lemma, "NOUN", "masc", "plur", "dat"]
        forms[lemma + "ाहून"] = [lemma, "NOUN", "masc", "sing", "abl"]
        forms[lemma + "ांहून"] = [lemma, "NOUN", "masc", "plur", "abl"]
        forms[lemma + "ाचा"] = [lemma, "NOUN", "masc", "sing", "gen"]
        forms[lemma + "ांचा"] = [lemma, "NOUN", "masc", "plur", "gen"]
        forms[lemma + "ात"] = [lemma, "NOUN", "masc", "sing", "loc"]
        forms[lemma + "ात"] = [lemma, "NOUN", "masc", "plur", "loc"]
        forms[lemma + "ा"] = [lemma, "NOUN", "masc", "sing", "voc"]
        forms[lemma + "ांनों"] = [lemma, "NOUN", "masc", "plur", "voc"]
    return forms

def adj_masc(lemma):
    forms = {}
    forms[lemma] = [lemma, "ADJ", "masc", "sing", "nom"]
    if lemma[-1] in "ाआ":
        forms[lemma[:-1] + "े"] = [lemma, "ADJ", "masc", "plur", "nom"]
        forms[lemma] = [lemma, "ADJ", "masc", "sing", "acc"]
        forms[lemma + "े"] = [lemma, "ADJ", "masc", "plur", "acc"]
        forms[lemma + "्यानें"] = [lemma, "ADJ", "masc", "sing", "inst"]
        forms[lemma + "्यानीं"] = [lemma, "ADJ", "masc", "plur", "inst"]
        forms[lemma + "्याला"] = [lemma, "ADJ", "masc", "sing", "dat"]
        forms[lemma + "्यांना-ला"] = [lemma, "ADJ", "masc", "plur", "dat"]
        forms[lemma + "्याहून"] = [lemma, "ADJ", "masc", "sing", "abl"]
        forms[lemma + "्यांहून"] = [lemma, "ADJ", "masc", "plur", "abl"]
        forms[lemma + "्याचा"] = [lemma, "ADJ", "masc", "sing", "gen"]
        forms[lemma + "्यांचा"] = [lemma, "ADJ", "masc", "plur", "gen"]
        forms[lemma + "्यात"] = [lemma, "ADJ", "masc", "sing", "loc"]
        forms[lemma + "्यात"] = [lemma, "ADJ", "masc", "plur", "loc"]
        forms[lemma + "्या"] = [lemma, "ADJ", "masc", "sing", "voc"]
        forms[lemma + "्यांनों"] = [lemma, "ADJ", "masc", "plur", "voc"]
    else:
        forms[lemma] = [lemma, "ADJ", "masc", "plur", "nom"]
        forms[lemma + "ाला"] = [lemma, "ADJ", "masc", "sing", "acc"]
        forms[lemma + "ांना"] = [lemma, "ADJ", "masc", "plur", "acc"]
        forms[lemma + "ानें"] = [lemma, "ADJ", "masc", "sing", "inst"]
        forms[lemma + "ांनीं"] = [lemma, "ADJ", "masc", "plur", "inst"]
        forms[lemma + "ाला"] = [lemma, "ADJ", "masc", "sing", "dat"]
        forms[lemma + "ांना"] = [lemma, "ADJ", "masc", "plur", "dat"]
        forms[lemma + "ाहून"] = [lemma, "ADJ", "masc", "sing", "abl"]
        forms[lemma + "ांहून"] = [lemma, "ADJ", "masc", "plur", "abl"]
        forms[lemma + "ाचा"] = [lemma, "ADJ", "masc", "sing", "gen"]
        forms[lemma + "ांचा"] = [lemma, "ADJ", "masc", "plur", "gen"]
        forms[lemma + "ात"] = [lemma, "ADJ", "masc", "sing", "loc"]
        forms[lemma + "ात"] = [lemma, "ADJ", "masc", "plur", "loc"]
        forms[lemma + "ा"] = [lemma, "ADJ", "masc", "sing", "voc"]
        forms[lemma + "ांनों"] = [lemma, "ADJ", "masc", "plur", "voc"]
    return forms


def adj_fem(lemma):
    forms = {}
    forms[lemma] = [lemma, "ADJ", "fem", "sing", "nom"]
    if lemma[-1] in "ईी":
        forms[lemma[:-1] + "्या"] = [lemma, "ADJ", "fem", "plur", "nom"]
        forms[lemma] = [lemma, "ADJ", "fem", "sing", "acc"]
        forms[lemma + "्या"] = [lemma, "ADJ", "fem", "plur", "acc"]
        forms[lemma + "नें"] = [lemma, "ADJ", "fem", "sing", "inst"]
        forms[lemma + "्यांनीं"] = [lemma, "ADJ", "fem", "plur", "inst"]
        forms[lemma + "ला"] = [lemma, "ADJ", "fem", "sing", "dat"]
        forms[lemma + "्यांना-ला"] = [lemma, "ADJ", "fem", "plur", "dat"]
        forms[lemma + "्याहून"] = [lemma, "ADJ", "fem", "sing", "abl"]
        forms[lemma + "्यांहून"] = [lemma, "ADJ", "fem", "plur", "abl"]
        forms[lemma + "ची"] = [lemma, "ADJ", "fem", "sing", "gen"]
        forms[lemma + "्यांचा"] = [lemma, "ADJ", "fem", "plur", "gen"]
        forms[lemma + "ींत"] = [lemma, "ADJ", "fem", "sing", "loc"]
        forms[lemma + "्यांत"] = [lemma, "ADJ", "fem", "plur", "loc"]
        forms[lemma + "े"] = [lemma, "ADJ", "fem", "sing", "voc"]
        forms[lemma + "्यांनों"] = [lemma, "ADJ", "fem", "plur", "voc"]
    else:
        forms[lemma] = [lemma, "ADJ", "fem", "plur", "nom"]
        forms[lemma + "ाला"] = [lemma, "ADJ", "fem", "sing", "acc"]
        forms[lemma + "ांना"] = [lemma, "ADJ", "fem", "plur", "acc"]
        forms[lemma + "ानें"] = [lemma, "ADJ", "fem", "sing", "inst"]
        forms[lemma + "ांनीं"] = [lemma, "ADJ", "fem", "plur", "inst"]
        forms[lemma + "ाला"] = [lemma, "ADJ", "fem", "sing", "dat"]
        forms[lemma + "ांना"] = [lemma, "ADJ", "fem", "plur", "dat"]
        forms[lemma + "ाहून"] = [lemma, "ADJ", "fem", "sing", "abl"]
        forms[lemma + "ांहून"] = [lemma, "ADJ", "fem", "plur", "abl"]
        forms[lemma + "ाचा"] = [lemma, "ADJ", "fem", "sing", "gen"]
        forms[lemma + "ांचा"] = [lemma, "ADJ", "fem", "plur", "gen"]
        forms[lemma + "ात"] = [lemma, "ADJ", "fem", "sing", "loc"]
        forms[lemma + "ात"] = [lemma, "ADJ", "fem", "plur", "loc"]
        forms[lemma + "ा"] = [lemma, "ADJ", "fem", "sing", "voc"]
        forms[lemma + "ांनों"] = [lemma, "ADJ", "fem", "plur", "voc"]
    return forms


def adj_neut(lemma):
    forms = {}
    forms[lemma] = [lemma, "ADJ", "neut", "sing", "nom"]
    if lemma[-1] in "एंें":
        forms[lemma[:-1] + "ी"] = [lemma, "ADJ", "neut", "plur", "nom"]
        forms[lemma] = [lemma, "ADJ", "neut", "sing", "acc"]
        forms[lemma[:-1] + "ी"] = [lemma, "ADJ", "neut", "plur", "acc"]
        forms[lemma + "्यानें"] = [lemma, "ADJ", "neut", "sing", "inst"]
        forms[lemma + "्यानीं"] = [lemma, "ADJ", "neut", "plur", "inst"]
        forms[lemma + "्याला"] = [lemma, "ADJ", "neut", "sing", "dat"]
        forms[lemma + "्यांना-ला"] = [lemma, "ADJ", "neut", "plur", "dat"]
        forms[lemma + "्याहून"] = [lemma, "ADJ", "neut", "sing", "abl"]
        forms[lemma + "्यांहून"] = [lemma, "ADJ", "neut", "plur", "abl"]
        forms[lemma + "्याचा"] = [lemma, "ADJ", "neut", "sing", "gen"]
        forms[lemma + "्यांचा"] = [lemma, "ADJ", "neut", "plur", "gen"]
        forms[lemma + "्यात"] = [lemma, "ADJ", "neut", "sing", "loc"]
        forms[lemma + "्यात"] = [lemma, "ADJ", "neut", "plur", "loc"]
        forms[lemma + "्या"] = [lemma, "ADJ", "neut", "sing", "voc"]
        forms[lemma + "्यांनों"] = [lemma, "ADJ", "neut", "plur", "voc"]
    else:
        forms[lemma] = [lemma, "ADJ", "neut", "plur", "nom"]
        forms[lemma + "ाला"] = [lemma, "ADJ", "neut", "sing", "acc"]
        forms[lemma + "ांना"] = [lemma, "ADJ", "neut", "plur", "acc"]
        forms[lemma + "ानें"] = [lemma, "ADJ", "neut", "sing", "inst"]
        forms[lemma + "ांनीं"] = [lemma, "ADJ", "neut", "plur", "inst"]
        forms[lemma + "ाला"] = [lemma, "ADJ", "neut", "sing", "dat"]
        forms[lemma + "ांना"] = [lemma, "ADJ", "neut", "plur", "dat"]
        forms[lemma + "ाहून"] = [lemma, "ADJ", "neut", "sing", "abl"]
        forms[lemma + "ांहून"] = [lemma, "ADJ", "neut", "plur", "abl"]
        forms[lemma + "ाचा"] = [lemma, "ADJ", "neut", "sing", "gen"]
        forms[lemma + "ांचा"] = [lemma, "ADJ", "neut", "plur", "gen"]
        forms[lemma + "ात"] = [lemma, "ADJ", "neut", "sing", "loc"]
        forms[lemma + "ात"] = [lemma, "ADJ", "neut", "plur", "loc"]
        forms[lemma + "ा"] = [lemma, "ADJ", "neut", "sing", "voc"]
        forms[lemma + "ांनों"] = [lemma, "ADJ", "neut", "plur", "voc"]
    return forms

def verbs_indicative(lemma):
    forms = {}
    forms[lemma + "तों"] = [lemma, "VERB", "masc", "sing", "ind", "pres", "p1"]
    forms[lemma + "तोस"] = [lemma, "VERB", "masc", "sing", "ind", "pres", "p2"]
    forms[lemma + "तो"] = [lemma, "VERB", "masc", "sing", "ind", "pres", "p3"]
    forms[lemma + "तें"] = [lemma, "VERB", "fem", "sing", "ind", "pres", "p1"]
    forms[lemma + "तेस"] = [lemma, "VERB", "fem", "sing", "ind", "pres", "p2"]
    forms[lemma + "ते"] = [lemma, "VERB", "fem", "sing", "ind", "pres", "p3"]
    forms[lemma + "तें"] = [lemma, "VERB", "neut", "sing", "ind", "pres", "p1"]
    forms[lemma + "तेंस"] = [lemma, "VERB", "neut", "sing", "ind", "pres", "p2"]
    forms[lemma + "तें"] = [lemma, "VERB", "neut", "sing", "ind", "pres", "p3"]
    forms[lemma + "तों"] = [lemma, "VERB", "masc|fem|neut", "plur", "ind", "pres", "p1"]
    forms[lemma + "तां"] = [lemma, "VERB", "masc|fem|neut", "plur", "ind", "pres", "p2"]
    forms[lemma + "तात"] = [lemma, "VERB", "masc|fem|neut", "plur", "ind", "pres", "p3"]
    forms[lemma + "लों"] = [lemma, "VERB", "masc", "sing", "ind", "past", "p1"]
    forms[lemma + "लास"] = [lemma, "VERB", "masc", "sing", "ind", "past", "p2"]
    forms[lemma + "ला"] = [lemma, "VERB", "masc", "sing", "ind", "past", "p3"]
    forms[lemma + "लें"] = [lemma, "VERB", "fem", "sing", "ind", "past", "p1"]
    forms[lemma + "लीस"] = [lemma, "VERB", "fem", "sing", "ind", "past", "p2"]
    forms[lemma + "ली"] = [lemma, "VERB", "fem", "sing", "ind", "past", "p3"]
    forms[lemma + "लें"] = [lemma, "VERB", "neut", "sing", "ind", "past", "p1"]
    forms[lemma + "लेंस"] = [lemma, "VERB", "neut", "sing", "ind", "past", "p2"]
    forms[lemma + "लें"] = [lemma, "VERB", "neut", "sing", "ind", "past", "p3"]
    forms[lemma + "लों"] = [lemma, "VERB", "masc|fem|neut", "plur", "ind", "past", "p1"]
    forms[lemma + "लां"] = [lemma, "VERB", "masc|fem|neut", "plur", "ind", "past", "p2"]
    forms[lemma + "ले"] = [lemma, "VERB", "masc", "plur", "ind", "past", "p3"]
    forms[lemma + "ल्या"] = [lemma, "VERB", "fem", "plur", "ind", "past", "p3"]
    forms[lemma + "लीं"] = [lemma, "VERB", "neut", "plur", "ind", "past", "p3"]

    forms[lemma + "ेन"] = [lemma, "VERB", "masc|fem|neut", "sing", "ind", "fut", "p1"]
    forms[lemma + "शील"] = [lemma, "VERB", "masc|fem|neut", "sing", "ind", "fut", "p2"]
    forms[lemma + "ेल"] = [lemma, "VERB", "masc|fem|neut", "sing", "ind", "fut", "p3"]
    forms[lemma + "ूं"] = [lemma, "VERB", "masc|fem|neut", "plur", "ind", "fut", "p1"]
    forms[lemma + "ाल"] = [lemma, "VERB", "masc|fem|neut", "plur", "ind", "fut", "p2"]
    forms[lemma + "तील"] = [lemma, "VERB", "masc|fem|neut", "plur", "ind", "fut", "p3"]

    forms[lemma + "ें"] = [lemma, "VERB", "masc|fem|neut", "sing", "ind", "past-hab", "p1"]
    forms[lemma + "ेस"] = [lemma, "VERB", "masc|fem|neut", "sing", "ind", "past-hab", "p2"]
    forms[lemma + "े"] = [lemma, "VERB", "masc|fem|neut", "sing", "ind", "past-hab", "p3"]
    forms[lemma + "ूं"] = [lemma, "VERB", "masc|fem|neut", "plur", "ind", "past-hab", "p1"]
    forms[lemma + "ां"] = [lemma, "VERB", "masc|fem|neut", "plur", "ind", "past-hab", "p2"]
    forms[lemma + "त"] = [lemma, "VERB", "masc|fem|neut", "plur", "ind", "past-hab", "p3"]

    return forms


def verbs_conditional(lemma):
    forms = {}
    forms[lemma + "तों"] = [lemma, "VERB", "masc", "sing", "cond", "pres", "p1"]
    forms[lemma + "तास"] = [lemma, "VERB", "masc", "sing", "cond", "pres", "p2"]
    forms[lemma + "ता"] = [lemma, "VERB", "masc", "sing", "cond", "pres", "p3"]
    forms[lemma + "तें"] = [lemma, "VERB", "fem", "sing", "cond", "pres", "p1"]
    forms[lemma + "तीस"] = [lemma, "VERB", "fem", "sing", "cond", "pres", "p2"]
    forms[lemma + "ती"] = [lemma, "VERB", "fem", "sing", "cond", "pres", "p3"]
    forms[lemma + "तें"] = [lemma, "VERB", "neut", "sing", "cond", "pres", "p1"]
    forms[lemma + "तेंस"] = [lemma, "VERB", "neut", "sing", "cond", "pres", "p2"]
    forms[lemma + "तें"] = [lemma, "VERB", "neut", "sing", "cond", "pres", "p3"]
    forms[lemma + "तों"] = [lemma, "VERB", "masc|fem|neut", "plur", "cond", "pres", "p1"]
    forms[lemma + "तां"] = [lemma, "VERB", "masc|fem|neut", "plur", "cond", "pres", "p2"]
    forms[lemma + "ते"] = [lemma, "VERB", "masc", "plur", "cond", "pres", "p3"]
    forms[lemma + "त्या"] = [lemma, "VERB", "fem", "plur", "cond", "pres", "p3"]
    forms[lemma + "तीं"] = [lemma, "VERB", "neut", "plur", "cond", "pres", "p3"]
    return forms


def verbs_subjunctive(lemma):
    forms = {}
    forms[lemma + "ावा"] = [lemma, "VERB", "masc", "sing", "subj", "pres", "p1"]
    forms[lemma + "ावास"] = [lemma, "VERB", "masc", "sing", "subj", "pres", "p2"]
    forms[lemma + "ावा"] = [lemma, "VERB", "masc", "sing", "subj", "pres", "p3"]
    forms[lemma + "ावी"] = [lemma, "VERB", "fem", "sing", "subj", "pres", "p1"]
    forms[lemma + "ावीस"] = [lemma, "VERB", "fem", "sing", "subj", "pres", "p2"]
    forms[lemma + "ावी"] = [lemma, "VERB", "fem", "sing", "subj", "pres", "p3"]
    forms[lemma + "ावें"] = [lemma, "VERB", "neut", "sing", "subj", "pres", "p1"]
    forms[lemma + "ावेंस"] = [lemma, "VERB", "neut", "sing", "subj", "pres", "p2"]
    forms[lemma + "ावें"] = [lemma, "VERB", "neut", "sing", "subj", "pres", "p3"]
    forms[lemma + "ावे"] = [lemma, "VERB", "masc|fem|neut", "plur", "subj", "pres", "p1"]
    forms[lemma + "ावेत"] = [lemma, "VERB", "masc|fem|neut", "plur", "subj", "pres", "p2"]
    forms[lemma + "तावे"] = [lemma, "VERB", "masc|fem|neut", "plur", "subj", "pres", "p3"]
    return forms


def verbs_imperative(lemma):
    forms = {}
    forms[lemma + "ूं"] = [lemma, "VERB", "masc|fem|neut", "sing", "imp", "pres", "p1"]
    forms[lemma] = [lemma, "VERB", "masc|fem|neut", "sing", "imp", "pres", "p2"]
    forms[lemma + "ो"] = [lemma, "VERB", "masc|fem|neut", "sing", "imp", "pres", "p3"]
    forms[lemma + "ूं"] = [lemma, "VERB", "masc|fem|neut", "sing", "imp", "pres", "p1"]
    forms[lemma + "ा"] = [lemma, "VERB", "masc|fem|neut", "sing", "imp", "pres", "p2"]
    forms[lemma + "ोत"] = [lemma, "VERB", "masc|fem|neut", "sing", "imp", "pres", "p3"]

    return forms

def personal_pronoun(lemma):
    forms = {}
    if lemma[0] in "म":
        forms[lemma] = [lemma, "PRON", "sing", "nom|acc"]
        forms["आह्" + lemma[:-1]] = [lemma, "PRON", "plur", "nom|acc"]
        forms[lemma[0] + "्या"] = [lemma, "PRON", "sing", "inst"]
        forms["आह्" + lemma] = [lemma, "PRON", "plur", "inst"]
        forms[lemma[0] + "ला"] = [lemma, "PRON", "sing", "dat"]
        forms["आह्" + lemma[0] + "ला"] = [lemma, "PRON", "plur", "dat"]
        forms[lemma[0] + "ाजाहून"] = [lemma, "PRON", "sing", "abl"]
        forms["आ" + lemma[0] + "ांहून"] = [lemma, "PRON", "plur", "abl"]
        forms[lemma[0] + "ाझा"] = [lemma, "PRON", "sing", "gen"]
        forms["आ" + lemma[0] + "चा"] = [lemma, "PRON", "plur", "gen"]
        forms[lemma[0] + "ाझ्यात"] = [lemma, "PRON", "sing", "loc"]
        forms["आ" + lemma[0] + "्हांत"] = [lemma, "PRON", "plur", "loc"]
    elif lemma is "तूं":
        forms[lemma] = [lemma, "PRON", "sing", "nom|acc"]
        forms[lemma[:-1] + "म्ही"] = [lemma, "PRON", "plur", "nom|acc"]
        forms[lemma[0] + "्वा"] = [lemma, "PRON", "sing", "inst"]
        forms[lemma + "म्हीं"] = [lemma, "PRON", "plur", "inst"]
        forms[lemma[:-1] + "ला"] = [lemma, "PRON", "sing", "dat"]
        forms[lemma[:-1] + "म्हाला"] = [lemma, "PRON", "plur", "dat"]
        forms[lemma[:-1] + "जहून"] = [lemma, "PRON", "sing", "abl"]
        forms[lemma[:-1] + "ज्यांहून"] = [lemma, "PRON", "plur", "abl"]
        forms[lemma[:-1] + "झा"] = [lemma, "PRON", "sing", "gen"]
        forms[lemma[:-1] + "मचा"] = [lemma, "PRON", "plur", "gen"]
        forms[lemma[:-1] + "झ्यात"] = [lemma, "PRON", "sing", "loc"]
        forms[lemma[:-1] + "म्हांत"] = [lemma, "PRON", "plur", "loc"]
