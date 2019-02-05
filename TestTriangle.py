# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
to test defects

mainly use assertEqual() function

@author: Zhe Sun
"""

import unittest
import math

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testIsoscelesTriangles(self):
        # test ID 01

        self.assertEqual(classifyTriangle(4, 4, 3), 'Isosceles', '4,4,3 should be a Isosceles triangle')
        self.assertNotEqual(classifyTriangle(4, 4, 4), 'Isosceles', '4,4,4 should be an Equilateral triangle')

    def testIsoscelesRightTriangles(self):
        # test ID 02

        self.assertEqual(classifyTriangle(1, math.sqrt(2), 1), 'Isosceles Right', '1,sqrt(2),1 should be a Isosceles Right triangle')
        self.assertNotEqual(classifyTriangle(5, 12, 13), 'Isosceles Right', '5,12,13 should be a Scalene right triangle')

    def testScaleneTriangles(self):
        # test ID 03

        self.assertEqual(classifyTriangle(3, 8, 9), 'Scalene', '3,8,9 should be Scalene triangle')
        self.assertEqual(classifyTriangle(8, 3, 9), 'Scalene', '8,3,9 should be Scalene triangle')
        self.assertNotEqual(classifyTriangle(8, 8, 9), 'Scalene', '8,8,9 should be Isosceles triangle')

    def testScaleneRightTriangles(self):
        # test ID 04

        self.assertEqual(classifyTriangle(5, 13, 12), 'Scalene Right', '5,13,12 should be Scalene right triangle')
        self.assertNotEqual(classifyTriangle(1, math.sqrt(2), 1), 'Scalene Right', '1,math.sqrt(2),1 should be a Isosceles Right triangle')

    def testNotTriangles(self):
        # test ID 05

        self.assertEqual(classifyTriangle(1, 1, 4), 'NotATriangle', '1,1,4 should not be a triangle')
        self.assertEqual(classifyTriangle(1, 4, 1), 'NotATriangle', '1,4,1 should not be a triangle')
        self.assertEqual(classifyTriangle(-1, 4, 1), 'NotATriangle', '-1,4,1 should not be a triangle')

    def testEquilateralTriangles(self):
        # test ID 06

        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be an Equilateral triangle')
        self.assertNotEqual(classifyTriangle(4, 4, 1), 'NotATriangle', '1,4,1 should not be a Isosceles triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
