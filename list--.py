Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> add = lambda
SyntaxError: invalid syntax
>>> add = lambda c:c*10
>>> add(10)
100
>>> add(5)
50
>>> add(0)
0
>>> subtract = lambda c:c*10
>>> subtract(10)
100
>>> subtract(3)
30
>>> subtract(0)
0
>>> add = lambda a,b:a*b
>>> add(10,2)
20
>>> add(3,0)
0
>>> [x+2 for x in range(1,20)]
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
>>> [x*5 for x in range(1,10)]
[5, 10, 15, 20, 25, 30, 35, 40, 45]
>>> [x+2 for x in range(1,10) if x>5]
[8, 9, 10, 11]
>>> [x+2 for x in range(1,10) if x>4]
[7, 8, 9, 10, 11]
>>> {x:x+2 for x in range(10)}
{0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 11}
