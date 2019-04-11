#!/usr/bin/python3

#VUT FIT 1BIT
#IVS-Project2
#Author: Martin Osvald
#Login: xosval03

# @author Martin Osvald xosval03




from pythonds.basic.stack import Stack #pip3 install --user  pythonds
from mathlibrary import Mathlibrary


##
# @brief Validate Number
#
# @param s String Number ( float or int ) 
#
# @return boolean True or False

def isNumber(s):
    
    
    for i in s:
        
        if i not in "0123456789.":
            return False
        
        

    return True


##
#@brief changing a Math expression from infixt to Postif
#
#@param infixexpr Math expression string with whitespace between characters 
#
#@return string  as infix expression

# Solution is based on article on http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
# This solution is edit because of floating numbers and new operators
# Also there our function for validate number

def infixToPostfix(infixexpr):
    operator = {}
    operator["√"] = 4
    operator["^"] = 4
    operator["*"] = 3
    operator["/"] = 3
    operator["+"] = 2
    operator["-"] = 2
    operator["("] = 1
    opStack = Stack()
    postfixList = []
    
    tokenList = infixexpr.split()
    
    for i in range(0,len(tokenList)):
        if tokenList[i] == '-':
            if i == 0:
                tokenList.insert(0,'0')

            elif isNumber(tokenList[i-1]) == False and  tokenList[i-1] != ')' :
                tokenList.insert(i,'0')

            else:
                continue
    
    
    #Regex solution , doesn't work 
    #import re
    #tokenList=re.findall(r"[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)  +|[()+\-*√^\/]", infixexpr) nefunguje


    for token in tokenList:

        if  ( isNumber(token) == True ):
            
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (operator[opStack.peek()] >= operator[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())



    return " ".join(postfixList)


##
# @brief function for stack evaluation , it's connected with Mathlibrary
#
# @param op  is operator
#
# @param op1 is number
#
# @param op2 is number  
#
# @return result



def doMath(op, op1, op2):
    if op == "*":
        return Mathlibrary.mul(op1,op2)  
    elif op == "/":
        return Mathlibrary.div(op1,op2)
    elif op == "+":
        return Mathlibrary.add(op1,op2)
    elif op == "√":
        return Mathlibrary.root(op2,int(op1))
    elif op == "^":
        return Mathlibrary.pow(op1,int(op2))

    else:
        return Mathlibrary.sub(op1,op2)



##
# @brief function create a Stack, adding a postif expression and then evaluate 
#
# @param postfixExpr  is expression in postifx , between characters there are whitespaces 
#
# @return result

def postfixEval(postfixExpr):
    operandStack = Stack()
    #operandStack.push(0)
    tokenList = postfixExpr.split()

    for token in tokenList:
        if  ( isNumber(token) == True ):
            operandStack.push(float(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    
    return operandStack.pop()






##
# @brief checked if the mathematical expression is correct ( infix ) 
#
# @param expression is string of mathematical expression
#
# @return boolean True or false


def validate(expression):
    expression=expression.split()
 
    flagNumber = False
    counterOfLeft=0
    counterOfRight=0
       
    for i in expression:
 
        if i == '.':
            return False

        if isNumber(i)==True:
            flagNumber = True

        elif(i =='('):
            counterOfLeft+=1
            flagNumber = False

        elif(i ==')'):
            counterOfRight+=1

        elif(counterOfRight > counterOfLeft):
            return False
    
        elif (i.count('.') > 1) :
            return False

        elif ( i.count('.') == 1 and len(s)== 1):
            return False

        elif i[0] == '.' or i[-1] == '.':
            return False

        else:
            continue


    for i in range(0,len(expression)):
 
        if (i == 0) and (expression[i] in "√^+*/"):
            return False
        elif (expression[i]   in "√+^-*/" ) and (expression[i-1] in "√+^-*/" )  :
            return False
        else:
            continue


    if ( expression[len(expression)-1] in "√+^-*/" ):
        return False 

    for i in range(0,len(expression)):
        if expression[i]   in "√+^-*/":
            if expression[i+1] == ')':
                return False



    if( counterOfRight != counterOfLeft):
        return False
    
    if( flagNumber == False):
        return False
    

    return True


##
# @brief calculate a string mathematical expression and return a value like eval ( infix ) 
#
# @param expression is string of mathematical expression
#
# @return result 


def resolve(expression):
    if ( validate(expression) != True ):
       raise ValueError("Not valid expression")
    return( postfixEval(infixToPostfix(expression)))



