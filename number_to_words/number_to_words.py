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

first_list = ['zero', 'one', 'two', 'three', 'four', 'five',
          'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
          'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
          'seventeen', 'eighteen', 'nineteen']

second_list = ["twenty", "thirty", "forty", 'fifty', 'sixty', 'seventy',
           'eighty', 'ninety']

def step_one(number):
    result = first_list[number]
    return result

def step_two(number):
    if number % 10 == 0:
        result = second_list[(number // 10) - 2]
    elif (number // 10) > 1 and (number // 10) <= 9:
        first_part = second_list[(number // 10) - 2]
        second_part = first_list[number % 10]
        result = " ".join([first_part, second_part])
    return result

def step_three(number):
    if number % 100 == 0:
        result = first_list[number // 100] + " hundred"
    elif number % 100 > 0 and number % 100 <= 99:
        part1 = first_list[number // 100] + " hundred "
        if (number % 100) >= 0 and (number % 100) <= 19:
            part2 = step_one(number % 100)
        elif (number % 100) >= 20 and (number % 100) <= 99:
            part2 = step_two(number % 100)
        result = part1 + part2
    return result

def step_four(number):
    if number % 1000 == 0:
        if (number // 1000) > 0 and (number // 1000) <= 19:
            result = step_one(number // 1000) + " thousand"
        elif (number // 1000) >= 20 and (number // 1000) <= 99:
            result = step_two(number // 1000) + " thousand"
        elif number // 1000 >= 100 and number // 1000 <= 999:
            result = step_three(number // 1000) + " thousand"

    elif number % 1000 > 0 and number % 1000 <= 999:
        if number // 1000 > 0 and number // 1000 <= 19:
            part1 = step_one(number // 1000) + " thousand "
        elif number // 1000 >= 20 and number // 1000 <= 99:
            part1 = step_two(number // 1000) + " thousand "
        elif number // 1000 >= 100 and number // 1000 <= 999:
            part1 = step_three(number // 1000) + " thousand "

        if number % 1000 > 0 and number % 1000 < 20:
            part2 = step_one(number % 1000)
        elif number % 1000 > 19 and number % 1000 < 100:
            part2 = step_two(number % 1000)
        elif number % 1000 > 99 and number % 1000 < 1000:
            part2 = step_three(number % 1000)
        result = part1 + part2
    return result

def step_five(number):
    if number % 1000000 == 0:
        if (number // 1000000) > 0 and (number // 1000000) < 20:
            result = " ".join([step_one(number // 1000000), "million"])
        elif (number // 1000000) > 19 and (number // 1000000) < 100:
            result = " ".join([step_two(number // 1000000), "million"])
        elif (number // 1000000) > 99 and (number // 1000000) < 1000:
            result = " ".join([step_three(number // 1000000), "million"])

    elif number % 1000000 > 0 and number % 1000000 < 1000000000:
        if number // 1000000 > 0 and number // 1000000 < 20:
            first_part = step_one(number // 1000000) + " million "
        elif number // 1000000 > 19 and number // 1000000 < 100:
            first_part = step_two(number // 1000000) + " million "
        elif number // 1000000 > 99 and number // 1000000 < 1000:
            first_part = step_three(number // 1000000) + " million "

        if number % 1000000 > 0 and number % 1000000 < 20:
            second_part = step_one(number % 1000000)
        elif number % 1000000 > 19 and number % 1000000 < 100:
            second_part = step_two(number % 1000000)
        elif number % 1000000 > 99 and number % 1000000 < 1000:
            second_part = step_three(number % 1000000)
        elif number % 1000000 > 999 and number % 1000000 < 1000000:
            second_part = step_four(number % 1000000)

        result = "".join([first_part, second_part])
    return result

def number_to_words(number):
    """
    This is the main function that should be called when converting number
    into words. This function will decide which of other function should be
    called on with regards to the given number. Below is an example.

    Ex.
    if number is 21, this function will call step_two(21) and will return
    string value of "twenty one". if number is 176, this function will call
    step_three(176) and will return a string value of "one hundred seventy six".
    """
    if isinstance(number, float):
        if len(str(number)[str(number).find('.')+1:]) == 1:
            temp_list = (str(number)+'0').split(".")
        elif len(str(number)[str(number).find('.')+1:]) > 2:
            number = round(number, 2)
            temp_list = str(number).split(".")
        else:
            temp_list = str(number).split(".")
        fraction = int(temp_list[1])
        number = int(temp_list[0])
        if number >= 0 and number < 20:
            first_part = step_one(number)
        elif number > 19 and number < 100:
            first_part = step_two(number)
        elif number > 99 and number < 1000:
            first_part = step_three(number)
        elif number > 999 and number < 1000000:
            first_part = step_four(number)
        elif number > 999999 and number < 1000000000:
            first_part = step_five(number)

        if fraction > 0:
            if fraction >= 0 and fraction < 20:
                second_part = step_one(fraction)
            elif fraction > 19 and fraction < 100:
                second_part = step_two(fraction)
            result = " ".join([first_part, "and", second_part])
            return result
        else:
            return first_part

    elif isinstance(number, int):
        if number >= 0 and number < 20:
            result = step_one(number)
        elif number > 19 and number < 100:
            result = step_two(number)
        elif number > 99 and number < 1000:
            result = step_three(number)
        elif number > 999 and number < 1000000:
            result = step_four(number)
        elif number > 999999 and number < 1000000000:
            result = step_five(number)
        return result
    else:
        return None

if __name__ == "__main__":
    print("A simple number to words converter.")
    print("Range: 0 to 999,999,999\n\n")
    # Example 1
    print("Example 1:")
    print("%s = %s" % (str(2), number_to_words(2)))
    # Example 2
    print("Example 2:")
    print("%s = %s" % (str(34), number_to_words(34)))
    # Example 3
    print("Example 3:")
    print("%s = %s" % (str(121), number_to_words(121)))
    # Example 4
    print("Example 4:")
    print("%s = %s" % (str(2378), number_to_words(2378)))
    # Example 5
    print("Example 5:")
    print("%s = %s" % (str(13725.4534), number_to_words(13725.4534)))
    # Example 6
    print("Example 6:")
    print("%s = %s" % (str(245312), number_to_words(245312)))
    # Example 7
    print("Example 7:")
    print("%s = %s" % (str(1000000), number_to_words(1000000)))
    # Example 8
    print("Example 8:")
    print("%s = %s" % (str(6782215), number_to_words(6782215)))
