"""Lab 2: Higher Order Functions & Lambdas"""
from utils import letter_to_num, num_to_letter, looper, mirror_letter

def make_derivative(f, h=1e-5):
    """Returns a function that approximates the derivative of f.

    Recall that f'(a) = (f(a + h) - f(a)) / h as h approaches 0. We will
    approximate the derivative by choosing a very small value for h.

    >>> square = lambda x: x*x
    >>> derivative = make_derivative(square)
    >>> result = derivative(3)
    >>> round(result, 3) # approximately 2*3
    6.0
    """
    deriv = lambda num: (f(num + h) - f(num)) / h
    return deriv


# String Transformers

from operator import add, sub

def caesar_generator(num, op):
    """Returns a one-argument Caesar cipher function. The function should "rotate" a
    letter by an integer amount 'num' using an operation 'op' (either add or
    sub).

    You may use the provided `letter_to_num` and `num_to_letter` functions,
    which will map all lowercase letters a-z to 0-25 and all uppercase letters
    A-Z to 26-51.

    >>> letter_to_num('a')
    0
    >>> letter_to_num('c')
    2
    >>> num_to_letter(3)
    'd'

    >>> caesar2 = caesar_generator(2, add)
    >>> caesar2('a')
    'c'
    >>> brutus3 = caesar_generator(3, sub)
    >>> brutus3('d')
    'a'
    """
    caesar = lambda x: num_to_letter(op(letter_to_num(x),num))
    return caesar


# Encryption and Decryption

def make_encrypter(f1, f2, f3):
    """Generates an "encrypter" that applies a specific set of encryption
    functions on the message

    >>> caesar3 = caesar_generator(3, add)
    >>> caesar2 = caesar_generator(2, add)
    >>> encrypter = make_encrypter(caesar2, mirror_letter, caesar3)
    >>> encrypter('abcd') # caesar2(mirror_letter(caesar3('a'))) -> 'y'
    'yxwv'
    """
    f1, f2, f3 = looper(f1), looper(f2), looper(f3)
    enc = lambda x: f1(f2(f3(x)))
    return enc

def make_decrypter(f1, f2, f3):
    """Generates a "decrypter" function.

    >>> brutus3 = caesar_generator(3, sub)
    >>> brutus2 = caesar_generator(2, sub)
    >>> decrypter = make_decrypter(brutus2, mirror_letter, brutus3)
    >>> decrypter('yxwv') # brutus3(mirror_letter(brutus2('y'))) = 'a'
    'abcd'
    """
    f1, f2, f3 = looper(f1), looper(f2), looper(f3)
    dec = lambda x: f3(f2(f1(x)))
    return dec


