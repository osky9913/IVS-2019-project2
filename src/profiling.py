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


def createSum(inputNumbers, subSum):
    total = "( "
    for x in inputNumbers.split():
        total += "( " + x + " ^ 2 - " + subSum + " ) + "
    total = total[:-2]
    total += ") "
    return total


def createSubSum(inputNumbers):
    totalSubSum = "( ( ( "
    N = 0
    for x in inputNumbers.split():
        totalSubSum += x
        totalSubSum += ' + '
        N += 1
    totalSubSum = totalSubSum[:-3]
    totalSubSum += " ) / " + str(N) + " ) ^ 2 * " + str(N) + " ) " + str(N)
    return totalSubSum

if __name__ == '__main__':
    inputNumbers=""
    for line in sys.stdin:
        inputNumbers += line
    inputNumbers = inputNumbers.replace('\n',' ')
    subSum = createSubSum(inputNumbers)
    N = subSum.split()[-1]
    subSum = subSum[:-1]
    totalSum = createSum(inputNumbers, subSum)
    evalString = "2 √ ( ( 1 / {} - 1 ) * {} )".format(N, totalSum)
    with PyCallGraph(output=GraphvizOutput()):
        resolve(evalString)
        
