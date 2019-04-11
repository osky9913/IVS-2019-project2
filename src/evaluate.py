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
