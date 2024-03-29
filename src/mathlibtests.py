#!/usr/bin/python3
# coding: utf-8

##
# @file mathlibtests.py
# @author xsarva00
# @brief Module containing various types of unit tests to check
# the functionality of individual calculator functions.
# @note To run the tests, use the command ./mathlibtests.py in the src folder
# of the project

import unittest
import math
from mathlibrary import Mathlibrary
from evaluate import resolve


##
# @brief Testing add function.
class MathLibraryTestAdd(unittest.TestCase):
    def setUp(self):
        self.mathlib = Mathlibrary()

    def testAddPositive(self):
        self.assertEqual(self.mathlib.add(0, 0), 0)
        self.assertEqual(self.mathlib.add(42, 37), 79)
        self.assertEqual(self.mathlib.add(234, 743), 977)
        self.assertEqual(self.mathlib.add(10000, 233891), 243891)

    def testAddNegative(self):
        self.assertEqual(self.mathlib.add(-14, -48), -62)
        self.assertEqual(self.mathlib.add(-34, 56), 22)
        self.assertEqual(self.mathlib.add(-2938, -230), -3168)
        self.assertEqual(self.mathlib.add(-83924, 21481), -62443)
        self.assertEqual(self.mathlib.add(1237471, -42194914284), -42193676813)

    def testAddPositiveFloat(self):
        self.assertAlmostEqual(self.mathlib.add(12.284523, 5.21421), 17.498733)
        self.assertAlmostEqual(self.mathlib.add(0.124894, 0.111111111), 0.23600511)
        self.assertAlmostEqual(self.mathlib.add(2389.4829, 40124.840179), 42514.323079)
        self.assertAlmostEqual(self.mathlib.add(99.9999999, 99.0001), 199.0000999)
        self.assertNotAlmostEqual(self.mathlib.add(0.0000000001, 0.0000001), 0.0000002)

    def testAddNegativeFloat(self):
        self.assertAlmostEqual(self.mathlib.add(-12.284523, -5.21421), -17.498733)
        self.assertAlmostEqual(self.mathlib.add(-0.124894, -0.111111111), -0.23600511)
        self.assertAlmostEqual(self.mathlib.add(-2389.4829, -40124.840179), -42514.323079)
        self.assertAlmostEqual(self.mathlib.add(-99.9999999, -99.0001), -199.0000999)
        self.assertNotAlmostEqual(self.mathlib.add(-0.0000000001, -0.0000001), -0.0000002)
        self.assertAlmostEqual(self.mathlib.add(0.9999998, -0.9999999), -0.0000001)


##
# @brief Testing sub function.

class MathLibraryTestSub(unittest.TestCase):
    def setUp(self):
        self.mathlib = Mathlibrary()

    def testSubPositive(self):
        self.assertEqual(self.mathlib.sub(2, 0), 2)
        self.assertEqual(self.mathlib.sub(0, 0), 0)
        self.assertEqual(self.mathlib.sub(234, 212), 22)
        self.assertEqual(self.mathlib.sub(4242, 1239), 3003)
        self.assertEqual(self.mathlib.sub(1234567890, 2345237), 1232222653)
        self.assertEqual(self.mathlib.sub(14701742817021, 14701742817021), 0)
        self.assertEqual(self.mathlib.sub(42, 67), -25)
        self.assertEqual(self.mathlib.sub(4367, 5001), -634)
        self.assertEqual(self.mathlib.sub(14314, 148735481541), -148735467227)

    def testSubNegative(self):
        self.assertEqual(self.mathlib.sub(-2, 0), -2)
        self.assertEqual(self.mathlib.sub(-123, 45), -168)
        self.assertEqual(self.mathlib.sub(347, -319), 666)
        self.assertEqual(self.mathlib.sub(-8654, -69), -8585)
        self.assertEqual(self.mathlib.sub(-1234567890, 2345237), -1236913127)
        self.assertEqual(self.mathlib.sub(-14701742817021, 14701742817021), -29403485634042)
        self.assertEqual(self.mathlib.sub(-14701742817021, -14701742817021), 0)

    def testSubFloat(self):
        self.assertAlmostEqual(self.mathlib.sub(1.242, 0.239), 1.003)
        self.assertAlmostEqual(self.mathlib.sub(12.134532, 32.5239905), -20.3894585)
        self.assertAlmostEqual(self.mathlib.sub(-34.6364329, -805.8520399), 771.215607)


##
# @brief Testing div function and zero division exception.

class MathLibraryTestDiv(unittest.TestCase):
    def setUp(self):
        self.mathlib = Mathlibrary()

    def testDivByZero(self):
        with self.assertRaises(ZeroDivisionError):
            self.mathlib.div(2145, 0)
        with self.assertRaises(ZeroDivisionError):
            self.mathlib.div(0, 0)

    def testDivPossitive(self):
        self.assertEqual(self.mathlib.div(0, 2), 0)
        self.assertEqual(self.mathlib.div(234, 2), 117)
        self.assertEqual(self.mathlib.div(10206, 42), 243)
        self.assertEqual(self.mathlib.div(11348337, 49127), 231)

    def testDivNegative(self):
        self.assertEqual(self.mathlib.div(-234, 117), -2)
        self.assertEqual(self.mathlib.div(-10206, -42), 243)
        self.assertEqual(self.mathlib.div(11348337, -49127), -231)

    def testDivFloat(self):
        self.assertAlmostEqual(self.mathlib.div(2, 3), 0.6666666666)
        self.assertAlmostEqual(self.mathlib.div(345, -17), -20.294117647)
        self.assertAlmostEqual(self.mathlib.div(840143, 4910), 171.1085539714)
        self.assertAlmostEqual(self.mathlib.div(784.893253, 9523.7329), 0.08241445463)


##
# @brief Testing mul function.

class MathLibraryTestMul(unittest.TestCase):
    def setUp(self):
        self.mathlib = Mathlibrary()

    def testMulPositive(self):
        self.assertEqual(self.mathlib.mul(5, 8), 40)
        self.assertEqual(self.mathlib.mul(19247, 0), 0)
        self.assertEqual(self.mathlib.mul(0, 701134), 0)
        self.assertEqual(self.mathlib.mul(12442, 823), 10239766)

    def testMulNegative(self):
        self.assertEqual(self.mathlib.mul(-5, 8), -40)
        self.assertEqual(self.mathlib.mul(-5, -8), 40)
        self.assertEqual(self.mathlib.mul(-9313, 7053170), -65686172210)
        self.assertEqual(self.mathlib.mul(0, -701134), 0)

    def testMulFloat(self):
        self.assertAlmostEqual(self.mathlib.mul(1.5132, 8.85130), 13.39378716)
        self.assertAlmostEqual(self.mathlib.mul(5.841021, 0.843103), 4.9245823281)
        self.assertAlmostEqual(self.mathlib.mul(-34.4104921, 913.83191), -31445.405719782911)
        self.assertAlmostEqual(self.mathlib.mul(-794.7415124, -0.05923), 47.072539779452)


##
# @brief Testing factorial function and its exception handling when
# @param parameter is not a number, is negative or floating point number.

class MathLibraryTestFactorial(unittest.TestCase):
    def setUp(self):
        self.mathlib = Mathlibrary()

    def testFactorialNotaNumber(self):
        with self.assertRaises(ValueError):
            self.mathlib.factorial("XX")
        with self.assertRaises(ValueError):
            self.mathlib.factorial("qwert")

    def testFactorialNegative(self):
        with self.assertRaises(ValueError):
            self.mathlib.factorial(-42)
        with self.assertRaises(ValueError):
            self.mathlib.factorial(-75319)

    def testFactorialFloat(self):
        with self.assertRaises(ValueError):
            self.mathlib.factorial(12.4242)
        with self.assertRaises(ValueError):
            self.mathlib.factorial(0.8410571)
        with self.assertRaises(ValueError):
            self.mathlib.factorial(0.0000001)

    def testFactorialPositive(self):
        self.assertEqual(self.mathlib.factorial(0), 1)
        self.assertEqual(self.mathlib.factorial(1), 1)
        self.assertEqual(self.mathlib.factorial(6), 720)
        self.assertEqual(self.mathlib.factorial(42), 1405006117752879898543142606244511569936384000000000)


##
# @brief Testing pow function and its exception handling when
# @param parameter is zero or negative or floating point number.

class MathLibraryTestPow(unittest.TestCase):
    def setUp(self):
        self.mathlib = Mathlibrary()

    def testPowNegativeExponent(self):
        with self.assertRaises(ValueError):
            self.mathlib.pow(-5, -4)
        with self.assertRaises(ValueError):
            self.mathlib.pow(423, -5892)

    def testPowFloatExponent(self):
        with self.assertRaises(ValueError):
            self.mathlib.pow(42, 4.20424)
        with self.assertRaises(ValueError):
            self.mathlib.pow(532.43, 49.00001)

    def testPowZeroExponent(self):
        self.assertEqual(self.mathlib.pow(0, 0), 1)
        self.assertEqual(self.mathlib.pow(123, 0), 1)
        self.assertEqual(self.mathlib.pow(-123, 0), 1)
        self.assertEqual(self.mathlib.pow(-12.3, 0), 1)
        self.assertEqual(self.mathlib.pow(12.3, 0), 1)

    def testPowEvenExponent(self):
        self.assertEqual(self.mathlib.pow(2, 2), 4)
        self.assertEqual(self.mathlib.pow(12, 6), 2985984)
        self.assertEqual(self.mathlib.pow(43, 4), 3418801)
        self.assertEqual(self.mathlib.pow(-4, 2), 16)
        self.assertEqual(self.mathlib.pow(-80, 4), 40960000)

    def testPowOddExponent(self):
        self.assertEqual(self.mathlib.pow(3, 3), 27)
        self.assertEqual(self.mathlib.pow(47, 5), 229345007)
        self.assertEqual(self.mathlib.pow(-12, 7), -35831808)
        self.assertEqual(self.mathlib.pow(-37, 5), -69343957)


##
# @brief Testing root function and its exception handling
# when the root is negative or floating point number or
# when base is negative and root is even number.

class MathLibraryTestRoot(unittest.TestCase):
    def setUp(self):
        self.mathlib = Mathlibrary()

    def testRootNegativeExponent(self):
        with self.assertRaises(ValueError):
            self.mathlib.root(5, -2)
        with self.assertRaises(ValueError):
            self.mathlib.root(42, -421)

    def testRootFloatExponent(self):
        with self.assertRaises(ValueError):
            self.mathlib.root(2, 0.00001)
        with self.assertRaises(ValueError):
            self.mathlib.root(4194, 12.4201412)
        with self.assertRaises(ValueError):
            self.mathlib.root(935295, 75392.000001)

    def testRootEvenNegativeBase(self):
        with self.assertRaises(ValueError):
            self.mathlib.root(-3, 6)
        with self.assertRaises(ValueError):
            self.mathlib.root(-7318, 4917912)

    def testRootFractionNegativeBase(self):
        with self.assertRaises(ValueError):
            self.mathlib.root(-0.5, 6)
        with self.assertRaises(ValueError):
            self.mathlib.root(-1.2, 4917912)

    def testRootZeroExponent(self):
        with self.assertRaises(ValueError):
            self.mathlib.root(2, 0)

    def testRootNaturalExponent(self):
        self.assertEqual(self.mathlib.root(4, 2), 2)
        self.assertEqual(self.mathlib.root(-27, 3), -3)
        self.assertEqual(self.mathlib.root(907784931546351634835748413459499319296, 24), 42)
        self.assertEqual(self.mathlib.root(-62748517, 7), -13)
        self.assertEqual(self.mathlib.root(109418989131512359209, 42), 3)


##
# @brief Testing ln function and its exception handling
# when given number is negative or zero.

class MathLibraryTestLn(unittest.TestCase):
    def setUp(self):
        self.mathlib = Mathlibrary()

    def testLnNegative(self):
        with self.assertRaises(ValueError):
            self.mathlib.ln(-123)
        with self.assertRaises(ValueError):
            self.mathlib.ln(-0.00001)
        with self.assertRaises(ValueError):
            self.mathlib.ln(-41928501)

    def testLnZero(self):
        with self.assertRaises(ValueError):
            self.mathlib.ln(0)
        with self.assertRaises(ValueError):
            self.mathlib.ln(0.00000)

    def testLnNaturalNumberGreaterThanOne(self):
        self.assertAlmostEqual(self.mathlib.ln(math.e), 1)
        self.assertAlmostEqual(self.mathlib.ln(2), 0.693147180)
        self.assertAlmostEqual(self.mathlib.ln(42), 3.73766961828)
        self.assertAlmostEqual(self.mathlib.ln(17349), 9.76129014682632)

    def testLnNaturalNumberLowerThanOne(self):
        self.assertAlmostEqual(self.mathlib.ln(0.8257), -0.19152376755875)
        self.assertAlmostEqual(self.mathlib.ln(0.541), -0.6143360001356)
        self.assertAlmostEqual(self.mathlib.ln(0.0042), -5.472670753692814)


##
# @brief Testing evaluation of expressions given to calculator and
# exception handling caused by incorrect expression given


class evaluateExpressionTest(unittest.TestCase):
    def testIncorrectExpressions(self):
        with self.assertRaises(ValueError):
            resolve("( ) )")
        with self.assertRaises(ValueError):
            resolve("( ( ( )")
        with self.assertRaises(ValueError):
            resolve("- - 234")
        with self.assertRaises(ValueError):
            resolve("( - ) + 42.42")
        with self.assertRaises(ValueError):
            resolve("9 + - 3 * / 12 ) ( - 2 ")
        with self.assertRaises(ValueError):
            resolve("( ( ( ( ( ( ( ( 2 + 2 ) ) ) ) ) ) )")
        with self.assertRaises(ValueError):
            resolve("√ ^ 2")
        with self.assertRaises(ValueError):
            resolve("2 * 4 - * √ 3")

    def testCorrectExpressionsBasicOperation(self):
        self.assertEqual(resolve("4 - 2"), 2)
        self.assertEqual(resolve("( 5 + 3 ) * 2"), 16)
        self.assertEqual(resolve("5 - 3 * 2"), -1)
        self.assertEqual(resolve("12 + 8 - 35 + 7"), -8)

    def testCorrectExpressionsRootPow(self):
        self.assertEqual(resolve("8 + 5 * 2 √ 9"), 23)
        self.assertEqual(resolve("2 √ 25 * 6"), 30)
        self.assertEqual(resolve("5 √ 32 + 6 √ 64"), 4)
        self.assertEqual(resolve("3 ^ 2 ^ 2"), 81)

    def testCorrectExpressionsBrackets(self):
        self.assertEqual(resolve("( ( 6 - 4 ) - ( 9 + 2 ) ) * 2"), -18)
        self.assertEqual(resolve("( ( ( - 5 ) + ( - 2 ) ) + 10 ) * 3"), 9)
        self.assertEqual(resolve("( ( 5 + 6 ) ) * 3"), 33)

    def testCorrectExpressionsFloat(self):
        self.assertAlmostEqual(resolve("2.5 + 3.6 - 2.3"), 3.8)
        self.assertAlmostEqual(resolve("4.1 * 12.41 / 9.314"), 5.4628516212153)
        self.assertAlmostEqual(resolve("2 √ 2 * 2 √ 23 "), 6.782329983125)
        self.assertAlmostEqual(resolve("( ( 5 - 8 ) + 5 √ 42 ) * 4.2"), -3.7304997871396)


if __name__ == '__main__':
    unittest.main()
