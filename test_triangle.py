# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    "Collection of test functions for triangle.py"
    # define multiple sets of tests as functions with names that begin

    def test_not_triangle_1(self):
        "classify_triangle test function, Expected Output: 'NotATriangle'"
        self.assertEqual(classify_triangle(100,1,10),'NotATriangle','100,1,10 is not a triangle')
    def test_not_triangle_2(self):
        "classify_triangle test function, Expected Output: 'NotATriangle'"
        self.assertEqual(classify_triangle(4,150,2),'NotATriangle','4,150,2 is not a triangle')
    def test_not_triangle_3(self):
        "classify_triangle test function, Expected Output: 'NotATriangle'"
        self.assertEqual(classify_triangle(1,20,1),'NotATriangle','1,20,1 is not a triangle')

    def test_right_triangle_1(self):
        "classify_triangle test function, Expected Output: 'Right'"
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a right triangle')
    def test_right_triangle_2(self):
        "classify_triangle test function, Expected Output: 'Right'"
        self.assertEqual(classify_triangle(8,15,17),'Right','8,15,17 is a right triangle')
    def test_right_triangle_3(self):
        "classify_triangle test function, Expected Output: 'Right'"
        self.assertEqual(classify_triangle(5,12,13),'Right','5,12,13 is a right triangle')

    def test_equilateral_triangle_1(self):
        "classify_triangle test function, Expected Output: 'Equilateral'"
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 is an equilateral triangle')
    def test_equilateral_triangle_2(self):
        "classify_triangle test function, Expected Output: 'Equilateral'"
        self.assertEqual(classify_triangle(2,2,2),'Equilateral','2,2,2 is an equilateral triangle')
    def test_equilateral_triangle_3(self):
        "classify_triangle test function, Expected Output: 'Equilateral'"
        self.assertEqual(classify_triangle(3,3,3),'Equilateral','3,3,3 is an equilateral triangle')

    def test_scalene_triangle_1(self):
        "classify_triangle test function, Expected Output: 'Scalene'"
        self.assertEqual(classify_triangle(10,11,12),'Scalene','10,11,12 is a scalene triangle')
    def test_scalene_triangle_2(self):
        "classify_triangle test function, Expected Output: 'Scalene'"
        self.assertEqual(classify_triangle(5,8,6),'Scalene','5,8,6 is a scalene triangle')
    def test_scalene_triangle_3(self):
        "classify_triangle test function, Expected Output: 'Scalene'"
        self.assertEqual(classify_triangle(10,12,14),'Scalene','10,12,14 is a scalene triangle')

    def test_isosceles_triangle_1(self):
        "classify_triangle test function, Expected Output: 'Isosceles'"
        self.assertEqual(classify_triangle(3,2,2),'Isosceles','3,2,2 is an isosceles triangle')
    def test_isosceles_triangle_2(self):
        "classify_triangle test function, Expected Output: 'Isosceles'"
        self.assertEqual(classify_triangle(5,7,5),'Isosceles','5,7,5 is an isosceles triangle')
    def test_isosceles_triangle_3(self):
        "classify_triangle test function, Expected Output: 'Isosceles'"
        self.assertEqual(classify_triangle(3,3,5),'Isosceles','3,3,5 is an isosceles triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
