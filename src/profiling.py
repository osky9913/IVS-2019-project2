#!/usr/bin/python3

##
# @file profiling.py
# @author xsarva00
# @brief profiling for mathematical and evaluating functions


## 
# @brief profiling for mathematical and evaluating functions
#
# This modul contains script for profiling functions od calculator
# on given mathematical formula. Its output is computed number and
# graph of called functions, number of calles and time.

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from evaluate import resolve
from mathlibrary import Mathlibrary
import sys

##
# @brief Make first sum in formula as a string from given numbers
# 
# @param Variable wich contains all numbers separated with '\n'
# 
# @return String representing sum of given numbers
def createSum(inputNumbers):
    total = "( "
    for x in inputNumbers.split():
        total += "( " + x + " ^ 2" + " ) + "
    total = total[:-2]
    total += ")"
    return total

##
# @brief Make second sum in formula as a string from given numbers
# 
# @param Variable wich contains all numbers separated with '\n'
# 
# @return String representing sum of given numbers divided by count of numbers
# than squared and multiplied with count of numbers
def createSubSum(inputNumbers):
    totalSubSum = "( ( ( ( "
    N = 0
    for x in inputNumbers.split():
        totalSubSum += x
        totalSubSum += ' + '
        N += 1
    totalSubSum = totalSubSum[:-3]
    totalSubSum += " ) / " + str(N) + " ) ^ 2 ) * " + str(N) + " )"
    return totalSubSum

##
# @brief Compute standard deviation either as one string or with side calculations
# prints result and make a .png graph
if __name__ == '__main__':
    inputNumbers=""
    # Switch between one string and side calculations computing
    oneString = False
    N = 0 
    # Read numbers from stdin
    for line in sys.stdin:
        inputNumbers += line
    # Replace eol with space
    inputNumbers = inputNumbers.replace('\n',' ')
    #Count the numbers
    for x in inputNumbers.split():
        N += 1

    #Profiling on one single string
    if oneString:
        subSum = createSubSum(inputNumbers)
        nextSum = createSum(inputNumbers)
        evalString = "2 √ ( ( 1 / ( {} - 1 ) ) * ( {} - {} ) )".format(N, nextSum, subSum)
        with PyCallGraph(output=GraphvizOutput()):
            print(resolve(evalString))


    #Profiling using side calculations
    else:
        firstSum = 0
        secondSum = 0
        with PyCallGraph(output=GraphvizOutput()):
            #Calculate SUM of numbers and SUM of numbers^2
            for x in inputNumbers.split():
                firstSum = Mathlibrary.add(firstSum, float(x))#sum of Xi
                secondSum = Mathlibrary.add(secondSum, Mathlibrary.pow(float(x), 2))
            #N*(x')^2
            firstSum = Mathlibrary.pow(Mathlibrary.div(firstSum, N), 2)
            firstSum = Mathlibrary.mul(firstSum, N)
            finalSum = Mathlibrary.sub(secondSum, firstSum)
            #final formula
            print(resolve("2 √ ( 1 / ( {} - 1 ) * {} )".format(N, finalSum)))

