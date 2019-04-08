#!/usr/bin/python3



from pythonds.basic.stack import Stack #pip3 install --user  pythonds
from mathlibrary import Mathlibrary


def isNumber(s):


    for i in s:
        
        if (i.count('.') > 1) :
            return False
        if ( i.count('.') == 1 and len(i)== 1):
            return False
        

        if i not in "0123456789.":
            return False
    return True
