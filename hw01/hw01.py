from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    if a > b:
    	x = a*a
    	if b>c:
    		y = b*b
    	else:
    		y = c*c
    else:
    	x = b*b
    	y = c*c
    return x + y


def largest_factor(n):
    """Return the largest factor of n*n-1 that is smaller than n.

    >>> largest_factor(4) # n*n-1 is 15; factors are 1, 3, 5, 15
    3
    >>> largest_factor(9) # n*n-1 is 80; factors are 1, 2, 4, 5, 8, 10, ...
    8
    """
    x = n*n-1
    y = 1
    for i in range(1,n+1):
    	if x % i == 0:
    		if i < n:
    			if i > y:
    				y = i
    return y


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return 3 == 2

def t():
    return 1 / 0

def f():
    return 1


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    x = 1
    while n != 1:
    	if n % 2 == 0:
    		n = int(n / 2)
    		x += 1
    		print(n)
    	else:
    		n = int(n * 3 + 1)
    		x += 1
    		print(n)
    return x


challenge_question_program = """
"*** YOUR CODE HERE ***"
"""

