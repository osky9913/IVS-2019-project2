from PyQt5 import QtWidgets
from ui_calculator import CalculatorUi
import evaluate
from mathlibrary import Mathlibrary

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
    decimalDot = False


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


    def digitPressed(self):
        if self.lastCharacter == ')' or self.lastCharacter == 'a':
            self.labelWrite.setText(self.labelWrite.text())
            return

        button = self.sender()
        self.labelWrite.setText(self.labelWrite.text() + button.text())

        self.lastCharacter = button.text()
        self.lastButton = 'dig'

    def decimalPressed(self):
        if self.lastButton == 'op' or self.decimalDot == True or self.lastCharacter == '':
            return

        self.labelWrite.setText(self.labelWrite.text() + '.')
        self.decimalDot = True
        self.lastCharacter = '.'
        self.lastButton = 'op'

    def plusPressed(self):
        if self.lastButton == 'op' and self.lastCharacter != ')':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' + ')
        self.decimalDot = False
        self.lastCharacter = '+'
        self.lastButton = 'op'

    def minusPressed(self):
        if self.lastButton == 'op' and self.lastCharacter not in '()':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' - ')
        self.decimalDot = False
        self.lastCharacter = '-'
        self.lastButton = 'op'

    def powerPressed(self):
        if self.lastButton == 'op' and self.lastCharacter != ')':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' ^ ')
        self.decimalDot = False
        self.lastCharacter = '^'
        self.lastButton = 'op'

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
            self.decimalDot = False
            self.ans = '0'
            return

        self.labelAns.setText(self.ans)
        self.labelWrite.setText('')
        self.lastCharacter = ''
        self.lastButton = 'dig'
        self.decimalDot = False

    def mulPressed(self):
        if self.lastButton == 'op' and self.lastCharacter != ')':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' * ')
        self.decimalDot = False
        self.lastCharacter = '*'
        self.lastButton = 'op'

    def bracketLeftPressed(self):
        if self.lastCharacter == '.':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' ( ')
        self.decimalDot = False
        self.lastCharacter = '('
        self.lastButton = 'op'

    def bracketRightPressed(self):
        if self.lastCharacter == '.' or self.lastCharacter == '':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' ) ')
        self.decimalDot = False
        self.lastCharacter = ')'
        self.lastButton = 'op'

    def divPressed(self):
        if self.lastButton == 'op' and self.lastCharacter != ')':
            return

        self.labelWrite.setText(self.labelWrite.text() + ' / ')
        self.decimalDot = False
        self.lastCharacter = '/'
        self.lastButton = 'op'

    def rootPressed(self):
        if self.lastButton != 'dig' and self.lastCharacter != ')':
            return 

        self.labelWrite.setText(self.labelWrite.text() + ' √ ')
        self.decimalDot = False
        self.lastCharacter = '√'
        self.lastButton = 'op'

    def factorialPressed(self):
        self.equalsPressed()
        if self.labelAns == 'ERROR':
            return

        if self.ans == '0':
            self.labelAns.setText('1.0')
            self.labelWrite.setText('')
            self.lastCharacter = ''
            self.lastButton = ''
            self.decimalDot = False
            self.ans = '1'
            return

        if self.ans[-1] != '0' or self.ans[-2] !=  '.':
            self.labelAns.setText('ERROR')
            self.labelWrite.setText('')
            self.lastCharacter = ''
            self.lastButton = ''
            self.decimalDot = False
            self.ans = '0'
        else:
            self.ans = self.ans.strip('.0')
            self.labelAns.setText(self.ans)
        
        try:
            self.ans = str(Mathlibrary.factorial(int(self.labelAns.text())))
        except:
            self.labelAns.setText('ERROR')
            self.labelWrite.setText('')
            self.lastCharacter = ''
            self.lastButton = ''
            self.decimalDot = False
            self.ans = '0'
            return

        self.labelAns.setText(self.ans)
        self.labelWrite.setText('')
        self.lastCharacter = ''
        self.lastButton = 'dig'
        self.decimalDot = False

    def cleanPressed(self):
        self.labelWrite.setText("") 
        self.labelAns.setText("") 
        self.lastCharacter = ''
        self.lastButton = 'dig'
        self.decimalDot = False
        self.ans = '0'

    def ansPressed(self):
        if (self.lastButton == 'dig' \
                or self.lastCharacter == '.') \
                and self.labelWrite.text() != '':
            return
        self.labelWrite.setText(self.labelWrite.text() + "ANS")
        self.lastButton = 'dig'
        self.lastCharacter = 'a'
        self.decimalDot = True

    def equalsPressed(self):
        if self.labelWrite.text() == "":
            self.labelWrite.setText('')
            self.decimalDot = False
            self.lastButton = 'dig'
            self.lastCharacter = ''
            self.ans = self.labelAns.text()
            return

        # takes care of the substitution of self.ans for its actual value
        if 'ANS' in self.labelWrite.text():
            if '-' in self.ans:
                self.ans = ' ( ' + self.ans[:1] + ' ' + self.ans[1:] + ' ) '
            self.labelWrite.setText(self.labelWrite.text().replace('ANS', self.ans))

        # creates the possibility to use previous result without explicitly
        # specifying it
        if self.labelWrite.text()[0] not in '0123456789':
            if self.labelWrite.text()[1] != '(':
                if '-' in self.ans:
                    self.ans = ' ( ' + self.ans[:1] + ' ' + self.ans[1:] + ' ) '
                self.labelWrite.setText(self.ans + self.labelWrite.text())

        try:
            self.ans = str(evaluate.resolve(self.labelWrite.text()))
        except:
            self.labelAns.setText('ERROR')
            self.labelWrite.setText('')
            self.lastCharacter = ''
            self.lastButton = 'dig'
            self.decimalDot = False
            self.ans = '0'
            return

        self.labelAns.setText(self.ans)
        self.labelWrite.setText('')
        self.decimalDot = False
        self.lastButton = 'dig'
        self.lastCharacter = ''
