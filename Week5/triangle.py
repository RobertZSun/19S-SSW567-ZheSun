# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles
the results come as expected.

@author: zhe sun
"""


def classify_triangle(first_side, second_side, third_side):
    """ This function classify_triangle(first_side, second_side, third_side)
        where first_side, second_side,and third_side are the lengths of the
        sides of the triangles. Then returns first_side string with the type
        of triangle from three values corresponding to the lengths of the
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

    biggest = max(first_side, second_side, third_side)
    lowest = min(first_side, second_side, third_side)
    # This information was not in the requirements spec but
    # is important for correctness
    # the difference of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    valid_triangle = not(((first_side + second_side) > third_side) and (
        (first_side + third_side) > second_side) and (
            (second_side + third_side) > first_side))
    # require that the input values be >= 0 and <= 200
    if biggest > 200 or lowest <= 0 or valid_triangle:
        raise ValueError('NotATriangle')

    middle = sum([first_side, second_side, third_side]) - biggest - lowest

    if first_side == second_side and second_side == third_side:
        return 'Equilateral'
    if (first_side == second_side) or (second_side == third_side) or (first_side == third_side):
        if round(((lowest ** 2) + (middle ** 2)), 2) == round((biggest ** 2), 2):
            return 'Isosceles Right'
        return 'Isosceles'
    if first_side not in (second_side, third_side):
        if round(((lowest ** 2) + (middle ** 2)), 2) == round((biggest ** 2), 2):
            return 'Scalene Right'
        return 'Scalene'
    return None
