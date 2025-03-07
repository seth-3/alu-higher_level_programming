#!/usr/bin/python3
'''creates a subclass Rectangle of parent class BaseGeometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class that defines a rectangle from BaseGeometry class'''

    def __init__(self, width, height):
        '''initialies variables'''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
