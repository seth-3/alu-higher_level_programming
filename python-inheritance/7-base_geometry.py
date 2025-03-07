#!/usr/bin/python3
'''defines a class'''


class BaseGeometry:
    '''defines a class'''

    def area(self):
        '''raises an exception message for the area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
