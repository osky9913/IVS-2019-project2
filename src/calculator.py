##
# @file calculator.py
# @author xsedla1h, xsvobo1t
#
# @brief Module consisting of funcions that handle the
# user interaction with the gui

from PyQt5 import QtWidgets
from ui_calculator import CalculatorUi
import math
import evaluate
from mathlibrary import Mathlibrary


##
# @brief This class contains all the necessary methods
# for the interconnection of the ui of the calculator and the
# mathematical and evaluation funcions
class CalculatorWindow(QtWidgets.QMainWindow, CalculatorUi):
    ##
    # @brief Stores the value of the last evaluated expression
    #
    ans = '0'

    ##
    # @brief Indicates the exact last character that was added to the
    # expression
    #
    lastCharacter = ''

    ##
    # @brief Indicates the type of the button that was pressed last. Can
    # be either 'dig' for digit or 'op' for operand
    #
    lastButton = 'dig'

    ##
    # @brief Indicates whether there has already been a decimal point written
    # within a given number
    #
    decimalPoint = False


    ##
    # @brief constructor
    #
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton_0.clicked.connect(self.digitPressed)
        self.pushButton_1.clicked.connect(self.digitPressed)
        self.pushButton_2.clicked.connect(self.digitPressed)
        self.pushButton_3.clicked.connect(self.digitPressed)
        self.pushButton_4.clicked.connect(self.digitPressed)
        self.pushButton_5.clicked.connect(self.digitPressed)
        self.pushButton_6.clicked.connect(self.digitPressed)
        self.pushButton_7.clicked.connect(self.digitPressed)
        self.pushButton_8.clicked.connect(self.digitPressed)
        self.pushButton_9.clicked.connect(self.digitPressed)

        self.pushButton_decimal.clicked.connect(self.decimalPressed)
        self.pushButton_plus.clicked.connect(self.plusPressed)
        self.pushButton_minus.clicked.connect(self.minusPressed)
        self.pushButton_mul.clicked.connect(self.mulPressed)
        self.pushButton_powr.clicked.connect(self.powerPressed)
        self.pushButton_factorial.clicked.connect(self.factorialPressed)
        self.pushButton_div.clicked.connect(self.divPressed)
        self.pushButton_bracketL.clicked.connect(self.bracketLeftPressed)
        self.pushButton_bracketR.clicked.connect(self.bracketRightPressed)
        self.pushButton_ln.clicked.connect(self.lnPressed)
        self.pushButton_root.clicked.connect(self.rootPressed)

        self.pushButton_clean.clicked.connect(self.cleanPressed)
        self.pushButton_ans.clicked.connect(self.ansPressed)
        self.pushButton_equals.clicked.connect(self.equalsPressed)
        self.labelAns.setText('0')

        self.pushButton_help.setToolTipDuration(99999)
        self.pushButton_help.setToolTip("\
        Welcome to our calculator!\n\
        This calculator is able to solve various types of expressions\n\
        but the user has to follow certain rules:\n\n\
         1. Any negative value has to be contained within brackets: (-1)    \n\
         2. Functions 'ln' and 'x!' first evaluate current user input,\n\
              then calculate the given function value from the result\n\
         3. In order to use the '√' function the user has to specify\n\
              the order of the root first: 2√3\n\
         4. 'ANS' variable stores the last caculated result\n\
         5. The calculator implicitely remembers the most recent result\n\
         ")

    ##
    # @brief Inserts a particular digit into the input string
    # 
    def digitPressed(self):
        if self.lastCharacter == ')' or self.lastCharacter == 'a':
            self.labelWrite.setText(self.labelWrite.text())
            return

        button = self.sender()
        self.labelWrite.setText(self.labelWrite.text() + button.text())

        self.lastCharacter = button.text()
        self.lastButton = 'dig'

    ##
    # @brief Inserts a decimal point into the input string
    # 
    def decimalPressed(self):
        if self.lastButton == 'op' \
            or self.decimalPoint == True \
            or self.lastCharacter == '':
            return

        self.labelWrite.setText(self.labelWrite.text() + '.')
        self.decimalPoint = True
        self.lastCharacter = '.'
        self.lastButton = 'op'

    ##
    # @brief Inserts the '+' character int the calc input
    # 
    def plusPressed(self):
        if self.lastButton == 'op' and self.lastCharacter != ')':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' + ')
        self.decimalPoint = False
        self.lastCharacter = '+'
        self.lastButton = 'op'

    ##
    # @brief Inserts the '-' character int the calc input
    # 
    def minusPressed(self):
        if self.lastButton == 'op' and self.lastCharacter not in '()':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' - ')
        self.decimalPoint = False
        self.lastCharacter = '-'
        self.lastButton = 'op'

    ##
    # @brief Inserts the '^' character int the calc input
    # 
    def powerPressed(self):
        if self.lastButton == 'op' and self.lastCharacter != ')':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' ^ ')
        self.decimalPoint = False
        self.lastCharacter = '^'
        self.lastButton = 'op'

    ##
    # @brief Inserts the '*' character into the calc input
    # 
    def mulPressed(self):
        if self.lastButton == 'op' and self.lastCharacter != ')':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' * ')
        self.decimalPoint = False
        self.lastCharacter = '*'
        self.lastButton = 'op'

    ##
    # @brief Inserts the left bracket into the input text
    # 
    def bracketLeftPressed(self):
        if self.lastCharacter == '.':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' ( ')
        self.decimalPoint = False
        self.lastCharacter = '('
        self.lastButton = 'op'

    ##
    # @brief Inserts the right bracket into the input text
    # 
    def bracketRightPressed(self):
        if self.lastCharacter == '.' or self.lastCharacter == '':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' ) ')
        self.decimalPoint = False
        self.lastCharacter = ')'
        self.lastButton = 'op'

    ##
    # @brief Inserts the '/' character into the calc input
    # 
    def divPressed(self):
        if self.lastButton == 'op' and self.lastCharacter != ')':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' / ')
        self.decimalPoint = False
        self.lastCharacter = '/'
        self.lastButton = 'op'

    ##
    # @brief Inserts the root symbol into the input. The user has to specify
    # the order of the root first
    # 
    def rootPressed(self):
        if self.lastButton != 'dig' and self.lastCharacter != ')':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' √ ')
        self.decimalPoint = False
        self.lastCharacter = '√'
        self.lastButton = 'op'

    ##
    # @brief Evaluates the current input and outputs the value of its
    # natural logarithm
    # 
    def lnPressed(self):
        self.equalsPressed()
        if self.labelAns == 'ERROR':
            return

        try:
            self.ans = str(Mathlibrary.ln(float(self.labelAns.text())))
        except:
            self.labelAns.setText('ERROR')
            self.labelWrite.setText('')
            self.lastCharacter = ''
            self.lastButton = ''
            self.decimalPoint = False
            self.ans = '0'
            return

        self.labelAns.setText(self.ans)
        self.labelWrite.setText('')
        self.lastCharacter = ''
        self.lastButton = 'dig'
        self.decimalPoint = False

    ##
    # @brief Evaluates the current calculator input and outputs the value
    # of its factorial
    # 
    def factorialPressed(self):
        self.equalsPressed()
        if self.labelAns.text() == 'ERROR':
            return
        if math.isinf(float(self.labelAns.text())) \
            or float(self.labelAns.text()) > 995:
            self.labelAns.setText('infinity')
            return

        # Checks if the result is a whole number and if so, trims the decimal part
        if int(float(self.labelAns.text())) - float(self.labelAns.text()) == 0:
            self.labelAns.setText(str(int(float(self.labelAns.text()))))

        try:
            self.ans = str(Mathlibrary.factorial(int(self.labelAns.text())))
        except:
            self.labelAns.setText('ERROR')
            self.labelWrite.setText('')
            self.lastCharacter = ''
            self.lastButton = ''
            self.decimalPoint = False
            self.ans = '0'
            return

        self.labelAns.setText(self.ans)
        self.labelWrite.setText('')
        self.lastCharacter = ''
        self.lastButton = 'dig'
        self.decimalPoint = False

    ##
    # @brief Resets the calc to the default state
    # 
    def cleanPressed(self):
        self.labelWrite.setText('')
        self.labelAns.setText('0')
        self.lastCharacter = ''
        self.lastButton = 'dig'
        self.decimalPoint = False
        self.ans = '0'

    ##
    # @brief Inserts a 'last answer' variable into the calc input label
    # 
    def ansPressed(self):
        if (self.lastButton == 'dig' \
            or self.lastCharacter == '.') \
            and self.labelWrite.text() != '':
            return

        self.labelWrite.setText(self.labelWrite.text() + 'ANS')
        self.lastButton = 'dig'
        self.lastCharacter = 'a'
        self.decimalPoint = True

    ##
    # @brief Evaluates current input and prints the result to the
    # answer label
    # 
    def equalsPressed(self):
        if self.labelWrite.text() == '':
            self.labelWrite.setText('')
            self.decimalPoint = False
            self.lastButton = 'dig'
            self.lastCharacter = ''
            self.ans = self.labelAns.text()
            return

        # Takes care of the substitution of self.ans for its actual value
        if 'ANS' in self.labelWrite.text():
            if '-' in self.ans:
                self.ans = ' ( ' + self.ans[:1] + ' ' + self.ans[1:] + ' ) '
            self.labelWrite.setText(self.labelWrite.text().replace('ANS', self.ans))

        # Gives the user an option to use previous result without explicitly
        # specifying it
        if self.labelWrite.text()[0] not in '0123456789':
            if self.labelWrite.text()[1] != '(':
                if '-' in self.ans:
                    self.ans = ' ( ' + self.ans[:1] + ' ' + self.ans[1:] + ' ) '
                self.labelWrite.setText(self.ans + self.labelWrite.text())

        # Tries to evaluate the input
        try:
            self.ans = str(evaluate.resolve(self.labelWrite.text()))
        except:
            self.labelAns.setText('ERROR')
            self.labelWrite.setText('')
            self.lastCharacter = ''
            self.lastButton = 'dig'
            self.decimalPoint = False
            self.ans = '0'
            return

        self.labelAns.setText(self.ans)
        self.labelWrite.setText('')
        self.decimalPoint = False
        self.lastButton = 'dig'
        self.lastCharacter = ''
