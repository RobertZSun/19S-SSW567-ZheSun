# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles
the results come as expected.

@author: zhe sun
"""
import math

def classifyTriangle(a, b, c):
    """ This function classify_triangle(a, b, c) where a, b,
        and c are the lengths of the sides of the triangles.
        Then returns a string with the type of triangle from
        three values corresponding to the lengths of the
        three sides of the Triangle.
        return:
            If all three sides are equal, return 'Equilateral'
            If exactly one pair of sides are equal, return 'Isoceles'
            If no pair of  sides are equal, return 'Scalene'
            If not a valid triangle, then return 'NotATriangle'
            If the sum of any two sides equals the squate of the
            third side, then return 'Right' this will be combined
            with other type of triangle, such as "Isoceles right triangle",
            "Scalene Right"
        """

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'NotATriangle'

    if a <= 0 or b <= 0 or c <= 0:
        return 'NotATriangle'

    # This information was not in the requirements spec but
    # is important for correctness
    # the difference of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if not(((a + b) > c) and ((a + c) > b) and ((b + c) > a)):
        return 'NotATriangle'

    # now we know that we have a valid triangle

    biggest = max(a, b, c)
    lowest = min(a, b, c)
    middle = sum([a, b, c]) - biggest - lowest

    if a == b and b == c:
        return 'Equilateral'
    elif (a == b) or (b == c) or (a == c):
        if round(((lowest ** 2) + (middle ** 2)), 2) == round((biggest ** 2), 2):
            return 'Isosceles Right'
        else:
            return 'Isosceles'
    elif (a != b) and (b != c) and (a != b):
        if round(((lowest ** 2) + (middle ** 2)), 2) == round((biggest ** 2), 2):
            return 'Scalene Right'
        else:
            return 'Scalene'

