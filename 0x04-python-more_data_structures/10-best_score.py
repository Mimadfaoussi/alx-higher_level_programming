#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary == None):
        return None
    #Best = (list(a_dictionary.),list(a_dictionary.values())[0]
    best = (None, None)
    for key in a_dictionary.keys():
        if best == (None, None):
            best = (key, a_dictionary[key])
        if a_dictionary[key] > best[1]:
            best = (key, a_dictionary[key])
    return best[0]
