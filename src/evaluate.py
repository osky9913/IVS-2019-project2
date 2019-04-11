#!/usr/bin/python3



from pythonds.basic.stack import Stack #pip3 install --user  pythonds
from mathlibrary import Mathlibrary


"""
@brief Validate Number
@param s String Number ( float or int ) 
@return boolean True or False
@author Martin Osvald xosval03
"""
def isNumber(s):


    for i in s:
        
        if (i.count('.') > 1) :
            return False
        if ( i.count('.') == 1 and len(i)== 1):
            return False
        
        if i not in "0123456789.":
            return False
        if s[0] == '.' or s[-1] == '.':
            return False

    return True


"""
@brief changing a Math expression from infixt to Postif
@param infixexpr Math expression string with whitespace between characters 
@return string  as infix expression
@author Martin Osvald xosval03
"""
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
    
#   print(tokenList)

    
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
    #print(tokenList)

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


    #print(" ".join(postfixList))
    return " ".join(postfixList)


"""
@brief function for stack evaluation , it's connected with Mathlibrary
@param op  is operator
@param op1 is number
@param op2 is number  
@return result
@author Martin Osvald xosval03
"""

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
