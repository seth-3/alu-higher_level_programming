#!/usr/bin/python3
'''Inheritance of a class'''


class MyList(list):
    '''class MyList inherits from the main list called list'''

    def print_sorted(self):
        '''prints the sorted list'''
        sorted_list = self.copy()
        sorted_list.sort()
        print("{}".format(sorted_list))
