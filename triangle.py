# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018
@author: jrr
@author: rk
"""

def classify_triangle(_a, _b , _c):
    "Function that returns a triangles classification string by taking sides a, b, c"
    # require that the input values be >= 0 and <= 200
    if _a > 200 or _b > 200 or _c > 200:
        return 'InvalidInput'

    if _a <= 0 or _b <= 0 or _c <= 0:
        return 'InvalidInput'

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(_a,int) and isinstance(_b,int) and isinstance(_c,int)):
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (_a >= (_b + _c)) or (_b >= (_a + _c)) or (_c >= (_a + _b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle

    _str = ""

    if _a == _b and _b == _c:
        _str = 'Equilateral'
    elif ((_a ** 2) + (_b ** 2)) == (_c ** 2):
        _str = 'Right'
    elif (_a != _b) and  (_b != _c) and (_c != _a):
        _str = 'Scalene'
    else:
        _str = 'Isosceles'

    return _str
