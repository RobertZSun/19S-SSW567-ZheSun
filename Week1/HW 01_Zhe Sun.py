#! C:\Users\Administrator\AppData\Local\Programs\Python\Python37
# -*- coding: utf-8 -*-
"""
Created  on Sunday Jan 27 22:05:48 2019

@author: zhe sun

This file demonstrates what kind of a triangle it is, or whether it is a triangle.
"""

import unittest
import random
import math


class TestTriangle(unittest.TestCase):

    def test_init(self):
        """ Sides stored properly in __init__() """

        t = Triangle(3, 4, 5)
        self.assertEqual(t.a, 3)
        self.assertEqual(t.b, 4)
        self.assertEqual(t.c, 5)

    def test_right_triangle(self):
        """ test right triangle detection """

        t1 = Triangle(3, 4, 5)
        self.assertTrue(t1.right_triangle())
        self.assertTrue(Triangle(5, 4, 3).right_triangle())
        self.assertFalse(Triangle(3, 3, 3).right_triangle())

    def test_Scalene_right_triangle(self):
        """ test Scalene_right_triangle detection """

        t2 = Triangle(3, 4, 5)
        self.assertEqual("Scalene right triangle", t2.classify_triangle())
        self.assertEqual("Scalene right triangle", Triangle(5, 4, 3).classify_triangle())
        self.assertNotEqual("Scalene right triangle", Triangle(3, 3, 3).classify_triangle())

    def test_Scalene_triangle(self):
        """ test Scalene_triangle detection """

        t3 = Triangle(3, 8, 9)
        self.assertEqual("Scalene triangle", t3.classify_triangle())
        self.assertEqual("Scalene triangle", Triangle(8, 3, 9).classify_triangle())
        self.assertNotEqual("Scalene triangle", Triangle(5, 13, 12).classify_triangle())

    def test_Isosceles_right_triangle(self):
        """ test Isosceles right triangle detection """

        t4 = Triangle(1, 1, math.sqrt(2))
        self.assertEqual("Isosceles right triangle", t4.classify_triangle())
        self.assertEqual("Isosceles right triangle", Triangle(1, math.sqrt(2), 1).classify_triangle())
        self.assertNotEqual("Isosceles right triangle", Triangle(5, 13, 12).classify_triangle())

    def test_Isosceles_triangle(self):
        """ test Isosceles triangle detection """

        t5 = Triangle(4, 4, 3)
        self.assertEqual("Isosceles triangle", t5.classify_triangle())
        self.assertEqual("Isosceles triangle", Triangle(4, 3, 4).classify_triangle())
        self.assertNotEqual("Isosceles triangle", Triangle(5, 5, 5).classify_triangle())

    def test_Equilateral_triangle(self):
        """ test Equilateral triangle detection """

        t6 = Triangle(4, 4, 4)
        self.assertEqual("Equilateral triangle", t6.classify_triangle())
        self.assertEqual("Equilateral triangle", Triangle(4, 4, 4).classify_triangle())
        self.assertNotEqual("Equilateral triangle", Triangle(4, 3, 4).classify_triangle())

    def test_Not_triangle(self):
        """ test not triangle condition detection """
        try:
            t7 = Triangle(1, 1, 4)
        except ValueError as v:
            self.assertEqual(type(v), ValueError)

        try:
            t8 = Triangle(1, 4, 1)
        except ValueError as v1:
            self.assertEqual(type(v1), ValueError)

        try:
            t9 = Triangle(-1, 4, 1)
        except ValueError as v2:
            self.assertEqual(type(v2), ValueError)


class Triangle:
    def __init__(self, s1, s2, s3):
        self.a = s1
        self.b = s2
        self.c = s3

        """ to make sure the lengths of the sides could be formed into a triangle"""
        if min(s1, s2, s3) > 0:
            if ((s1 + s2) > s3) and ((s1 + s3) > s2) and ((s2 + s3) > s1):
                pass
            else:
                raise ValueError("Error! The sum of any two sides of a triangle has to be greater than the third side")
        else:
            raise ValueError("Error! Any side of a triangle can not be negative number")

    def right_triangle(self):
        """ To judge whether this is a right triangle """

        biggest = max(self.a, self.b, self.c)
        lowest = min(self.a, self.b, self.c)
        middle = sum([self.a, self.b, self.c]) - biggest - lowest
        if round(((lowest ** 2) + (middle ** 2)), 2) == round((biggest ** 2), 2):
            return True
        else:
            return False

    def classify_triangle(self):
        """ This function classify_triangle(a, b, c) where a, b,
        and c are the lengths of the sides of the triangles.
        Then returns a string with the type of triangle from
        three values corresponding to the lengths of the
        three sides of the Triangle.
        return:
            If all three sides are equal, return 'Equilateral triangle'
            If exactly one pair of sides are equal, return 'Isoceles triangle'
            If no pair of  sides are equal, return 'Scalene triangle'
            If not a valid triangle, then return 'NotATriangle'
            If the sum of any two sides equals the squate of the
            third side, then return 'Right triangle' this will be combined
            with other type of triangle, such as "Isoceles right triangle",
            "Scalene right triangle"
        """

        if self.a == self.b == self.c:
            return "Equilateral triangle"
        elif (self.a == self.b) or (self.a == self.c) or (self.b == self.c):
            if self.right_triangle():
                return "Isosceles right triangle"
            else:
                return "Isosceles triangle"
        elif (self.a != self.b) and (self.a != self.c) and (self.b != self.c):
            if self.right_triangle():
                return "Scalene right triangle"
            else:
                return "Scalene triangle"
        else:
            return None


def main():

    print("Welcome to Auto Triangle Judgement!")
    a = float(input("Please input the first length of a triangle: "))
    b = float(input("Please input the first length of a triangle: "))
    c = float(input("Please input the first length of a triangle: "))

    triangle1 = Triangle(a, b, c)
    result1 = triangle1.classify_triangle()
    print("It's a ", result1)


if __name__ == '__main__':

    unittest.main(exit=False, verbosity=2)
    main()
