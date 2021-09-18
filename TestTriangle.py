# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testNotTriangle1(self): 
        self.assertEqual(classifyTriangle(100,1,10),'NotATriangle','100,1,10 is not a triangle')
    def testNotTriangle2(self): 
        self.assertEqual(classifyTriangle(4,150,2),'NotATriangle','4,150,2 is not a triangle')
    def testNotTriangle3(self): 
        self.assertEqual(classifyTriangle(1,20,1),'NotATriangle','1,20,1 is not a triangle')

    def testRightTriangle1(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a right triangle')
    def testRightTriangle2(self): 
        self.assertEqual(classifyTriangle(8,15,17),'Right','8,15,17 is a right triangle')
    def testRightTriangle3(self):
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a right triangle')

    def testEquilateralTriangle1(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is an equilateral triangle')
    def testEquilateralTriangle2(self): 
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 is an equilateral triangle')
    def testEquilateralTriangle3(self): 
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 is an equilateral triangle')

    def testScaleneTriangle1(self):
        self.assertEqual(classifyTriangle(10,11,12),'Scalene','10,11,12 is a scalene triangle')
    def testScaleneTriangle2(self):
        self.assertEqual(classifyTriangle(5,8,6),'Scalene','5,8,6 is a scalene triangle')
    def testScaleneTriangle3(self):
        self.assertEqual(classifyTriangle(10,12,14),'Scalene','10,12,14 is a scalene triangle')
    
    def testIsoscelesTriangle1(self):
        self.assertEqual(classifyTriangle(3,2,2),'Isosceles','3,2,2 is an isosceles triangle')
    def testIsoscelesTriangle2(self):
        self.assertEqual(classifyTriangle(5,7,5),'Isosceles','5,7,5 is an isosceles triangle')
    def testIsoscelesTriangle3(self):
        self.assertEqual(classifyTriangle(3,3,5),'Isosceles','3,3,5 is an isosceles triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

