#!/usr/bin/python3
'''A script that checks if the object is an instance of a class'''


def is_kind_of_class(obj, a_class):
    '''checks if the object is an instance of a class

    Args:
       obj: object to check
       a_class: class of the object

    Returns:
       True: if the object is an instance of, or if the obj is a class instance
       False: if the obj isn't an instance of, or if the it is a class instance
    '''
    return isinstance(obj, a_class)
