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
def createSum(inputNumbers):
    total = "( "
    for x in inputNumbers.split():
        total += "( " + x + " ^ 2" + " ) + "
    total = total[:-2]
    total += ")"
    return total

#  creating SUM of given numbers divided by count of numbers squared
# for evaluating single string
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

#Main. oneString variable is used as switch to do profiling
# either with one giant string or with some side calculations
if __name__ == '__main__':
    inputNumbers=""
    oneString = True
    N = 0 
    #Read numbers from stdin
    for line in sys.stdin:
        inputNumbers += line
    #Replace eol with space
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
                firstSum = resolve("{} + {}".format(firstSum, x))#sum of Xi
                secondSum = resolve("{} + {} ^ 2".format(secondSum, x))
            #N*(x')^2
            firstSum = resolve("( {} / {} ) ^ 2 * {}".format(firstSum, N, N))
            #final formula
            print(resolve("2 √ ( 1 / ( {} - 1 ) * ( {} - {} ) )".format(N, secondSum, firstSum)))

