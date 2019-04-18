#!/usr/bin/python3

#VUT FIT 1BIT
#IVS-Project2
#Author: Marek Sarvas
#Login: xsarva00

# @author Marek Sarvas xsarva00

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from evaluate import resolve
import sys

# create SUM in standard deviation formula as string
# for evaluating single string
def createSum(inputNumbers, subSum):
    total = "( "
    for x in inputNumbers.split():
        total += "( " + x + " ^ 2 - " + subSum + " ) + "
    total = total[:-2]
    total += ") "
    return total

#  creating SUM of given numbers divided by count of numbers squared
# for evaluating single string
def createSubSum(inputNumbers):
    totalSubSum = "( ( ( "
    N = 0
    for x in inputNumbers.split():
        totalSubSum += x
        totalSubSum += ' + '
        N += 1
    totalSubSum = totalSubSum[:-3]
    totalSubSum += " ) / " + str(N) + " ) ^ 2 * " + str(N) + " ) "
    return totalSubSum

# main
if __name__ == '__main__':
    inputNumbers=""
    N = 0 
    for line in sys.stdin:
        inputNumbers += line
        N += 1
    inputNumbers = inputNumbers.replace('\n',' ')

    #Profiling on one single string
    #subSum = createSubSum(inputNumbers)
    #totalSum = createSum(inputNumbers, subSum)
    #evalString = "2 √ ( ( 1 / {} - 1 ) * {} )".format(N, totalSum)
    #with PyCallGraph(output=GraphvizOutput()):
    #    print(resolve(evalString))


    #Profiling using side calculations
    firstSum = 0
    secondSum = 0
    with PyCallGraph(output=GraphvizOutput()):
        #Calculate SUM of numbers and SUM of numbers^2
        for x in inputNumbers.split():
            firstSum = resolve("{} + {}".format(firstSum, x))#sum of Xi
            secondSum = resolve("{} + {} ^ 2".format(secondSum, x))
        #N*(x')^2
        firstSum = resolve("( {} / {} ) ^ 2 * {}".format(firstSum, N, N))
        #final formula
        print(resolve("2 √ ( 1 / ( {} - 1 ) * ( {} - {} ) )".format(N, secondSum, firstSum)))

