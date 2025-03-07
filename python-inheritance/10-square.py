#!/usr/bin/python3
'''creates a subclass Square from Rectangle'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''defines a new class Square from inheritance of Rectangle'''

    def __init__(self, size):
        '''initialize variables'''
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        '''method to return the string with the area'''
        return self.__size ** 2
