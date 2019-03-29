#!/usr/bin/python


##
# @package mathlibrary
# Library of mathematical methods for the calculator
#
# This module contains all the necessary methods
# for the calculator so that it can perform all
# mathematical operations.


class Mathlibrary:

    ## 
    # @brief Computes the sum of two numbers
    # 
    # @param a First number to be summed
    # @param b Second number to be summed
    # 
    # @return Sum of 'a' and 'b'
    @staticmethod
    def add(a, b):


    ## 
    # @brief Computes the difference of two numbers
    # 
    # @param a Number we subtract from
    # @param b Number we subtract with
    # 
    # @return Difference of 'a' and 'b'
    @staticmethod
    def sub(a, b):


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


    ## 
    # @brief Multiplies two numbers together 
    # 
    # @param a Number we multiply
    # @param b Number we multiply with
    # 
    # @return Value of 'a' multiplied by 'b'
    @staticmethod
    def mul(a, b):


    ## 
    # @brief Computes the factorial to a given number
    # 
    # @param a Number whose factorial value is to be computed 
    # 
    # @exception Undefined Parameter 'a' was either not an integer or it was negative
    #
    # @return Value of 'a!'
    @taticmethod
    def factorial(a):


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
