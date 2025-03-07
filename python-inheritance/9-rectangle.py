#!/usr/bin/python3
'''creates a class Rectangle from parent class BaseGeometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class that inherits from BaseGeometry'''

    def __init__(self, width, height):
        '''initialize variables'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''function to return the area of a rectangle'''
        r_area = self.__width * self.__height
        return r_area

    def __str__(self):
        '''returns Rectangle width/height'''
        return f"[Rectangle] {self.__width}/{self.__height}"
