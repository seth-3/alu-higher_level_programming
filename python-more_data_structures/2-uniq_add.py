#!/usr/bin/python3
def uniq_add(my_list=[]):
    setty = set(my_list)
    n = 0
    for i in setty:
        n += i
    return n
