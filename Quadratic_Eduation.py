'''
Implement the function find_roots to find the roots of the quadratic equation: ax2 + bx + c = 0. The function should return a tuple containing roots in any order.

The roots of the quadratic equation can be found with the following formula: A quadratic equation.

For example, find_roots(2, 10, 8) should return (-1, -4) or (-4, -1) as the roots of the equation 2x2 + 10x + 8 = 0 are -1 and -4.
'''

import math

def find_roots(a, b, c):
    x,y = -b/(2*a)+math.sqrt(b**2-4*a*c)/(2*a),-b/(2*a)-math.sqrt(b**2-4*a*c)/(2*a)
    return (x,y)

print(find_roots(2, 10, 8));
