#!/usr/bin/python3

##
# @file mathlibrary.py
# @author xsedla1h
#
# @brief Library of mathematical methods for the calculator
#
# This module contains all the necessary methods
# for the calculator so that it can perform all
# mathematical operations.
#

class Mathlibrary:

    ## 
    # @brief Computes the sum of two numbers
    # 
    # @param a First number to be summed
    # @param b Second number to be summed
    # 
    # @return Sum of 'a' and 'b'
    @staticmethod
    def add( a , b ):
        return round(a + b, 10)


    ## 
    # @brief Computes the difference of two numbers
    # 
    # @param a Number we subtract from
    # @param b Number we subtract with
    # 
    # @return Difference of 'a' and 'b'
    @staticmethod
    def sub(a, b):
        return round(a - b, 10)


    ## 
    # @brief Divides a number with another number
    # 
    # @param a Number to be divided
    # @param b Number we divide with
    # 
    # @exception DividedByZero Parameter 'b' was zero, cannot divide by zero
    #
    # @return Value of 'a' divided by 'b'
    @staticmethod
    def div(a, b):
        if b == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return round(a / b, 10)


    ## 
    # @brief Multiplies two numbers together 
    # 
    # @param a Number we multiply
    # @param b Number we multiply with
    # 
    # @return Value of 'a' multiplied by 'b'
    @staticmethod
    def mul(a, b):
        return round(a * b, 10)


    ## 
    # @brief Computes the factorial to a given number
    # 
    # @param a Number whose factorial value is to be computed 
    # 
    # @exception Undefined Parameter 'a' was either not an integer or it was negative
    #
    # @return Value of 'a!'
    @staticmethod
    def factorial(a):
        if isinstance(a, str):
            raise ValueError('Factorial: a is not a number')
        if a < 0 or isinstance(a, float):
            raise ValueError('Factorial is not defined for negative numbers or floats')

        if a == 1 or a == 0:
            return 1
        else:
            return a * Mathlibrary.factorial(a - 1)


    ## 
    # @brief Computes the power of two numbers
    # 
    # @param base Number whose power is to be computed
    # @param exp The exponent, has to be a natural number or zero
    # 
    # @exception Undefined Parameter 'exp' was not a natural number
    # or zero
    #
    # @return Value of 'base^exp'
    @staticmethod
    def pow(base, exp):
        if not isinstance(exp, int) or exp < 0:
            raise ValueError('The exponent has to be a positive integer')
        return round(base ** exp, 10)


    ## 
    # @brief Computes the n-th root of a given number
    # 
    # @param base Number whose root is to be computed
    # @param n The exponent which determines the order of the root.
    # It has to be a natural number
    # 
    # @exception UndefinedExponent Parameter 'n' was not a natural number
    # @exception UndefinedRoot Parameter 'base' was negative and the exponent
    # happened to be even
    # @exception UndefinedRoot Parameter 'base' was a negative fraction
    #
    # @return Value of the 'n-th' root of 'base'
    @staticmethod
    def root(base, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError('The order of the root has to be a natural number')
        if base < 0 and (n % 2) == 0:
            raise ValueError('This root has no solution in real numbers')
        if isinstance(base, float) and base < 0:
            raise ValueError('The value of this root is undefined')

        if base < 0:
            return round(-((-base) ** (1/n)), 10)
        else:
            return round(base ** (1/n), 10)



    ## 
    # @brief Computes the natural log of a given number
    # 
    # @param a Number whose natural log is to be computed
    # 
    # @exception Undefined Parameter 'a' was not bigger than zero 
    #
    # @return Natural log of 'a' - 'ln(a)'
    @staticmethod
    def ln(a):
        if a <= 0:
            raise ValueError('Natural log is not defined for negative values and zero')

        # Computing the natural log using a continued fraction algorithm
        n = 1000
        power = (a - 1) / (a + 1)
        result = (2 * n) - 1

        i = n - 1
        while i > 0:
            result = ((2 * i) - 1) - ((i * i * power * power) / result)
            i -= 1
        result = (2 * power) / result

        return round(result, 10)
