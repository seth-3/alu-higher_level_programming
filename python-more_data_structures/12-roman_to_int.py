#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return (0)
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    next_numeral = 0
    length = len(roman_string)
    while (i < length):
        current_numeral = numerals[roman_string[i]]
        if i + 1 <= length - 1:
            next_numeral = numerals[roman_string[i+1]]
        if next_numeral and current_numeral < next_numeral:
            total += next_numeral - current_numeral
            i += 1
        else:
            total += current_numeral
        i += 1
    return (total)
