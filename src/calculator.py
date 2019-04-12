from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator
import evaluate

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
        if self.lastCharacter == ')':
            return

        button = self.sender()
        self.label_write.setText(self.label_write.text() + button.text())

        self.lastCharacter = button.text()
        self.lastButton = 'dig'

    def decimal_pressed(self):
        if self.lastButton == 'op' or self.decimalDot == 'true':
            return
        self.decimalDot = 'true'
        self.label_write.setText(self.label_write.text() + '.')

    def plus_pressed(self):
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' + ')

    def minus_pressed(self):
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' - ')

    def powr_pressed(self):
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' ^ ')

    # vyhodnoti aktualni vstup a vysledek posle do metody ln
    def ln_pressed(self):
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + 'ln')

    def mul_pressed(self):
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' * ')

    def bracketL_pressed(self):
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' ( ')

    def bracketR_pressed(self):
        self.lastCharacter = ')'
        self.lastButton = 'op'
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' ) ')

    def div_pressed(self):
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' / ')

    def root_pressed(self):
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + ' √ ')

    # vyhodnoti aktualni vstup a vysledek posle do metody factorial
    def factorial_pressed(self):
        self.decimalDot = 'false'
        self.label_write.setText(self.label_write.text() + '!')

    def clean_pressed(self):
        self.label_write.setText("") 
        self.lastCharacter = ''
        self.lastButton = ''
        self.decimalDot = 'false'
        self.ans = '0'

    def ans_pressed(self):
        self.label_write.setText(self.label_write.text() + " ANS ")

    def equals_pressed(self):
        self.label_Ans.setText(str(evaluate.resolve(self.label_write.text())))
