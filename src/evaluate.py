#!/usr/bin/python3

##
# @file evaluate.py
# @author xosval03
# @brief This file contains all the necessary functions for evalulating
# the calculator input

# VUT FIT 1BIT
# IVS-Project2
# Author: Martin Osvald
# Login: xosval03

from stack import EvalStack
from mathlibrary import Mathlibrary


##
# @brief Checks if a string is a valid number
#
# @param s The input string we need to check
#
# @return True or False
def isNumber(s):
    for i in s:

        if i not in "0123456789.":
            return False

    return True


# The solution is based on an article which can be found on:
# http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
# This solution modifies the original idea because of floats and new operators.

##
# @brief Changes a mathematical expression from infix to postfix
#
# @param infixexpr Math expression string with whitespaces between characters
#
# @return Returns a string as an infix expression

def infixToPostfix(infixexpr):
    operator = {}
    operator["√"] = 4
    operator["^"] = 4
    operator["*"] = 3
    operator["/"] = 3
    operator["+"] = 2
    operator["-"] = 2
    operator["("] = 1
    opStack = EvalStack()
    postfixList = []

    tokenList = infixexpr.split()

    for i in range(0, len(tokenList)):
        if tokenList[i] == '-':
            if i == 0:
                tokenList.insert(0, '0')

            elif isNumber(tokenList[i - 1]) == False and tokenList[i - 1] != ')':
                tokenList.insert(i, '0')

            else:
                continue

    for token in tokenList:

        if (isNumber(token) == True):

            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.empty()) and (operator[opStack.peek()] >= operator[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.empty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


##
# @brife Evaluates the input taken from the stack, computes the result. Utilizes
# the module mathlibrary
#
# @param op  Is an operator
#
# @param op1 Is a number
#
# @param op2 Is a number  
#
# @return Returns the result of the operation


def doMath(op, op1, op2):
    if op == "*":
        return Mathlibrary.mul(op1, op2)
    elif op == "/":
        return Mathlibrary.div(op1, op2)
    elif op == "+":
        return Mathlibrary.add(op1, op2)
    elif op == "√":
        return Mathlibrary.root(op2, op1)
    elif op == "^":
        return Mathlibrary.pow(op1, op2)

    else:
        return Mathlibrary.sub(op1, op2)


##
# @brief Creates a stack from the postfix expression, then pops the content and evaluates it
#
# @param postfixExpr An Expression in postfix split with whitespaces
#
# @return Returns the result

def postfixEval(postfixExpr):
    operandStack = EvalStack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if (isNumber(token) == True):
            operandStack.push(float(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            try:
                doMath(token, operand1, operand2)
            except:
                raise ValueError("Not valid expression")
            result = doMath(token, operand1, operand2)

            operandStack.push(result)

    return operandStack.pop()


##
# @brief Checks if the mathematical expression is correct (infix) 
#
# @param expression A math expression
#
# @return True or false
def validate(expression):
    expression = expression.split()

    flagNumber = False
    counterOfLeft = 0
    counterOfRight = 0

    for i in expression:

        if i == '.':
            return False

        if isNumber(i) == True:
            flagNumber = True

        elif (i == '('):
            counterOfLeft += 1
            flagNumber = False

        elif (i == ')'):
            counterOfRight += 1

        elif (counterOfRight > counterOfLeft):
            return False

        elif (i.count('.') > 1):
            return False

        elif (i.count('.') == 1 and len(s) == 1):
            return False

        elif i[0] == '.' or i[-1] == '.':
            return False

        else:
            continue

    for i in range(0, len(expression)):

        if (i == 0) and (expression[i] in "√^+*/"):
            return False
        elif (expression[i] in "√+^-*/") and (expression[i - 1] in "√+^-*/"):
            return False
        else:
            continue

    if (expression[len(expression) - 1] in "√+^-*/"):
        return False

    for i in range(0, len(expression)):
        if expression[i] in "√+^-*/":
            if expression[i + 1] == ')':
                return False

    if (counterOfRight != counterOfLeft):
        return False

    if (flagNumber == False):
        return False

    return True


##
# @brief Evaluates a mathematical expression and returns its result 
#
# @param expression A mathematical expression
#
# @return Returns the result of the evaluated expression
def resolve(expression):
    if (validate(expression) != True):
        raise ValueError("Not valid expression")
    return (postfixEval(infixToPostfix(expression)))