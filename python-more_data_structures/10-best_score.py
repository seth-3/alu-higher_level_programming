#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = list(a_dictionary)[0]
    for x, y in a_dictionary.items():
        if a_dictionary[max] < y:
            max = x
    return max
