#!/usr/bin/python3
'''function to returns true/false if the object is an instance of a class'''


def is_same_class(obj, a_class):
    '''function to check if object is an instance of a class given

    Args:
        obj: Object to check
        a_class: class of the object

    Returns:
        True if the obj is an instance
        False if not an instance
    '''
    return (type(obj) == a_class)
