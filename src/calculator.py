from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator
import evaluate
from mathlibrary import Mathlibrary

class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    
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
    lastButton = ''

    ##
    # @brief Indicates whether there has already been a decimal point written
    # within a given number
    #
    decimalDot = 'false'


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        self.pushButton_decimal.clicked.connect(self.decimal_pressed)
        self.pushButton_plus.clicked.connect(self.plus_pressed)
        self.pushButton_minus.clicked.connect(self.minus_pressed)
        self.pushButton_mul.clicked.connect(self.mul_pressed)
        self.pushButton_powr.clicked.connect(self.powr_pressed)
        self.pushButton_factorial.clicked.connect(self.factorial_pressed)
        self.pushButton_div.clicked.connect(self.div_pressed)
        self.pushButton_bracketL.clicked.connect(self.bracketL_pressed)
        self.pushButton_bracketR.clicked.connect(self.bracketR_pressed)
        self.pushButton_ln.clicked.connect(self.ln_pressed)
        self.pushButton_root.clicked.connect(self.root_pressed)

        self.pushButton_clean.clicked.connect(self.clean_pressed)
        self.pushButton_Ans.clicked.connect(self.ans_pressed)
        self.pushButton_equals.clicked.connect(self.equals_pressed)

    """
    zkontroluje, podminku, zda je mozne psat cislo
    zapise ho
    nastavi lastCharacter a lastButton

    """
    def digit_pressed(self):
        if self.lastCharacter == ')' or self.lastCharacter == 'a':
            self.label_write.setText(self.label_write.text())
            return

        button = self.sender()
        self.label_write.setText(self.label_write.text() + button.text())

        self.lastCharacter = button.text()
        self.lastButton = 'dig'

    def decimal_pressed(self):
        if self.lastButton == 'op' or self.decimalDot == 'true' or self.lastCharacter == '':
            self.label_write.setText(self.label_write.text())
            return
        self.lastButton = 'op'
        self.lastCharacter = '.'
        self.decimalDot = 'true'
        self.label_write.setText(self.label_write.text() + '.')

    def plus_pressed(self):
        if self.lastButton == 'op' or self.lastCharacter == '':
            self.label_write.setText(self.label_write.text())
            return
        self.lastButton = 'op'
        self.lastCharacter = '+'
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' + ')

    def minus_pressed(self):
        if self.lastButton == 'op' or self.lastCharacter == '':
            self.label_write.setText(self.label_write.text())
            return
        self.lastButton = 'op'
        self.lastCharacter = '-'
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' - ')

    def powr_pressed(self):
        if self.lastButton == 'op' or self.lastCharacter == ' ^ ' or self.lastCharacter == '':
            self.label_write.setText(self.label_write.text())
            return
        self.lastButton = 'op'
        self.lastCharacter = '^'
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' ^ ')

    # vyhodnoti aktualni vstup a vysledek posle do metody ln
    def ln_pressed(self):
        self.lastButton = 'op'
        self.lastCharacter = 'ln'
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + 'ln')

    def mul_pressed(self):
        if self.lastButton == 'op' or self.lastCharacter == '':
            self.label_write.setText(self.label_write.text())
            return
        self.lastButton = 'op'
        self.lastCharacter = ' * '
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' * ')

    def bracketL_pressed(self):
        if self.lastCharacter == '.' or self.decimalDot == 'true':
            self.label_write.setText(self.label_write.text())
            return
        self.lastButton = 'op'
        self.lastCharacter = '('
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' ( ')

    def bracketR_pressed(self):
        if self.lastCharacter == '.' or self.lastCharacter == '':
            self.label_write.setText(self.label_write.text())
            return
        self.lastCharacter = ')'
        self.lastButton = 'op'
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' ) ')

    def div_pressed(self):
        if self.lastButton == 'op' or self.lastCharacter == '':
            self.label_write.setText(self.label_write.text())
        return
        self.lastCharacter = '/'
        self.lastButton = 'op'
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' / ')

    def root_pressed(self):
        if self.lastCharacter == '.':
            self.label_write.setText(self.label_write.text())
        return
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' √ ')

    def factorial_pressed(self):
        self.equals_pressed()
        if self.label_Ans == 'ERROR':
            return

        if self.ans[-1] != '0' or self.ans[-2] !=  '.':
            self.label_Ans.setText('ERROR')
            self.label_write.setText('')
            self.lastCharacter = ''
            self.lastButton = ''
            self.decimalDot = 'false'
            self.ans = '0'
        else:
            self.ans = self.ans.strip('.0')
            self.label_Ans.setText(self.ans)
        
        try:
            self.ans = str(Mathlibrary.factorial(int(self.label_Ans.text())))
        except:
            self.label_Ans.setText('ERROR')
            self.label_write.setText('')
            self.lastCharacter = ''
            self.lastButton = ''
            self.decimalDot = 'false'
            self.ans = '0'
            return

        self.label_Ans.setText(self.ans)
        self.label_write.setText('')


    def clean_pressed(self):
        self.label_write.setText("") 
        self.label_Ans.setText("") 
        self.lastCharacter = ''
        self.lastButton = ''
        self.decimalDot = 'false'
        self.ans = '0'

    def ans_pressed(self):
        if self.lastButton == 'dig' or self.lastCharacter == '.':
            return
        self.label_write.setText(self.label_write.text() + "ANS")
        self.lastButton = 'dig'
        self.lastCharacter = 'a'


    def equals_pressed(self):
        if self.label_write.text() == "":
            self.label_Ans.setText('0')
            return

        # takes care of the substitution of self.ans for its actual value
        if 'ANS' in self.label_write.text():
            if '-' in self.ans:
                self.ans = self.ans[:1] + ' ' + self.ans[1:]
            self.label_write.setText(self.label_write.text().replace("ANS", self.ans))

        try:
            self.ans = str(evaluate.resolve(self.label_write.text()))
        except:
            self.label_Ans.setText('ERROR')
            self.label_write.setText('')
            self.lastCharacter = ''
            self.lastButton = ''
            self.decimalDot = 'false'
            self.ans = '0'
            return

        self.label_Ans.setText(self.ans)
        self.label_write.setText('')
