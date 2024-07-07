#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# number_to_words.py - A simple number to words converter.
# Copyright (c) 2016 - Jesus Vedasto Olazo - jestoy.olazo@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
A simple number to words converter.

Ex.
1 = "one"
2 = "two"
.
.
.
.
992 = "nine hundred ninety two"

"""

__version__ = "1.0.0"

ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 
        'seventeen', 'eighteen', 'nineteen']

TENS = ["", "", "twenty", "thirty", "forty", 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def convert_hundreds(number):
    if number < 20:
        return ONES[number]
    elif number < 100:
        return TENS[number // 10] + ('' if number % 10 == 0 else ' ' + ONES[number % 10])
    else:
        return ONES[number // 100] + ' hundred' + ('' if number % 100 == 0 else ' ' + convert_hundreds(number % 100))

def convert_thousands(number):
    if number < 1000:
        return convert_hundreds(number)
    else:
        return convert_hundreds(number // 1000) + ' thousand' + ('' if number % 1000 == 0 else ' ' + convert_hundreds(number % 1000))

def convert_millions(number):
    if number < 1000000:
        return convert_thousands(number)
    else:
        return convert_hundreds(number // 1000000) + ' million' + ('' if number % 1000000 == 0 else ' ' + convert_thousands(number % 1000000))

def number_to_words(number):
    if isinstance(number, float):
        integer_part, fractional_part = divmod(number * 100, 100)
        words = convert_millions(int(integer_part))
        if fractional_part:
            words += ' and ' + convert_hundreds(int(fractional_part))
        return words
    elif isinstance(number, int):
        return convert_millions(number)
    else:
        return None

if __name__ == "__main__":
    print("A simple number to words converter.")
    print("Range: 0 to 999,999,999\n\n")
    # Example 1
    print("Example 1:")
    print(f"2 = {number_to_words(2)}")
    # Example 2
    print("Example 2:")
    print(f"34 = {number_to_words(34)}")
    # Example 3
    print("Example 3:")
    print(f"121 = {number_to_words(121)}")
    # Example 4
    print("Example 4:")
    print(f"2378 = {number_to_words(2378)}")
    # Example 5
    print("Example 5:")
    print(f"13725.4534 = {number_to_words(13725.4534)}")
    # Example 6
    print("Example 6:")
    print(f"245312 = {number_to_words(245312)}")
    # Example 7
    print("Example 7:")
    print(f"1000000 = {number_to_words(1000000)}")
    # Example 8
    print("Example 8:")
    print(f"6782215 = {number_to_words(6782215)}")
